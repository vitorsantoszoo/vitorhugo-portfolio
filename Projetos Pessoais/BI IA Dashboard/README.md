# 📁 Estrutura Completa do Projeto

BI IA Dashboard/
│
├── notebooks/
│   └── bi_dashboard_pipeline.ipynb        # Notebook principal (orquestrador)
│
├── src/
│   ├── load_data.py                       # Módulo de leitura e inferência de colunas
│   ├── preprocessing.py                   # Tratamento e limpeza de dados
│   ├── metrics.py                         # Cálculo de KPIs e agregações
│   ├── forecasting.py                     # IA para previsões (RF / Prophet)
│   ├── visualization.py                   # Gráficos interativos (Plotly)
│   └── nlg_agent.py                       # Geração automática de relatórios (NLG)
│
├── data/
│   ├── examples/
│   │   └── sample_sales.csv               # Dataset de exemplo usado no projeto
│   └── user_uploads/                      # (opcional) onde o usuário pode salvar dados
│
├── dashboard/
│   ├── exports/                           # Saída final: HTML, PDF, gráficos
│   └── reports/                           # Relatórios automáticos gerados
│
└── README.md                              # Documentação principal
