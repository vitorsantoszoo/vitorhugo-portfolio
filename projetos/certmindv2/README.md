# 🧠 CertMind V2 — Assistente Inteligente para Certificação CompTIA A+

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)

---

## 🎯 Objetivo

Assistente interativo de estudos para a certificação **CompTIA A+**, com quiz inteligente, acompanhamento de progresso e repetição espaçada para otimizar a memorização.

- Cobrir os principais subdomínios da certificação
- Dar feedback imediato e pontuação por dificuldade
- Acompanhar desempenho ao longo do tempo (analytics, metas, sequência de estudo)

---

## ⭐ Funcionalidades principais

- **Quiz interativo** — questões aleatórias, feedback imediato com explicações, pontuação por dificuldade (Fácil/Médio/Difícil)
- **Dashboard e analytics** — métricas de desempenho, progresso por categoria, sequência de dias de estudo
- **Progresso** — metas diárias/semanais, evolução temporal, exportação de dados
- **Configurações** — metas personalizadas e gerenciamento de dados

### Subdomínios CompTIA A+ cobertos

| Categoria | Questões |
|-----------|----------|
| 💻 Hardware | 10 |
| 🌐 Redes | 5 |
| 💿 Sistemas Operacionais | 5 |
| 🔒 Segurança | 5 |
| 🔧 Troubleshooting | 5 |
| ☁️ Tecnologias Avançadas | 5 |
| 👥 Procedimentos Profissionais | 5 |

---

## 🛠️ Tecnologias

Streamlit • Python 3.13 • HTML/CSS/JS (estilização customizada) • Session State (gerenciamento de progresso local)

---

## 📂 Estrutura

```
vitorhugo-portfolio/
└── projetos/certmindv2/
    ├── app_v2_final.py       # Aplicação principal
    ├── README.md
    ├── QUICK_START.md        # Guia de início rápido
    ├── requirements.txt
    ├── data/                 # Banco de questões e progresso
    ├── modules/              # Analytics, progresso, repetição espaçada
    └── utils/                # Utilitários (migração de dados)
```

---

## 🚀 Como executar

```bash
git clone https://github.com/vitorsantoszoo/vitorhugo-portfolio.git
cd vitorhugo-portfolio/projetos/certmindv2
pip install -r requirements.txt
streamlit run app_v2_final.py
# acesse http://localhost:8501
```

---

## 📈 Status

Versão beta funcional: quiz, analytics, dashboard e configurações implementados; banco de questões (40+) em expansão contínua.

---

## 🌱 Próximos passos

- Ampliar o banco de questões
- Sistema de repetição espaçada (SM-2)
- Suporte a outras certificações (Network+, Security+)

---

## 📫 Contato

📧 **Email:** vitoor.hugoo@hotmail.com  
🔗 **LinkedIn:** [linkedin.com/in/vitor-hugo-3861391b8](https://www.linkedin.com/in/vitor-hugo-3861391b8/)  
💻 **GitHub:** [github.com/vitorsantoszoo](https://github.com/vitorsantoszoo)
