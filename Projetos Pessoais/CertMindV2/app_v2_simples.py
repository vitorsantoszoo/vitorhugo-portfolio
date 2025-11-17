import streamlit as st
import pandas as pd
import time
import json
from datetime import datetime, timedelta
import random

# Configuração da página
st.set_page_config(
    page_title="CertMind V2 - Teste",
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
}
</style>
""", unsafe_allow_html=True)

# Header principal
st.markdown('<h1 class="main-header">🧠 CertMind V2</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; font-size: 1.2rem; color: #666;">Sistema de Estudos para Certificações IT</p>', unsafe_allow_html=True)

# Controle de inicialização
if 'initialized' not in st.session_state:
    with st.spinner("🔄 Inicializando sistema..."):
        st.session_state.initialized = True
        st.session_state.start_time = time.time()
        time.sleep(1.5)  # Simula carregamento rápido
        st.success("✅ Sistema inicializado com sucesso!")

# Sidebar com informações
st.sidebar.markdown("## 🔍 Status do Sistema")
st.sidebar.markdown(f"**Tempo de inicialização**: {time.time() - st.session_state.start_time:.2f}s")
st.sidebar.markdown(f"**Versão**: 2.0 - Teste")

# Simulação de dados (em versão real, estes viriam dos módulos)
def generate_sample_data():
    """Gera dados de exemplo para demonstração"""
    return {
        'questions': [
            {"id": 1, "question": "Qual é o propósito da memória RAM?", "answer": "Armazenar dados temporariamente para acesso rápido", "category": "Hardware"},
            {"id": 2, "question": "O que significa DNS?", "answer": "Domain Name System - Sistema de Nomes de Domínio", "category": "Redes"},
            {"id": 3, "question": "Quantos bits tem um byte?", "answer": "8 bits", "category": "Fundamentos"}
        ],
        'progress': [
            {"topic": "Hardware", "correct": 15, "total": 20, "percentage": 75},
            {"topic": "Redes", "correct": 8, "total": 15, "percentage": 53},
            {"topic": "Fundamentos", "correct": 12, "total": 18, "percentage": 67}
        ]
    }

# Carregamento de dados otimizado
@st.cache_data(ttl=300)  # Cache por 5 minutos
def load_certmind_data():
    with st.spinner("📚 Carregando dados do curso..."):
        time.sleep(1)  # Simula carregamento real
        return generate_sample_data()

# Carregar dados
data = load_certmind_data()

# Layout principal
tab1, tab2, tab3, tab4 = st.tabs(["🏠 Dashboard", "📝 Quiz", "📊 Progresso", "⚙️ Configurações"])

with tab1:
    st.markdown('<h2 class="sub-header">📊 Dashboard Principal</h2>', unsafe_allow_html=True)
    
    # Métricas principais
    col1, col2, col3, col4 = st.columns(4)
    
    total_questions = len(data['questions'])
    completed_topics = len([p for p in data['progress'] if p['percentage'] > 80])
    overall_progress = sum([p['percentage'] for p in data['progress']]) / len(data['progress'])
    
    with col1:
        st.metric("Total de Questões", total_questions, "+3 hoje")
    with col2:
        st.metric("Tópicos Concluídos", completed_topics, f"{completed_topics} de {len(data['progress'])}")
    with col3:
        st.metric("Progresso Geral", f"{overall_progress:.1f}%", "+2% esta semana")
    with col4:
        st.metric("Taxa de Acerto", "68.3%", "+1.2% esta semana")
    
    # Gráfico de progresso por tópico
    st.markdown("### 📈 Progresso por Tópico")
    
    progress_df = pd.DataFrame(data['progress'])
    st.bar_chart(progress_df.set_index('topic')['percentage'])
    
    # Status cards
    st.markdown("### 🎯 Status dos Módulos")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="status-card" style="background-color: #d4edda; color: #155724;">
            ✅ <strong>Spaced Repetition</strong><br>
            Sistema funcionando perfeitamente
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="status-card" style="background-color: #d1ecf1; color: #0c5460;">
            📊 <strong>Analytics</strong><br>
            Dados carregando corretamente
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="status-card" style="background-color: #fff3cd; color: #856404;">
            🎯 <strong>Quiz Interface</strong><br>
            Pronto para simulados
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="status-card" style="background-color: #f8d7da; color: #721c24;">
            📁 <strong>Progress Manager</strong><br>
            Sincronizando dados...
        </div>
        """, unsafe_allow_html=True)

with tab2:
    st.markdown('<h2 class="sub-header">🎯 Quiz Interativo</h2>', unsafe_allow_html=True)
    
    if 'current_question' not in st.session_state:
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.session_state.answers = []
    
    # Navegação do quiz
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col1:
        if st.button("⬅️ Anterior", disabled=st.session_state.current_question == 0):
            st.session_state.current_question -= 1
            st.rerun()
    
    with col2:
        st.markdown(f"### Questão {st.session_state.current_question + 1} de {total_questions}")
        progress_bar = st.progress((st.session_state.current_question + 1) / total_questions)
    
    with col3:
        if st.button("Próximo ➡️", disabled=st.session_state.current_question == total_questions - 1):
            st.session_state.current_question += 1
            st.rerun()
    
    # Exibir questão atual
    if st.session_state.current_question < total_questions:
        question = data['questions'][st.session_state.current_question]
        
        st.markdown(f"**📚 Categoria**: {question['category']}")
        st.markdown(f"**❓ Pergunta**: {question['question']}")
        
        # Resposta (em versão real, seria um input do usuário)
        answer = st.text_input("💬 Sua resposta:", key=f"answer_{st.session_state.current_question}")
        
        if st.button("✅ Verificar Resposta"):
            if answer.lower().strip() == question['answer'].lower().strip():
                st.success("🎉 Resposta correta!")
                st.session_state.score += 1
            else:
                st.error(f"❌ Incorreto. Resposta: {question['answer']}")
    
    # Pontuação
    if st.session_state.current_question > 0:
        accuracy = (st.session_state.score / st.session_state.current_question) * 100
        st.markdown(f"**🎯 Pontuação atual**: {st.session_state.score}/{st.session_state.current_question} ({accuracy:.1f}%)")

with tab3:
    st.markdown('<h2 class="sub-header">📈 Analytics Detalhado</h2>', unsafe_allow_html=True)
    
    # Métricas detalhadas
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📊 Estatísticas Gerais")
        
        stats_data = {
            'Métrica': ['Questões Respondidas', 'Taxa de Acerto', 'Tempo Médio', 'Sequência Atual'],
            'Valor': [st.session_state.get('total_answered', 35), '68.3%', '2:30 min', '12 dias'],
            'Tendência': ['↗️ +5', '↗️ +2.1%', '↘️ -15s', '🔥 Sequência ativa']
        }
        
        st.dataframe(stats_data, use_container_width=True)
    
    with col2:
        st.markdown("### 🎯 Performance por Dia")
        
        # Simular dados de performance semanal
        days = ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab', 'Dom']
        scores = [75, 82, 68, 91, 77, 85, 89]
        
        chart_data = pd.DataFrame({
            'Dia': days,
            'Pontuação': scores
        })
        
        st.line_chart(chart_data.set_index('Dia'))
    
    # Gráfico de pizza por categoria
    st.markdown("### 📚 Distribuição por Categoria")
    
    category_data = pd.DataFrame({
        'Categoria': ['Hardware', 'Redes', 'Fundamentos', 'Sistemas Operacionais'],
        'Questões': [20, 15, 18, 12],
        'Concluídas': [15, 8, 12, 7]
    })
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.bar_chart(category_data.set_index('Categoria')[['Questões', 'Concluídas']])
    
    with col2:
        # Gráfico de pizza das conclusões
        st.markdown("**Taxa de Conclusão por Categoria:**")
        for idx, row in category_data.iterrows():
            completion_rate = (row['Concluídas'] / row['Questões']) * 100
            st.progress(completion_rate / 100)
            st.caption(f"{row['Categoria']}: {completion_rate:.1f}%")

with tab4:
    st.markdown('<h2 class="sub-header">⚙️ Configurações do Sistema</h2>', unsafe_allow_html=True)
    
    # Informações do sistema
    st.markdown("### 🖥️ Informações Técnicas")
    
    system_info = {
        "📁 Repositório": "vitorhugo-portfolio",
        "🔗 Estrutura": "Projetos Pessoais/CertMindV2/",
        "📄 Arquivo Principal": "app_v2_simples.py",
        "🕒 Última Atualização": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "⚡ Status": "Operacional",
        "🎯 Versão": "2.0 - Teste Otimizado"
    }
    
    for key, value in system_info.items():
        st.markdown(f"**{key}**: {value}")
    
    # Controles de sistema
    st.markdown("### 🎮 Controles de Teste")
    
    if st.button("🔄 Reiniciar Sistema"):
        st.session_state.clear()
        st.success("Sistema reiniciado com sucesso!")
        st.rerun()
    
    if st.button("📊 Gerar Relatório de Teste"):
        report = f"""
        ## Relatório de Teste - CertMind V2
        
        **Data**: {datetime.now().strftime("%d/%m/%Y %H:%M")}
        **Status**: ✅ Funcionando
        **Tempo de Carregamento**: {time.time() - st.session_state.start_time:.2f}s
        **Funcionalidades Testadas**: Dashboard, Quiz, Analytics, Configurações
        
        **Resultado**: Sistema operacional e responsivo.
        """
        st.markdown(report)
    
    # Debug information
    with st.expander("🔍 Debug Information (Avançado)"):
        debug_info = {
            "Streamlit Version": st.__version__,
            "Session State Keys": list(st.session_state.keys()),
            "Python Environment": "Streamlit Cloud",
            "Memory Usage": "Normal",
            "Load Time": f"{time.time() - st.session_state.start_time:.2f}s",
            "Cache Status": "Ativo"
        }
        
        st.json(debug_info)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; margin-top: 2rem;">
    🧠 <strong>CertMind V2</strong> • Sistema de Estudos para Certificações IT • 
    Desenvolvido para otimizar seu aprendizado
</div>
""", unsafe_allow_html=True)
