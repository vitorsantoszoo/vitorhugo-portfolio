import streamlit as st
import random
import json
from datetime import datetime, timedelta

# Configuração da página
st.set_page_config(
    page_title="CertMind V2 - Assistente CompTIA A+",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ===============================
# BANCO DE QUESTÕES EXPANDIDO
# ===============================

QUESTIONS_DATA = {
    1: {
        "category": "Hardware",
        "subdomain": "Dispositivos de Entrada/Saída",
        "question": "Qual dispositivo de entrada permite ao usuário interagir com o computador usando toque na tela?",
        "options": ["A) Mouse óptico", "B) Teclado mecânico", "C) Touchscreen", "D) Scanner de código de barras"],
        "correct": 2,
        "difficulty": "easy",
        "explanation": "Touchscreen permite interação através do toque direto na tela, sendo um dispositivo híbrido de entrada e saída."
    },
    2: {
        "category": "Hardware", 
        "subdomain": "Dispositivos de Entrada/Saída",
        "question": "Qual tipo de conector USB oferece a maior velocidade de transferência de dados?",
        "options": ["A) USB 2.0", "B) USB 3.0", "C) USB-C", "D) USB 1.1"],
        "correct": 2,
        "difficulty": "medium",
        "explanation": "USB-C suporta velocidades de até 10 Gbps (USB 3.1), sendo superior aos padrões anteriores."
    },
    3: {
        "category": "Hardware",
        "subdomain": "Dispositivos de Entrada/Saída", 
        "question": "Qual resolução de vídeo é considerada Full HD?",
        "options": ["A) 1920x1080", "B) 1366x768", "C) 2560x1440", "D) 1024x768"],
        "correct": 0,
        "difficulty": "easy",
        "explanation": "1920x1080 pixels é o padrão de resolução Full HD (1080p) amplamente usado em monitores e TVs."
    },
    4: {
        "category": "Hardware",
        "subdomain": "Dispositivos de Entrada/Saída",
        "question": "Qual periférico é essencial para digitalizar documentos físicos?",
        "options": ["A) Webcam", "B) Plotter", "C) Scanner", "D) Impressora matricial"],
        "correct": 2,
        "difficulty": "easy",
        "explanation": "Scanner é o dispositivo específico para converter documentos físicos em formato digital."
    },
    5: {
        "category": "Hardware",
        "subdomain": "Dispositivos de Entrada/Saída",
        "question": "Qual tecnologia de monitor oferece melhores ângulos de visão e cores mais precisas?",
        "options": ["A) TN (Twisted Nematic)", "B) IPS (In-Plane Switching)", "C) VA (Vertical Alignment)", "D) CRT"],
        "correct": 1,
        "difficulty": "medium",
        "explanation": "Monitores IPS oferecem ângulos de visão de até 178° e melhor reprodução de cores comparado aos painéis TN."
    },
    
    # Redes e Conectividade
    6: {
        "category": "Redes",
        "subdomain": "Conectividade de Rede",
        "question": "Qual protocolo é usado para converter nomes de domínio em endereços IP?",
        "options": ["A) HTTP", "B) FTP", "C) DNS", "D) SMTP"],
        "correct": 2,
        "difficulty": "easy",
        "explanation": "DNS (Domain Name System) traduz nomes de domínio legíveis (como google.com) em endereços IP."
    },
    7: {
        "category": "Redes",
        "subdomain": "Conectividade de Rede", 
        "question": "Qual cabo de rede suporta velocidades de até 1 Gbps e distância máxima de 100 metros?",
        "options": ["A) Cat 5e", "B) Cat 6", "C) Cat 6A", "D) Cat 7"],
        "correct": 1,
        "difficulty": "medium",
        "explanation": "Cat 6 suporta até 1 Gbps em até 100 metros de distância, sendo padrão para redes gigabit."
    },
    8: {
        "category": "Redes",
        "subdomain": "Conectividade de Rede",
        "question": "Qual protocolo é usado para enviar emails?",
        "options": ["A) POP3", "B) IMAP", "C) SMTP", "D) DNS"],
        "correct": 2,
        "difficulty": "easy",
        "explanation": "SMTP (Simple Mail Transfer Protocol) é usado especificamente para envio de emails."
    },
    9: {
        "category": "Redes",
        "subdomain": "Conectividade de Rede",
        "question": "Qual máscara de sub-rede é usada em uma rede Classe C padrão?",
        "options": ["A) 255.0.0.0", "B) 255.255.0.0", "C) 255.255.255.0", "D) 255.255.255.255"],
        "correct": 2,
        "difficulty": "medium",
        "explanation": "Máscara 255.255.255.0 é padrão para redes Classe C, permitindo 254 hosts por rede."
    },
    10: {
        "category": "Redes",
        "subdomain": "Conectividade de Rede",
        "question": "Qual frequência opera o Wi-Fi 6 (802.11ax)?",
        "options": ["A) 2.4 GHz apenas", "B) 5 GHz apenas", "C) 2.4 GHz e 5 GHz", "D) 6 GHz apenas"],
        "correct": 2,
        "difficulty": "medium",
        "explanation": "Wi-Fi 6 opera nas frequências de 2.4 GHz e 5 GHz, oferecendo melhor performance em ambientes congestionados."
    },

    # Sistemas Operacionais
    11: {
        "category": "Sistemas Operacionais",
        "subdomain": "Windows",
        "question": "Qual comando do Windows CMD verifica a conectividade de rede?",
        "options": ["A) dir", "B) ping", "C) ls", "D) whoami"],
        "correct": 1,
        "difficulty": "easy",
        "explanation": "ping é usado para testar a conectividade entre dispositivos enviando pacotes ICMP."
    },
    12: {
        "category": "Sistemas Operacionais",
        "subdomain": "Windows",
        "question": "Qual atalho de teclado abre o Gerenciador de Tarefas no Windows?",
        "options": ["A) Ctrl + Alt + Del", "B) Ctrl + Shift + Esc", "C) Alt + Tab", "D) Win + R"],
        "correct": 1,
        "difficulty": "easy",
        "explanation": "Ctrl + Shift + Esc abre diretamente o Gerenciador de Tarefas no Windows."
    },
    13: {
        "category": "Sistemas Operacionais",
        "subdomain": "Windows",
        "question": "Qual arquivo de sistema do Windows contém informações de configuração do sistema?",
        "options": ["A) autoexec.bat", "B) config.sys", "C) registry", "D) win.ini"],
        "correct": 2,
        "difficulty": "medium",
        "explanation": "Registry é o banco de dados central que armazena configurações do sistema Windows."
    },
    14: {
        "category": "Sistemas Operacionais",
        "subdomain": "Windows",
        "question": "Qual ferramenta do Windows permite gerenciar partições do disco rígido?",
        "options": ["A) Defrag", "B) Disk Cleanup", "C) Disk Management", "D) System Restore"],
        "correct": 2,
        "difficulty": "medium",
        "explanation": "Disk Management (Gerenciamento de Disco) permite criar, redimensionar e gerenciar partições."
    },
    15: {
        "category": "Sistemas Operacionais",
        "subdomain": "Linux",
        "question": "Qual comando Linux lista arquivos em um diretório?",
        "options": ["A) cd", "B) ls", "C) cat", "D) mkdir"],
        "correct": 1,
        "difficulty": "easy",
        "explanation": "ls (list) é o comando básico para listar conteúdo de diretórios no Linux."
    },

    # Segurança
    16: {
        "category": "Segurança",
        "subdomain": "Proteção de Dados",
        "question": "Qual é o método mais eficaz para proteger dados sensíveis em trânsito?",
        "options": ["A) Hash", "B) Criptografia", "C) Backup", "D) Firewall"],
        "correct": 1,
        "difficulty": "medium",
        "explanation": "Criptografia protege dados convertendo-os em formato ilegível durante transmissão."
    },
    17: {
        "category": "Segurança",
        "subdomain": "Proteção de Dados",
        "question": "O que é um ataque de engenharia social?",
        "options": ["A) Exploração de vulnerabilidades de software", "B) Manipulação psicológica para obter informações", "C) Ataque de força bruta", "D) Injeção de código SQL"],
        "correct": 1,
        "difficulty": "easy",
        "explanation": "Engenharia social manipula pessoas para obter acesso ou informações, explorando confiança."
    },
    18: {
        "category": "Segurança",
        "subdomain": "Proteção de Dados",
        "question": "Qual tipo de malware se propaga automaticamente entre sistemas?",
        "options": ["A) Trojan", "B) Worm", "C) Virus", "D) Spyware"],
        "correct": 1,
        "difficulty": "medium",
        "explanation": "Worms são malware auto-replicantes que se espalham automaticamente através de redes."
    },
    19: {
        "category": "Segurança",
        "subdomain": "Proteção de Dados",
        "question": "O que é autenticação de dois fatores (2FA)?",
        "options": ["A) Senha e PIN", "B) Senha e impressão digital", "C) Duas formas de verificação independentes", "D) Senha criptografada"],
        "correct": 2,
        "difficulty": "easy",
        "explanation": "2FA requer duas formas independentes de verificação para acessar um sistema."
    },
    20: {
        "category": "Segurança",
        "subdomain": "Proteção de Dados",
        "question": "Qual protocolo é usado para conexões web seguras (https)?",
        "options": ["A) SSL/TLS", "B) SSH", "C) FTP", "D) Telnet"],
        "correct": 0,
        "difficulty": "medium",
        "explanation": "SSL/TLS é o protocolo que fornece criptografia para conexões HTTPS seguras."
    },

    # Troubleshooting
    21: {
        "category": "Troubleshooting",
        "subdomain": "Diagnóstico",
        "question": "Qual é o primeiro passo no processo de troubleshooting?",
        "options": ["A) Identificar o problema", "B) Testar a solução", "C) Documentar o problema", "D) Estabelecer uma teoria"],
        "correct": 0,
        "difficulty": "medium",
        "explanation": "O primeiro passo sempre é identificar claramente qual é o problema antes de buscar soluções."
    },
    22: {
        "category": "Troubleshooting",
        "subdomain": "Diagnóstico",
        "question": "Qual ferramenta do Windows ajuda a diagnosticar problemas de memória?",
        "options": ["A) msconfig", "B) msinfo32", "C) Windows Memory Diagnostic", "D) chkdsk"],
        "correct": 2,
        "difficulty": "medium",
        "explanation": "Windows Memory Diagnostic testa a memória RAM para identificar problemas de hardware."
    },
    23: {
        "category": "Troubleshooting",
        "subdomain": "Diagnóstico",
        "question": "O que pode causar a 'tela azul da morte' (BSOD)?",
        "options": ["A) Superheating", "B) Falhas de driver ou hardware", "C) Software antivírus", "D) Conexão de internet lenta"],
        "correct": 1,
        "difficulty": "easy",
        "explanation": "BSOD geralmente indica falhas críticas de driver ou problemas de hardware incompatível."
    },
    24: {
        "category": "Troubleshooting",
        "subdomain": "Diagnóstico",
        "question": "Qual comando verifica a integridade dos arquivos do sistema Windows?",
        "options": ["A) sfc /scannow", "B) chkdsk /f", "C) ipconfig /flushdns", "D) netstat"],
        "correct": 0,
        "difficulty": "medium",
        "explanation": "sfc /scannow verifica e repara arquivos de sistema corrompidos no Windows."
    },
    25: {
        "category": "Troubleshooting",
        "subdomain": "Diagnóstico",
        "question": "Qual ferramenta monitora recursos do sistema em tempo real?",
        "options": ["A) Event Viewer", "B) Task Manager", "C) System Configuration", "D) Performance Monitor"],
        "correct": 1,
        "difficulty": "easy",
        "explanation": "Task Manager mostra uso de CPU, memória, disco e rede em tempo real."
    },

    # Hardware Avançado
    26: {
        "category": "Hardware",
        "subdomain": "Componentes Internos",
        "question": "Qual componente é responsável por executar instruções do programa?",
        "options": ["A) RAM", "B) HD", "C) CPU", "D) Placa-mãe"],
        "correct": 2,
        "difficulty": "easy",
        "explanation": "CPU (Unidade Central de Processamento) é o 'cérebro' que executa todas as instruções."
    },
    27: {
        "category": "Hardware",
        "subdomain": "Componentes Internos",
        "question": "Qual tipo de memória é volátil e mais rápida que o HD?",
        "options": ["A) ROM", "B) RAM", "C) SSD", "D) Cache"],
        "correct": 1,
        "difficulty": "easy",
        "explanation": "RAM (Random Access Memory) é volátil (perde dados sem energia) e muito mais rápida que armazenamento."
    },
    28: {
        "category": "Hardware",
        "subdomain": "Componentes Internos",
        "question": "Qual interface de armazenamento é mais rápida: SATA III ou NVMe?",
        "options": ["A) SATA III", "B) NVMe", "C) Ambas iguais", "D) Depende do HD"],
        "correct": 1,
        "difficulty": "medium",
        "explanation": "NVMe usa interface PCIe e pode atingir velocidades até 10x superiores ao SATA III."
    },
    29: {
        "category": "Hardware",
        "subdomain": "Componentes Internos",
        "question": "Qual componente protege contra picos de energia?",
        "options": ["A) Regulador de tensão", "B) No-break", "C) Fusível", "D) Todas as anteriores"],
        "correct": 3,
        "difficulty": "medium",
        "explanation": "No-break, reguladores e fusíveis oferecem diferentes níveis de proteção contra picos de energia."
    },
    30: {
        "category": "Hardware",
        "subdomain": "Componentes Internos",
        "question": "Qual é a função do BIOS/UEFI?",
        "options": ["A) Gerenciar arquivos", "B) Interface entre hardware e sistema operacional", "C) Processar gráficos", "D) Conectar à internet"],
        "correct": 1,
        "difficulty": "medium",
        "explanation": "BIOS/UEFI é o firmware que inicializa o hardware e fornece interface para o sistema operacional."
    },

    # Virtualização e Nuvem
    31: {
        "category": "Tecnologias Avançadas",
        "subdomain": "Virtualização",
        "question": "O que é virtualização?",
        "options": ["A) Executar múltiplos sistemas operacionais em um hardware", "B) Aumentar a velocidade do processador", "C) Expandir a memória RAM", "D) Instalar mais discos rígidos"],
        "correct": 0,
        "difficulty": "easy",
        "explanation": "Virtualização permite executar múltiplos sistemas operacionais isolados no mesmo hardware físico."
    },
    32: {
        "category": "Tecnologias Avançadas",
        "subdomain": "Virtualização",
        "question": "Qual é a vantagem principal de usar máquinas virtuais?",
        "options": ["A) Menor consumo de energia", "B) Isolamento e portabilidade", "C) Melhor qualidade gráfica", "D) Conexão mais rápida"],
        "correct": 1,
        "difficulty": "medium",
        "explanation": "VMs oferecem isolamento completo e podem ser facilmente movidas entre diferentes hosts físicos."
    },
    33: {
        "category": "Tecnologias Avançadas",
        "subdomain": "Nuvem",
        "question": "O que significa 'Infrastructure as a Service' (IaaS)?",
        "options": ["A) Software como serviço", "B) Infraestrutura como serviço", "C) Plataforma como serviço", "D) Backup como serviço"],
        "correct": 1,
        "difficulty": "medium",
        "explanation": "IaaS fornece recursos de infraestrutura virtualizados (servidores, storage, rede) via nuvem."
    },
    34: {
        "category": "Tecnologias Avançadas",
        "subdomain": "Nuvem",
        "question": "Qual é uma vantagem da computação em nuvem?",
        "options": ["A) Requer hardware local constante", "B) Escalabilidade e acesso remoto", "C) Funciona apenas offline", "D) Mais caro que infraestrutura local"],
        "correct": 1,
        "difficulty": "easy",
        "explanation": "Nuvem oferece escalabilidade under demande e acesso aos recursos de qualquer lugar com internet."
    },
    35: {
        "category": "Tecnologias Avançadas",
        "subdomain": "Sistemas Operacionais Móveis",
        "question": "Qual sistema operacional móvel é baseado no kernel Linux?",
        "options": ["A) iOS", "B) Android", "C) Windows Phone", "D) BlackBerry OS"],
        "correct": 1,
        "difficulty": "easy",
        "explanation": "Android é baseado no kernel Linux e é o sistema móvel mais usado mundialmente."
    },

    # Procedimentos Profissionais
    36: {
        "category": "Procedimentos Profissionais",
        "subdomain": "Comunicação",
        "question": "Qual é a primeira regra na comunicação com clientes durante suporte técnico?",
        "options": ["A) Usar jargão técnico", "B) Escutar ativamente e ser empático", "C) Resolver rapidamente sem explicar", "D) Evitar contato visual"],
        "correct": 1,
        "difficulty": "easy",
        "explanation": "Escutar ativamente e demonstrar empatia são fundamentais para entender o problema do cliente."
    },
    37: {
        "category": "Procedimentos Profissionais",
        "subdomain": "Documentação",
        "question": "Por que é importante documentar soluções de problemas?",
        "options": ["A) Para ocupar espaço", "B) Para referência futura e treinamento", "C) Para impressionar o chefe", "D) Não é necessário"],
        "correct": 1,
        "difficulty": "easy",
        "explanation": "Documentação permite reuso de soluções e serve como base de conhecimento para a equipe."
    },
    38: {
        "category": "Procedimentos Profissionais",
        "subdomain": "Segurança",
        "question": "Qual medida de segurança é essencial ao trabalhar com dados de clientes?",
        "options": ["A) Compartilhar com colegas", "B) Manter confidencialidade", "C) Salvar em pendrive pessoal", "D) Imprimir em papel"],
        "correct": 1,
        "difficulty": "easy",
        "explanation": "Confidencialidade é fundamental ao lidar com dados sensíveis de clientes."
    },
    39: {
        "category": "Procedimentos Profissionais",
        "subdomain": "Planejamento",
        "question": "Qual é o benefício de manter um inventário atualizado de hardware?",
        "options": ["A) Ocupar menos espaço", "B) Facilitar manutenção e upgrades", "C) Impressionar visitantes", "D) Vender mais equipamentos"],
        "correct": 1,
        "difficulty": "medium",
        "explanation": "Inventário atualizado facilita planejamento de manutenção, upgrades e substituição de equipamentos."
    },
    40: {
        "category": "Procedimentos Profissionais",
        "subdomain": "Ética",
        "question": "O que fazer se você descobrir uma vulnerabilidade de segurança em um sistema cliente?",
        "options": ["A) Ignorar para não gerar custos", "B) Reportar imediatamente ao responsável", "C) Compartilhar com outros técnicos", "D) Explorar para testes pessoais"],
        "correct": 1,
        "difficulty": "easy",
        "explanation": "Vulnerabilidades devem ser reportadas imediatamente para proteção dos dados do cliente."
    }
}

# ===============================
# FUNÇÕES DE INICIALIZAÇÃO
# ===============================

def initialize_session_state():
    """Inicializa o estado da sessão com valores zerados"""
    if 'user_data' not in st.session_state:
        st.session_state.user_data = {
            'quiz_data': {
                'current_question': 0,
                'score': 0,
                'total_questions': 0,
                'answered_questions': [],
                'categories_answered': {},
                'correct_answers': 0,
                'wrong_answers': 0
            },
            'progress_data': {
                'category_progress': {},
                'weekly_goal': 50,
                'questions_this_week': 0,
                'study_streak': 0,
                'last_study_date': None,
                'achievements': []
            },
            'settings': {
                'theme': 'light',
                'notifications': True,
                'daily_goal': 10
            }
        }
    
    # Garantir que não há dados pré-carregados
    if 'quiz_started' not in st.session_state:
        st.session_state.quiz_started = False
    if 'current_question_data' not in st.session_state:
        st.session_state.current_question_data = None

def get_random_questions(count=10):
    """Retorna questões aleatórias do banco"""
    question_ids = list(QUESTIONS_DATA.keys())
    selected_ids = random.sample(question_ids, min(count, len(question_ids)))
    return {qid: QUESTIONS_DATA[qid] for qid in selected_ids}

def calculate_difficulty(difficulty):
    """Calcula pontuação baseada na dificuldade"""
    points = {'easy': 1, 'medium': 2, 'hard': 3}
    return points.get(difficulty, 1)

# ===============================
# COMPONENTES DE INTERFACE
# ===============================

def display_header():
    """Cabeçalho principal do aplicativo"""
    st.markdown("""
    <div style="background: linear-gradient(90deg, #667eea 0%, #764ba2 100%); 
                padding: 1rem; border-radius: 10px; margin-bottom: 2rem; color: white;">
        <h1 style="margin: 0; text-align: center;">🧠 CertMind V2</h1>
        <p style="margin: 0; text-align: center; font-size: 1.1em;">
            Assistente Inteligente para Certificação CompTIA A+
        </p>
    </div>
    """, unsafe_allow_html=True)

def display_dashboard():
    """Dashboard principal com métricas"""
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="📊 Questões Respondidas", 
            value=st.session_state.user_data['quiz_data']['total_questions'],
            delta=None
        )
    
    with col2:
        correct = st.session_state.user_data['quiz_data']['correct_answers']
        total = st.session_state.user_data['quiz_data']['total_questions']
        accuracy = (correct / total * 100) if total > 0 else 0
        st.metric(
            label="🎯 Precisão", 
            value=f"{accuracy:.1f}%",
            delta=f"{correct}/{total}"
        )
    
    with col3:
        st.metric(
            label="🔥 Sequência de Dias", 
            value=st.session_state.user_data['progress_data']['study_streak'],
            delta="dias consecutivos"
        )
    
    with col4:
        weekly = st.session_state.user_data['progress_data']['questions_this_week']
        goal = st.session_state.user_data['progress_data']['weekly_goal']
        progress_percent = (weekly / goal * 100) if goal > 0 else 0
        st.metric(
            label="📈 Meta Semanal", 
            value=f"{weekly}/{goal}",
            delta=f"{progress_percent:.0f}%"
        )

def display_progress_charts():
    """Gráficos de progresso"""
    st.subheader("📊 Visualização de Progresso")
    
    # Gráfico de progresso por categoria
    categories_data = st.session_state.user_data['quiz_data']['categories_answered']
    if categories_data:
        category_names = list(categories_data.keys())
        category_counts = list(categories_data.values())
        
        if category_names:
            st.bar_chart({
                'Questões por Categoria': dict(zip(category_names, category_counts))
            })
    
    # Gráfico de precisão por categoria
    st.subheader("🎯 Precisão por Categoria")
    col1, col2 = st.columns(2)
    
    with col1:
        # Distribuição de respostas
        correct = st.session_state.user_data['quiz_data']['correct_answers']
        wrong = st.session_state.user_data['quiz_data']['wrong_answers']
        
        if correct + wrong > 0:
            # Usar métricas em vez de pie chart para evitar erros
            col_a, col_b = st.columns(2)
            with col_a:
                st.metric("✅ Corretas", correct, f"{correct/(correct+wrong)*100:.1f}%")
            with col_b:
                st.metric("❌ Incorretas", wrong, f"{wrong/(correct+wrong)*100:.1f}%")
        else:
            st.info("📝 Complete um quiz para ver a distribuição de respostas")
    
    with col2:
        # Progresso semanal
        weekly_data = {
            'Meta': st.session_state.user_data['progress_data']['weekly_goal'],
            'Atual': st.session_state.user_data['progress_data']['questions_this_week']
        }
        st.bar_chart(weekly_data)

def display_quiz_interface():
    """Interface principal do quiz"""
    st.subheader("🎯 Quiz Interativo")
    
    # Botão para iniciar quiz
    if not st.session_state.quiz_started:
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🚀 Iniciar Nova Sessão de Quiz", type="primary", use_container_width=True):
                start_new_quiz_session()
        return
    
    # Se já está no quiz, mostra a questão atual
    if st.session_state.current_question_data:
        display_current_question()
    
    # Botões de controle
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        if st.button("📊 Ver Resultados Parciais", type="secondary", use_container_width=True):
            display_partial_results()

def start_new_quiz_session():
    """Inicia uma nova sessão de quiz"""
    st.session_state.quiz_data = get_random_questions(10)
    st.session_state.question_ids = list(st.session_state.quiz_data.keys())
    st.session_state.current_question_index = 0
    st.session_state.quiz_started = True
    st.session_state.answered_current = False
    
    # Reset dados da sessão
    st.session_state.user_data['quiz_data']['current_question'] = 0
    st.session_state.user_data['quiz_data']['total_questions'] = 0
    st.session_state.user_data['quiz_data']['answered_questions'] = []
    st.session_state.user_data['quiz_data']['categories_answered'] = {}
    st.session_state.user_data['quiz_data']['correct_answers'] = 0
    st.session_state.user_data['quiz_data']['wrong_answers'] = 0
    
    display_current_question()

def display_current_question():
    """Exibe a questão atual"""
    if st.session_state.current_question_index >= len(st.session_state.question_ids):
        display_quiz_completed()
        return
    
    current_id = st.session_state.question_ids[st.session_state.current_question_index]
    question_data = st.session_state.quiz_data[current_id]
    st.session_state.current_question_data = question_data
    
    # Cabeçalho da questão
    progress = (st.session_state.current_question_index + 1) / len(st.session_state.question_ids)
    st.progress(progress)
    
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown(f"**Questão {st.session_state.current_question_index + 1} de {len(st.session_state.question_ids)}**")
    with col2:
        difficulty_colors = {"easy": "🟢", "medium": "🟡", "hard": "🔴"}
        st.markdown(f"{difficulty_colors.get(question_data['difficulty'], '⚪')} {question_data['difficulty'].title()}")
    
    st.markdown("---")
    
    # Exibe a questão
    st.markdown(f"**📚 Categoria:** {question_data['category']}")
    st.markdown(f"**🎯 Subdomínio:** {question_data['subdomain']}")
    st.markdown(f"**❓ {question_data['question']}**")
    
    st.markdown("---")
    
    # Opções de resposta
    st.markdown("**Escolha sua resposta:**")
    
    # Inicializa estado da resposta atual
    if 'selected_answer' not in st.session_state:
        st.session_state.selected_answer = None
    
    # Radio buttons para as opções
    answer_options = [f"{option}" for option in question_data['options']]
    selected_index = st.radio(
        "Selecione uma opção:",
        options=range(len(answer_options)),
        format_func=lambda x: answer_options[x],
        key=f"question_{current_id}"
    )
    
    # Botões de ação
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        # Botão para confirmar resposta (corrigido)
        if st.button("✅ Confirmar Resposta", type="primary", use_container_width=True):
            if selected_index is not None:
                check_answer(selected_index)
            else:
                st.warning("Por favor, selecione uma resposta antes de confirmar!")
    
    # Botão para próxima questão (aparece apenas após responder)
    if st.session_state.user_data['quiz_data']['current_question'] > st.session_state.current_question_index:
        if st.button("➡️ Próxima Questão", type="secondary", use_container_width=True):
            st.session_state.current_question_index += 1
            st.session_state.selected_answer = None
            st.rerun()

def check_answer(selected_index):
    """Verifica se a resposta está correta"""
    current_id = st.session_state.question_ids[st.session_state.current_question_index]
    question_data = st.session_state.quiz_data[current_id]
    correct_answer = question_data['correct']
    
    # Atualiza estatísticas
    st.session_state.user_data['quiz_data']['current_question'] = st.session_state.current_question_index + 1
    st.session_state.user_data['quiz_data']['total_questions'] += 1
    st.session_state.user_data['quiz_data']['answered_questions'].append(current_id)
    
    # Atualiza progresso por categoria
    category = question_data['category']
    if category not in st.session_state.user_data['quiz_data']['categories_answered']:
        st.session_state.user_data['quiz_data']['categories_answered'][category] = 0
    st.session_state.user_data['quiz_data']['categories_answered'][category] += 1
    
    # Verifica se está correta
    is_correct = (selected_index == correct_answer)
    
    if is_correct:
        st.session_state.user_data['quiz_data']['correct_answers'] += 1
        points = calculate_difficulty(question_data['difficulty'])
        st.session_state.user_data['quiz_data']['score'] += points
        
        st.success(f"✅ **Correto!** +{points} pontos")
    else:
        st.session_state.user_data['quiz_data']['wrong_answers'] += 1
        st.error(f"❌ **Incorreto!** A resposta correta era: {question_data['options'][correct_answer]}")
    
    # Mostra explicação
    with st.expander("📖 Ver Explicação"):
        st.write(question_data['explanation'])
    
    # Atualiza sequência de estudo
    today = datetime.now().date()
    last_study = st.session_state.user_data['progress_data']['last_study_date']
    
    if last_study:
        if (today - last_study).days == 1:
            st.session_state.user_data['progress_data']['study_streak'] += 1
        elif (today - last_study).days > 1:
            st.session_state.user_data['progress_data']['study_streak'] = 1
    
    st.session_state.user_data['progress_data']['last_study_date'] = today
    st.session_state.user_data['progress_data']['questions_this_week'] += 1

def display_quiz_completed():
    """Exibe os resultados finais do quiz"""
    st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                padding: 2rem; border-radius: 15px; margin: 2rem 0; text-align: center; color: white;">
        <h2>🎉 Quiz Concluído!</h2>
        <h3>Parabéns por completar a sessão!</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Estatísticas finais
    total = st.session_state.user_data['quiz_data']['total_questions']
    correct = st.session_state.user_data['quiz_data']['correct_answers']
    score = st.session_state.user_data['quiz_data']['score']
    accuracy = (correct / total * 100) if total > 0 else 0
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("🎯 Precisão Final", f"{accuracy:.1f}%", f"{correct}/{total}")
    
    with col2:
        st.metric("🏆 Pontuação Total", score, "pontos")
    
    with col3:
        performance = "Excelente" if accuracy >= 80 else "Bom" if accuracy >= 60 else "Precisa Melhorar"
        st.metric("📊 Performance", performance, "avaliação")
    
    # Botões de ação
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        if st.button("🔄 Novo Quiz", type="primary", use_container_width=True):
            st.session_state.quiz_started = False
            st.rerun()
        
        if st.button("📊 Ver Análise Detalhada", type="secondary", use_container_width=True):
            display_detailed_analysis()

def display_partial_results():
    """Mostra resultados parciais durante o quiz"""
    st.subheader("📊 Resultados Parciais")
    
    current = st.session_state.user_data['quiz_data']['current_question']
    correct = st.session_state.user_data['quiz_data']['correct_answers']
    accuracy = (correct / current * 100) if current > 0 else 0
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("📝 Respondidas", f"{current}/{len(st.session_state.question_ids)}")
    
    with col2:
        st.metric("✅ Corretas", f"{correct}/{current}", f"{accuracy:.1f}%")
    
    with col3:
        st.metric("⭐ Pontos", st.session_state.user_data['quiz_data']['score'])

def display_detailed_analysis():
    """Análise detalhada dos resultados"""
    st.subheader("📈 Análise Detalhada")
    
    # Performance por categoria
    categories_data = st.session_state.user_data['quiz_data']['categories_answered']
    if categories_data:
        st.write("**📊 Desempenho por Categoria:**")
        for category, count in categories_data.items():
            st.write(f"- **{category}**: {count} questões respondidas")
    
    # Recomendações baseadas na performance
    accuracy = (st.session_state.user_data['quiz_data']['correct_answers'] / 
                st.session_state.user_data['quiz_data']['total_questions'] * 100) if st.session_state.user_data['quiz_data']['total_questions'] > 0 else 0
    
    st.write("**💡 Recomendações de Estudo:**")
    if accuracy >= 80:
        st.success("🎯 Excelente desempenho! Continue praticando para manter o nível.")
    elif accuracy >= 60:
        st.info("👍 Bom desempenho! Foque nas categorias com mais erros.")
    else:
        st.warning("📚 Recomende revisar os fundamentos básicos antes de continuar.")

def display_settings():
    """Interface de configurações"""
    st.subheader("⚙️ Configurações")
    
    # Configurações de meta
    st.write("**📈 Metas de Estudo**")
    weekly_goal = st.number_input(
        "Meta de questões por semana:",
        min_value=10,
        max_value=200,
        value=st.session_state.user_data['progress_data']['weekly_goal'],
        step=10
    )
    st.session_state.user_data['progress_data']['weekly_goal'] = weekly_goal
    
    daily_goal = st.number_input(
        "Meta diária de questões:",
        min_value=1,
        max_value=50,
        value=st.session_state.user_data['settings']['daily_goal'],
        step=1
    )
    st.session_state.user_data['settings']['daily_goal'] = daily_goal
    
    # Configurações de notificação
    st.write("**🔔 Notificações**")
    notifications = st.checkbox(
        "Ativar notificações de lembrete",
        value=st.session_state.user_data['settings']['notifications']
    )
    st.session_state.user_data['settings']['notifications'] = notifications
    
    # Reset de dados
    st.write("**🗑️ Gerenciamento de Dados**")
    if st.button("🔄 Resetar Progresso", type="secondary"):
        initialize_session_state()
        st.success("Progresso resetado com sucesso!")
        st.rerun()
    
    if st.button("📊 Exportar Dados", type="secondary"):
        # Criar dados para export
        export_data = {
            'quiz_data': st.session_state.user_data['quiz_data'],
            'progress_data': st.session_state.user_data['progress_data'],
            'export_date': datetime.now().isoformat()
        }
        
        # Download dos dados
        st.download_button(
            label="💾 Baixar Dados de Progresso",
            data=json.dumps(export_data, indent=2, ensure_ascii=False),
            file_name=f"certmind_progress_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
            mime="application/json"
        )

def display_about():
    """Informações sobre o aplicativo"""
    st.subheader("ℹ️ Sobre o CertMind V2")
    
    st.markdown("""
    **🧠 CertMind V2** é um assistente inteligente para estudos da certificação CompTIA A+.
    
    **✨ Características:**
    - 🎯 Quiz interativo com questões aleatórias
    - 📊 Acompanhamento detalhado de progresso
    - 🎨 Interface moderna e intuitiva
    - 📈 Sistema de metas e conquistas
    - 🔄 Repetição espaçada inteligente
    
    **📚 Banco de Questões:**
    - 40+ questões organizadas por subdomínios
    - Explicações detalhadas para cada resposta
    - Dificuldade progressiva (Fácil, Médio, Difícil)
    
    **🎯 Subdomínios Cobertos:**
    - Hardware e Componentes
    - Redes e Conectividade
    - Sistemas Operacionais
    - Segurança da Informação
    - Troubleshooting
    - Tecnologias Avançadas
    - Procedimentos Profissionais
    
    **🏆 Sistema de Pontuação:**
    - Questões Fáciles: 1 ponto
    - Questões Médias: 2 pontos
    - Questões Difíceis: 3 pontos
    
    **Versão:** 2.0 Final
    **Última atualização:** 2025
    """)
    
    # Estatísticas gerais
    st.subheader("📊 Estatísticas do Banco de Questões")
    
    categories = {}
    difficulties = {}
    
    for q_data in QUESTIONS_DATA.values():
        cat = q_data['category']
        diff = q_data['difficulty']
        
        categories[cat] = categories.get(cat, 0) + 1
        difficulties[diff] = difficulties.get(diff, 0) + 1
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Por Categoria:**")
        for cat, count in categories.items():
            st.write(f"- {cat}: {count} questões")
    
    with col2:
        st.write("**Por Dificuldade:**")
        for diff, count in difficulties.items():
            st.write(f"- {diff.title()}: {count} questões")

# ===============================
# PROGRAMA PRINCIPAL
# ===============================

def main():
    """Função principal do aplicativo"""
    # Inicializar estado da sessão
    initialize_session_state()
    
    # Cabeçalho
    display_header()
    
    # Sidebar com navegação
    st.sidebar.title("🧭 Navegação")
    page = st.sidebar.radio(
        "Selecione uma seção:",
        ["🏠 Dashboard", "🎯 Quiz", "📈 Progresso", "⚙️ Configurações", "ℹ️ Sobre"]
    )
    
    # Conteúdo principal baseado na página selecionada
    if page == "🏠 Dashboard":
        display_dashboard()
        display_progress_charts()
        
    elif page == "🎯 Quiz":
        display_quiz_interface()
        
    elif page == "📈 Progresso":
        st.subheader("📈 Análise de Progresso Detalhada")
        display_progress_charts()
        
        # Estatísticas adicionais
        st.subheader("🏆 Conquistas e Metas")
        progress_data = st.session_state.user_data['progress_data']
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric("🔥 Sequência Atual", f"{progress_data['study_streak']} dias", "consecutivos")
        
        with col2:
            weekly = progress_data['questions_this_week']
            goal = progress_data['weekly_goal']
            progress_percent = (weekly / goal * 100) if goal > 0 else 0
            st.metric("📅 Progresso Semanal", f"{weekly}/{goal}", f"{progress_percent:.0f}%")
        
        # Próxima meta
        if progress_data['study_streak'] >= 7:
            st.success("🏆 **Conquista:** Sequência de 7 dias!")
        if progress_percent >= 100:
            st.success("🎯 **Meta Atingida:** Meta semanal completada!")
            
    elif page == "⚙️ Configurações":
        display_settings()
        
    elif page == "ℹ️ Sobre":
        display_about()
    
    # Rodapé
    st.sidebar.markdown("---")
    st.sidebar.markdown("**CertMind V2**  \n🧠 Assistente CompTIA A+")
    st.sidebar.markdown(f"**Questões no banco:** {len(QUESTIONS_DATA)}")

if __name__ == "__main__":
    main()
