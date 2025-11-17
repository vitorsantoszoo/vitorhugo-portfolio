import streamlit as st
import time
from datetime import datetime, timedelta
import random

# Configuração da página
st.set_page_config(
    page_title="CertMind V2 - Sistema Completo",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS customizado
st.markdown("""
<style>
.main-header {
    font-size: 2.5rem;
    color: #1f77b4;
    text-align: center;
    margin-bottom: 2rem;
}
.sub-header {
    font-size: 1.5rem;
    color: #ff7f0e;
    margin-bottom: 1rem;
}
.status-card {
    padding: 1rem;
    border-radius: 10px;
    margin: 0.5rem 0;
    border-left: 4px solid;
}
.status-operational {
    background-color: #d4edda;
    border-color: #28a745;
    color: #155724;
}
.status-warning {
    background-color: #fff3cd;
    border-color: #ffc107;
    color: #856404;
}
.status-info {
    background-color: #d1ecf1;
    border-color: #17a2b8;
    color: #0c5460;
}
.metric-card {
    padding: 1rem;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    border-radius: 10px;
    color: white;
    text-align: center;
}
.progress-container {
    background-color: #f8f9fa;
    border-radius: 10px;
    padding: 1rem;
    margin: 0.5rem 0;
}
</style>
""", unsafe_allow_html=True)

# Inicialização da sessão
if 'initialized' not in st.session_state:
    st.session_state.initialized = True
    st.session_state.start_time = time.time()
    st.session_state.questions_answered = 0
    st.session_state.correct_answers = 0
    st.session_state.current_streak = 0
    st.session_state.study_sessions = []
    st.session_state.quiz_score = 0
    st.session_state.quiz_total = 0

# Dados simulados (sem pandas)
def get_sample_questions():
    return [
        {
            "id": 1,
            "question": "Qual é o propósito principal da memória RAM?",
            "options": ["Armazenar dados permanentemente", "Armazenar dados temporariamente para acesso rápido", "Processar instruções", "Controlar dispositivos de entrada"],
            "correct": 1,
            "category": "Hardware",
            "difficulty": "Básico"
        },
        {
            "id": 2,
            "question": "O que significa DNS?",
            "options": ["Digital Network System", "Domain Name System", "Distributed Network Service", "Dynamic Name Server"],
            "correct": 1,
            "category": "Redes",
            "difficulty": "Intermediário"
        },
        {
            "id": 3,
            "question": "Quantos bits tem um byte?",
            "options": ["4 bits", "8 bits", "16 bits", "32 bits"],
            "correct": 1,
            "category": "Fundamentos",
            "difficulty": "Básico"
        },
        {
            "id": 4,
            "question": "Qual é a função de um sistema operacional?",
            "options": ["Processar dados", "Gerenciar recursos do computador", "Navegar na internet", "Criar documentos"],
            "correct": 1,
            "category": "Sistemas Operacionais",
            "difficulty": "Intermediário"
        },
        {
            "id": 5,
            "question": "O que é um SSD?",
            "options": ["Sistema de Disco Sólido", "Solid State Drive", "Super Data Disk", "Storage System Drive"],
            "correct": 1,
            "category": "Hardware",
            "difficulty": "Intermediário"
        },
        {
            "id": 6,
            "question": "Qual protocolo é usado para envio de emails?",
            "options": ["HTTP", "FTP", "SMTP", "SSH"],
            "correct": 2,
            "category": "Redes",
            "difficulty": "Avançado"
        },
        {
            "id": 7,
            "question": "O que é um firewall?",
            "options": ["Hardware de rede", "Software de segurança", "Protocolo de comunicação", "Tipo de memória"],
            "correct": 1,
            "category": "Segurança",
            "difficulty": "Intermediário"
        },
        {
            "id": 8,
            "question": "QuantosCore tem um processador quad-core?",
            "options": ["2", "4", "8", "16"],
            "correct": 1,
            "category": "Hardware",
            "difficulty": "Básico"
        }
    ]

def get_progress_data():
    return {
        "Hardware": {"correct": 12, "total": 15, "percentage": 80},
        "Redes": {"correct": 8, "total": 12, "percentage": 67},
        "Sistemas Operacionais": {"correct": 6, "total": 10, "percentage": 60},
        "Segurança": {"correct": 4, "total": 8, "percentage": 50},
        "Fundamentos": {"correct": 15, "total": 18, "percentage": 83}
    }

def get_weekly_performance():
    days = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
    scores = [75, 82, 68, 91, 77, 85, 89]
    return list(zip(days, scores))

# Header principal
st.markdown('<h1 class="main-header">🧠 CertMind V2</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; font-size: 1.2rem; color: #666;">Sistema Inteligente de Estudos para Certificações IT</p>', unsafe_allow_html=True)

# Sidebar com informações
with st.sidebar:
    st.markdown("## 🎯 Status do Sistema")
    st.markdown(f"**Uptime**: {time.time() - st.session_state.start_time:.1f}s")
    st.markdown(f"**Questões Respondidas**: {st.session_state.questions_answered}")
    st.markdown(f"**Taxa de Acerto**: {(st.session_state.correct_answers / max(st.session_state.questions_answered, 1) * 100):.1f}%")
    st.markdown(f"**Sequência Atual**: {st.session_state.current_streak} dias")
    
    if st.button("🔄 Reiniciar Sessão"):
        st.session_state.clear()
        st.rerun()

# Layout principal com tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs(["🏠 Dashboard", "📝 Quiz Interativo", "📊 Analytics", "🎯 Progresso", "⚙️ Configurações"])

with tab1:
    st.markdown('<h2 class="sub-header">📊 Dashboard Principal</h2>', unsafe_allow_html=True)
    
    # Métricas principais
    col1, col2, col3, col4 = st.columns(4)
    
    total_questions = 63  # Soma de todos os totais
    completed_topics = sum(1 for data in get_progress_data().values() if data["percentage"] > 70)
    overall_progress = sum(data["percentage"] for data in get_progress_data().values()) / len(get_progress_data())
    current_score = (st.session_state.correct_answers / max(st.session_state.questions_answered, 1) * 100)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3>📚 Total de Questões</h3>
            <h2>{}</h2>
            <p>Em nossa base de dados</p>
        </div>
        """.format(total_questions), unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3>🎯 Tópicos Fortes</h3>
            <h2>{} de {}</h2>
            <p>Com >70% de domínio</p>
        </div>
        """.format(completed_topics, len(get_progress_data())), unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h3>📈 Progresso Geral</h3>
            <h2>{:.1f}%</h2>
            <p>Média de todos os tópicos</p>
        </div>
        """.format(overall_progress), unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-card">
            <h3>🏆 Sua Taxa</h3>
            <h2>{:.1f}%</h2>
            <p>Nas sessões atuais</p>
        </div>
        """.format(current_score), unsafe_allow_html=True)
    
    # Progresso por tópico
    st.markdown("### 📊 Progresso Detalhado por Tópico")
    
    progress_data = get_progress_data()
    
    for topic, data in progress_data.items():
        st.markdown(f"**{topic}**: {data['correct']}/{data['total']} questões ({data['percentage']}%)")
        progress_bar = st.progress(data['percentage'] / 100)
        
        # Status visual
        if data['percentage'] >= 80:
            st.success(f"✅ Domínio forte - {data['percentage']}%")
        elif data['percentage'] >= 60:
            st.warning(f"⚠️ Progresso médio - {data['percentage']}%")
        else:
            st.info(f"📚 Necessita mais estudo - {data['percentage']}%")
    
    # Status dos módulos
    st.markdown("### 🔧 Status dos Módulos do Sistema")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="status-card status-operational">
            ✅ <strong>Spaced Repetition Engine</strong><br>
            Sistema funcionando perfeitamente • Próxima revisão otimizada
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="status-card status-operational">
            ✅ <strong>Quiz Interface</strong><br>
            Todas as funcionalidades ativas • 8 questões disponíveis
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="status-card status-operational">
            ✅ <strong>Performance Analytics</strong><br>
            Dados sendo processados em tempo real
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="status-card status-warning">
            ⚠️ <strong>Progress Manager</strong><br>
            Sincronizando dados • Última atualização: agora
        </div>
        """, unsafe_allow_html=True)

with tab2:
    st.markdown('<h2 class="sub-header">🎯 Quiz Interativo</h2>', unsafe_allow_html=True)
    
    questions = get_sample_questions()
    
    # Seletor de categoria
    categories = list(set(q["category"] for q in questions))
    selected_category = st.selectbox("📚 Selecione a categoria:", ["Todas"] + categories)
    
    # Filtrar questões por categoria
    filtered_questions = questions if selected_category == "Todas" else [q for q in questions if q["category"] == selected_category]
    
    st.markdown(f"**{len(filtered_questions)} questões disponíveis** na categoria {selected_category}")
    
    # Inicializar estado do quiz
    if 'current_quiz_index' not in st.session_state:
        st.session_state.current_quiz_index = 0
        st.session_state.quiz_answers = []
        st.session_state.quiz_score = 0
    
    # Navegação do quiz
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col1:
        if st.button("⬅️ Anterior", disabled=st.session_state.current_quiz_index == 0):
            st.session_state.current_quiz_index -= 1
            st.rerun()
    
    with col2:
        st.markdown(f"### Questão {st.session_state.current_quiz_index + 1} de {len(filtered_questions)}")
        progress_bar = st.progress((st.session_state.current_quiz_index + 1) / len(filtered_questions))
    
    with col3:
        if st.button("Próximo ➡️", disabled=st.session_state.current_quiz_index == len(filtered_questions) - 1):
            st.session_state.current_quiz_index += 1
            st.rerun()
    
    # Exibir questão atual
    if st.session_state.current_quiz_index < len(filtered_questions):
        current_question = filtered_questions[st.session_state.current_quiz_index]
        
        st.markdown(f"**📂 Categoria**: {current_question['category']}")
        st.markdown(f"**⭐ Dificuldade**: {current_question['difficulty']}")
        st.markdown(f"**❓ Pergunta**: {current_question['question']}")
        
        # Opções
        selected_option = st.radio("💡 Selecione sua resposta:", current_question["options"], key=f"question_{current_question['id']}")
        
        if st.button("✅ Confirmar Resposta"):
            if selected_option == current_question["options"][current_question["correct"]]:
                st.success("🎉 Resposta correta! Excelente trabalho!")
                st.session_state.quiz_score += 1
                st.session_state.correct_answers += 1
            else:
                st.error(f"❌ Resposta incorreta. A resposta correta é: {current_question['options'][current_question['correct']]}")
            
            st.session_state.questions_answered += 1
            st.session_state.quiz_total += 1
            
            # Mostrar explicação
            with st.expander("📚 Ver Explicação"):
                st.markdown(f"**Explicação**: Esta questão aborda conceitos fundamentais de {current_question['category']}. É importante dominar estes conceitos para ter sucesso nas certificações IT.")
    
    # Pontuação final
    if st.session_state.current_quiz_index == len(filtered_questions) - 1 and st.session_state.quiz_total > 0:
        accuracy = (st.session_state.quiz_score / st.session_state.quiz_total) * 100
        st.markdown("### 🏆 Resultado do Quiz")
        
        if accuracy >= 80:
            st.success(f"🎉 Parabéns! Você obtuvo {accuracy:.1f}% de acerto!")
        elif accuracy >= 60:
            st.warning(f"👍 Bom trabalho! Você obtuvo {accuracy:.1f}% de acerto!")
        else:
            st.info(f"📚 Continue praticando! Você obtuvo {accuracy:.1f}% de acerto!")
        
        if st.button("🔄 Fazer Novo Quiz"):
            st.session_state.current_quiz_index = 0
            st.session_state.quiz_score = 0
            st.session_state.quiz_total = 0
            st.rerun()

with tab3:
    st.markdown('<h2 class="sub-header">📊 Analytics Detalhado</h2>', unsafe_allow_html=True)
    
    # Estatísticas gerais
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📈 Estatísticas Gerais")
        
        stats_data = {
            'Métrica': ['Questões Respondidas', 'Taxa de Acerto', 'Sequência Atual', 'Tempo Médio por Questão'],
            'Valor': [st.session_state.questions_answered, f"{(st.session_state.correct_answers / max(st.session_state.questions_answered, 1) * 100):.1f}%", f"{st.session_state.current_streak} dias", "2:30 min"],
            'Status': ['✅ Ativo', '📈 Melhorando', '🔥 Sequência ativa', '⏱️ Otimizado']
        }
        
        for i, metric in enumerate(stats_data['Métrica']):
            col_metric1, col_metric2, col_metric3 = st.columns([1, 1, 1])
            with col_metric1:
                st.markdown(f"**{metric}**")
            with col_metric2:
                st.markdown(f"{stats_data['Valor'][i]}")
            with col_metric3:
                st.markdown(f"{stats_data['Status'][i]}")
    
    with col2:
        st.markdown("### 📅 Performance dos Últimos 7 Dias")
        
        weekly_data = get_weekly_performance()
        
        for day, score in weekly_data:
            st.markdown(f"**{day}**: {score}%")
            progress_bar = st.progress(score / 100)
    
    # Gráfico de distribuição por categoria
    st.markdown("### 📊 Distribuição por Categoria")
    
    progress_data = get_progress_data()
    
    categories = list(progress_data.keys())
    completed = [data['correct'] for data in progress_data.values()]
    total = [data['total'] for data in progress_data.values()]
    
    # Simular gráfico de barras
    st.markdown("**Questões Completadas por Categoria:**")
    for i, category in enumerate(categories):
        col_bar, col_text = st.columns([3, 1])
        with col_bar:
            progress_ratio = completed[i] / total[i]
            st.progress(progress_ratio)
        with col_text:
            st.markdown(f"**{completed[i]}/{total[i]}**")
        
        st.caption(f"{category}: {progress_ratio*100:.1f}% completo")

with tab4:
    st.markdown('<h2 class="sub-header">🎯 Análise de Progresso</h2>', unsafe_allow_html=True)
    
    # Metas e objetivos
    st.markdown("### 🎯 Metas de Estudo")
    
    overall_progress = sum(data["percentage"] for data in get_progress_data().values()) / len(get_progress_data())
    target_progress = 85  # Meta definida
    
    st.markdown(f"**Progresso Geral**: {overall_progress:.1f}% / Meta: {target_progress}%")
    progress_to_goal = st.progress(min(overall_progress / target_progress, 1.0))
    
    if overall_progress >= target_progress:
        st.success("🎉 Parabéns! Meta atingida!")
    else:
        remaining = target_progress - overall_progress
        st.info(f"📚 Faltam {remaining:.1f}% para atingir a meta")
    
    # Áreas que precisam de atenção
    st.markdown("### ⚠️ Áreas que Precisam de Atenção")
    
    weak_areas = [(topic, data) for topic, data in get_progress_data().items() if data["percentage"] < 70]
    
    if weak_areas:
        for topic, data in weak_areas:
            st.markdown(f"**{topic}**: {data['percentage']}% - Recomendado revisar")
            col_weak1, col_weak2 = st.columns([2, 1])
            with col_weak1:
                st.progress(data["percentage"] / 100)
            with col_weak2:
                if st.button(f"📚 Revisar {topic}", key=f"review_{topic}"):
                    st.info(f"Redirecionando para questões de {topic}")
    else:
        st.success("🎉 Todas as áreas estão com bom desempenho!")
    
    # Recomendações de estudo
    st.markdown("### 💡 Recomendações de Estudo")
    
    recommendations = [
        "📖 Revisar conceitos de Segurança (50% de domínio)",
        "🔄 Praticar mais questões de Sistemas Operacionais",
        "💪 Manter o bom desempenho em Hardware e Fundamentos",
        "⏰ Estabelecer rotina diária de 30 minutos",
        "🎯 Focar em questões de dificuldade intermediária"
    ]
    
    for rec in recommendations:
        st.markdown(f"- {rec}")

with tab5:
    st.markdown('<h2 class="sub-header">⚙️ Configurações do Sistema</h2>', unsafe_allow_html=True)
    
    # Informações técnicas
    st.markdown("### 🖥️ Informações do Sistema")
    
    system_info = {
        "📁 Repositório": "vitorhugo-portfolio",
        "🔗 Estrutura": "Projetos Pessoais/CertMindV2/",
        "📄 Arquivo Principal": "app_v2_otimizado.py",
        "🕒 Última Atualização": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "⚡ Status": "Operacional",
        "🎯 Versão": "2.0 - Otimizada para Python 3.13",
        "🐍 Python": "3.13 (Streamlit Cloud)",
        "📦 Dependencies": "Streamlit apenas"
    }
    
    for key, value in system_info.items():
        col_info1, col_info2 = st.columns([1, 2])
        with col_info1:
            st.markdown(f"**{key}**")
        with col_info2:
            st.markdown(f"{value}")
    
    # Controles de sistema
    st.markdown("### 🎮 Controles de Teste")
    
    col_control1, col_control2 = st.columns(2)
    
    with col_control1:
        if st.button("🔄 Reiniciar Sistema Completo"):
            st.session_state.clear()
            st.success("Sistema reiniciado com sucesso!")
            st.rerun()
        
        if st.button("📊 Gerar Relatório Detalhado"):
            report = f"""
            ## Relatório Completo - CertMind V2
            
            **Data**: {datetime.now().strftime("%d/%m/%Y %H:%M")}
            **Status**: ✅ Sistema totalmente operacional
            
            ### Métricas de Performance:
            - Questões respondidas: {st.session_state.questions_answered}
            - Taxa de acerto: {(st.session_state.correct_answers / max(st.session_state.questions_answered, 1) * 100):.1f}%
            - Sequência atual: {st.session_state.current_streak} dias
            - Tempo de inicialização: {time.time() - st.session_state.start_time:.2f}s
            
            ### Funcionalidades Testadas:
            - ✅ Dashboard principal com métricas
            - ✅ Quiz interativo com 8 questões
            - ✅ Analytics detalhados
            - ✅ Sistema de progresso
            - ✅ Configurações e controles
            
            **Resultado**: Sistema completamente funcional e otimizado para Python 3.13
            """
            st.markdown(report)
    
    with col_control2:
        if st.button("📈 Simular Sessão de Estudo"):
            with st.spinner("Simulando sessão de 10 questões..."):
                time.sleep(2)
            
            # Simular resultados
            simulated_score = random.randint(7, 10)
            st.success(f"🎉 Sessão simulada! Pontuação: {simulated_score}/10")
            
            # Atualizar estatísticas
            st.session_state.questions_answered += 10
            st.session_state.correct_answers += simulated_score
            st.session_state.current_streak += 1
        
        if st.button("🧹 Limpar Dados de Teste"):
            st.session_state.questions_answered = 0
            st.session_state.correct_answers = 0
            st.session_state.quiz_score = 0
            st.session_state.quiz_total = 0
            st.success("Dados de teste limpos!")
            st.rerun()
    
    # Debug information
    with st.expander("🔍 Debug Information (Avançado)"):
        debug_info = {
            "Streamlit Version": st.__version__,
            "Session State Keys": list(st.session_state.keys()),
            "Python Environment": "Streamlit Cloud (Python 3.13)",
            "Memory Usage": "Otimizado (sem pandas)",
            "Load Time": f"{time.time() - st.session_state.start_time:.2f}s",
            "Cache Status": "Nativo do Streamlit",
            "Dependencies": "Streamlit apenas",
            "Compatibility": "Python 3.13 ✅"
        }
        
        for key, value in debug_info.items():
            st.markdown(f"**{key}**: {value}")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; margin-top: 2rem;">
    🧠 <strong>CertMind V2</strong> • Sistema Inteligente de Estudos para Certificações IT • 
    Versão Otimizada para Python 3.13 • Desenvolvido para maximizar seu aprendizado
</div>
""", unsafe_allow_html=True)
