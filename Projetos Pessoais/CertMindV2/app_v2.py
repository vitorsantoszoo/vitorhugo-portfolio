"""
CertMind V2 - Sistema Inteligente de Estudo para Certificações
Aplicação principal com repetição espaçada, analytics e interface aprimorada
"""

import json
import os
import streamlit as st
from datetime import datetime

# Importar módulos do sistema
from progress_manager_v2 import ProgressManager
from spaced_repetition import SpacedRepetitionEngine
from analytics import PerformanceAnalytics, QuizInterface

# ==========================================
# CONFIGURAÇÃO INICIAL
# ==========================================

st.set_page_config(
    page_title="CertMind V2 — Estudo Inteligente",
    layout="wide",
    page_icon="🧠",
    initial_sidebar_state="expanded"
)

# CSS customizado
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1E88E5;
        text-align: center;
        margin-bottom: 10px;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 30px;
    }
    .stMetric {
        background-color: #f0f2f6;
        padding: 10px;
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# CARREGAR DADOS
# ==========================================

@st.cache_data
def load_question_bank(filename: str) -> dict:
    """Carrega banco de questões"""
    path = os.path.join("data", filename)
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

# Carregar bancos de questões
try:
    core1_qbank = load_question_bank("core1_questions_v2.json")
    core2_qbank = load_question_bank("core2_questions_v2.json")
except FileNotFoundError:
    st.error("❌ Arquivos de questões não encontrados. Execute o script de migração primeiro.")
    st.stop()

# Inicializar gerenciadores (sem cache para manter estado atualizado)
if 'progress_manager' not in st.session_state:
    st.session_state.progress_manager = ProgressManager()
    st.session_state.sr_engine = SpacedRepetitionEngine()
    st.session_state.analytics = PerformanceAnalytics(st.session_state.progress_manager)
    st.session_state.quiz_interface = QuizInterface()

pm = st.session_state.progress_manager
sr_engine = st.session_state.sr_engine
analytics = st.session_state.analytics
quiz_ui = st.session_state.quiz_interface

# ==========================================
# HEADER
# ==========================================

st.markdown('<p class="main-header">🧠 CertMind V2</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Sistema Inteligente de Estudo para CompTIA A+</p>', unsafe_allow_html=True)

# ==========================================
# SIDEBAR - NAVEGAÇÃO
# ==========================================

st.sidebar.title("📚 Menu de Navegação")
page = st.sidebar.radio(
    "Escolha uma seção:",
    ["🎯 Quiz Inteligente", "📊 Dashboard", "ℹ️ Sobre o CertMind V2"],
    label_visibility="collapsed"
)

st.sidebar.markdown("---")

# Estatísticas rápidas na sidebar
st.sidebar.markdown("### 📈 Resumo Rápido")
quick_stats = pm.get_overall_stats()
st.sidebar.metric("Questões Estudadas", quick_stats['total_unique_questions'])
st.sidebar.metric("Conceitos Dominados", quick_stats['mastered_concepts'])
st.sidebar.metric("Sequência", f"{quick_stats['streak_days']} dias")

st.sidebar.markdown("---")

# Link para o projeto
st.sidebar.markdown("### 🔗 Links")
st.sidebar.markdown("[📂 GitHub do Projeto](https://github.com/vitorsantoszoo/vitorhugo-portfolio)")
st.sidebar.markdown("Made with ❤️ by Vitor Hugo")

# ==========================================
# PÁGINA: QUIZ INTELIGENTE
# ==========================================

if page == "🎯 Quiz Inteligente":
    
    st.markdown("## 🎯 Modo Quiz Inteligente")
    st.markdown("O sistema seleciona automaticamente as melhores questões para você estudar agora, baseado em:")
    st.markdown("- 🆕 Conceitos que você ainda não viu")
    st.markdown("- ⏰ Questões que estão prontas para revisão")
    st.markdown("- ⚠️ Tópicos onde você tem mais dificuldade")
    
    st.markdown("---")
    
    # Seleção de exame
    col1, col2 = st.columns([1, 3])
    
    with col1:
        exam_choice = st.selectbox(
            "📌 Escolha o exame:",
            ["Core 1 (220-1201)", "Core 2 (220-1202)"],
            key="exam_select"
        )
    
    # Selecionar banco de questões
    qbank = core1_qbank if exam_choice == "Core 1 (220-1201)" else core2_qbank
    all_questions = qbank['questions']
    
    # Opção de filtrar por domínio (opcional)
    with col2:
        domains = sorted(set(q['domain'] for q in all_questions))
        domain_filter = st.selectbox(
            "🔍 Filtrar por domínio (opcional):",
            ["Todos os domínios"] + domains,
            key="domain_filter"
        )
    
    # Aplicar filtro se necessário
    if domain_filter != "Todos os domínios":
        filtered_questions = [q for q in all_questions if q['domain'] == domain_filter]
    else:
        filtered_questions = all_questions
    
    st.markdown("---")
    
    # Obter questões prioritárias
    priority_questions = sr_engine.get_questions_to_review(
        filtered_questions,
        pm.get_performance_data(),
        limit=50
    )
    
    if not priority_questions:
        st.success("🎉 Você revisou todas as questões disponíveis!")
        st.info("💡 Volte amanhã para revisar conceitos que já estudou usando repetição espaçada.")
        st.stop()
    
    # Mostrar estatísticas do filtro atual
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info(f"📚 **{len(filtered_questions)}** questões disponíveis")
    
    with col2:
        st.success(f"⭐ **{len(priority_questions)}** questões prioritárias")
    
    with col3:
        # Calcular não vistas
        performance_data = pm.get_performance_data()
        never_seen = len([q for q in filtered_questions if q['id'] not in performance_data or performance_data[q['id']].get('attempts', 0) == 0])
        st.warning(f"🆕 **{never_seen}** não vistas")
    
    st.markdown("---")
    
    # ==========================================
    # SISTEMA DE QUIZ
    # ==========================================
    
    # Inicializar estado do quiz
    if 'current_question_idx' not in st.session_state:
        st.session_state.current_question_idx = 0
        st.session_state.answered = False
        st.session_state.user_answer = None
        pm.start_session()
    
    # Obter questão atual
    if st.session_state.current_question_idx >= len(priority_questions):
        st.success("🎉 Você completou todas as questões prioritárias desta sessão!")
        
        if st.button("🔄 Começar Nova Sessão"):
            st.session_state.current_question_idx = 0
            st.session_state.answered = False
            st.session_state.user_answer = None
            pm.start_session()
            st.rerun()
        
        st.stop()
    
    current_question = priority_questions[st.session_state.current_question_idx]
    
    # Obter performance anterior (se houver)
    performance = pm.get_question_performance(current_question['id'])
    
    # Mostrar progresso da sessão
    progress_pct = st.session_state.current_question_idx / len(priority_questions)
    st.progress(progress_pct)
    st.caption(f"Questão {st.session_state.current_question_idx + 1} de {len(priority_questions)}")
    
    st.markdown("---")
    
    # Renderizar questão
    quiz_ui.render_question_card(current_question, performance)
    
    # Renderizar opções
    if not st.session_state.answered:
        user_choice = quiz_ui.render_answer_options(current_question, key_suffix=str(st.session_state.current_question_idx))
        
        st.write("")
        
        col1, col2, col3 = st.columns([2, 1, 1])
        
        with col1:
            if st.button("✅ Confirmar Resposta", type="primary", use_container_width=True):
                if user_choice is None:
                    st.warning("⚠️ Por favor, selecione uma alternativa antes de confirmar.")
                else:
                    st.session_state.user_answer = user_choice
                    st.session_state.answered = True
                    st.rerun()
        
        with col2:
            if st.button("⏭️ Pular Questão", use_container_width=True):
                st.session_state.current_question_idx += 1
                st.session_state.answered = False
                st.session_state.user_answer = None
                st.rerun()
        
        with col3:
            if st.button("🏠 Voltar ao Início", use_container_width=True):
                st.session_state.current_question_idx = 0
                st.session_state.answered = False
                st.session_state.user_answer = None
                st.rerun()
    
    else:
        # Mostrar feedback
        is_correct = st.session_state.user_answer == current_question['answer']
        
        # Registrar resposta
        feedback_data = pm.record_answer(
            question_id=current_question['id'],
            is_correct=is_correct,
            exam=exam_choice,
            domain=current_question['domain'],
            subdomain=current_question['subdomain']
        )
        
        # Renderizar feedback
        quiz_ui.render_feedback(current_question, st.session_state.user_answer, is_correct, feedback_data)
        
        # Botão de próxima questão
        col1, col2 = st.columns([3, 1])
        
        with col1:
            if st.button("➡️ Próxima Questão", type="primary", use_container_width=True):
                st.session_state.current_question_idx += 1
                st.session_state.answered = False
                st.session_state.user_answer = None
                st.rerun()
        
        with col2:
            if st.button("🏠 Início", use_container_width=True):
                st.session_state.current_question_idx = 0
                st.session_state.answered = False
                st.session_state.user_answer = None
                st.rerun()

# ==========================================
# PÁGINA: DASHBOARD
# ==========================================

elif page == "📊 Dashboard":
    
    # Renderizar dashboard completo
    analytics.render_dashboard()
    
    st.markdown("---")
    
    # Opções administrativas
    with st.expander("⚙️ Opções Avançadas"):
        st.warning("⚠️ Use com cuidado!")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("🗑️ Resetar Todo o Progresso"):
                if st.button("⚠️ Confirmar Reset (clique novamente)"):
                    pm.reset_progress()
                    st.success("Progresso resetado com sucesso!")
                    st.rerun()
        
        with col2:
            st.download_button(
                label="💾 Exportar Dados",
                data=json.dumps(pm.data, indent=2, ensure_ascii=False),
                file_name=f"certmind_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                mime="application/json"
            )

# ==========================================
# PÁGINA: SOBRE
# ==========================================

elif page == "ℹ️ Sobre o CertMind V2":
    
    st.markdown("## 📖 Sobre o CertMind V2")
    
    st.markdown("""
    ### 🎯 O que é o CertMind?
    
    O **CertMind** é um sistema inteligente de estudo desenvolvido especificamente para auxiliar na preparação 
    para certificações técnicas de TI, começando com a **CompTIA A+**.
    
    ### ✨ Novidades da Versão 2.0
    
    #### 🧠 Sistema de Repetição Espaçada
    - Baseado no algoritmo **SM-2 (SuperMemo 2)**
    - Otimiza o momento ideal para revisar cada conceito
    - Maximiza retenção de longo prazo com menos esforço
    
    #### 📊 Analytics Avançado
    - Dashboard completo com estatísticas detalhadas
    - Identificação automática de áreas fracas
    - Recomendações personalizadas de estudo
    - Tracking de sequência de dias estudando
    
    #### 🎯 Seleção Inteligente de Questões
    - Prioriza conceitos não vistos
    - Identifica questões prontas para revisão
    - Foca em tópicos com dificuldade
    - Elimina redundâncias do banco de questões
    
    #### 💎 Feedback Rico
    - Explicações detalhadas para cada questão
    - Métricas de performance individuais
    - Níveis de domínio por conceito
    - Tags e categorização inteligente
    
    ### 🏗️ Arquitetura do Sistema
    
    ```
    CertMind V2
    ├── 📊 progress_manager_v2.py    - Gerenciamento de progresso
    ├── 🧠 spaced_repetition.py      - Algoritmo de repetição espaçada
    ├── 📈 analytics.py               - Sistema de análise e visualizações
    ├── 🎨 app_v2.py                  - Interface principal (Streamlit)
    └── 📦 data/
        ├── core1_questions_v2.json  - Banco de questões Core 1
        ├── core2_questions_v2.json  - Banco de questões Core 2
        └── progress_v2.json         - Dados de progresso do usuário
    ```
    
    ### 📚 Certificações Suportadas
    
    #### ✅ Disponível Agora:
    - **CompTIA A+ Core 1 (220-1201)** - 51 questões únicas
    - **CompTIA A+ Core 2 (220-1202)** - 45 questões únicas
    
    #### 🔜 Planejado para o Futuro:
    - CompTIA Network+
    - CompTIA Security+
    - Cisco CCNA
    - AWS Cloud Practitioner
    - E mais...
    
    ### 🔬 Como Funciona a Repetição Espaçada?
    
    O sistema calcula o momento ideal para revisar cada conceito baseado em:
    
    1. **Taxa de Acerto**: Quanto melhor você responde, maior o intervalo
    2. **Tentativas**: Conceitos respondidos múltiplas vezes são espaçados mais
    3. **Histórico**: O sistema aprende com seu padrão de respostas
    4. **Dificuldade**: Conceitos difíceis são revistos com mais frequência
    
    **Intervalos típicos:**
    - Primeira revisão: 1 dia
    - Segunda revisão: 6 dias
    - Terceira+ revisão: Intervalo anterior × fator de facilidade
    
    ### 🎓 Metodologia de Estudo Recomendada
    
    1. **📚 Estudo Teórico**: Primeiro, estude o material oficial
    2. **🎯 Quiz Inicial**: Teste seu conhecimento com o CertMind
    3. **📊 Análise**: Identifique áreas fracas no dashboard
    4. **🔁 Revisão**: Foque nos tópicos com dificuldade
    5. **⏰ Repetição Espaçada**: Volte nos intervalos sugeridos
    6. **✅ Domínio**: Continue até dominar 80%+ dos conceitos
    
    ### 👨‍💻 Sobre o Desenvolvedor
    
    **Vitor Hugo** - Profissional de TI apaixonado por educação, segurança da informação 
    e proteção de dados. O CertMind nasceu da necessidade pessoal de uma ferramenta 
    de estudo mais eficiente e evoluiu para ajudar outros profissionais.
    
    ### 🤝 Contribuições
    
    O projeto é **open source** e aceita contribuições! Se você tem ideias para melhorias,
    encontrou bugs ou quer adicionar novas certificações, sinta-se à vontade para contribuir.
    
    📧 **Contato**: Abra uma issue no GitHub
    🔗 **Repositório**: [github.com/vitorsantoszoo/vitorhugo-portfolio](https://github.com/vitorsantoszoo/vitorhugo-portfolio)
    
    ### 📄 Licença
    
    Este projeto é disponibilizado para uso educacional. O conteúdo das questões é baseado 
    nos objetivos oficiais da CompTIA A+ e foi adaptado para fins de estudo.
    
    ---
    
    **Versão**: 2.0  
    **Última Atualização**: Novembro 2025  
    **Status**: ✅ Estável e Pronto para Uso
    """)
    
    st.balloons()
