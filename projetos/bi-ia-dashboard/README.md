# 🧠 BI IA Dashboard — Inteligência Analítica com Python

Mini-sistema de Business Intelligence que lê um dataset de vendas/faturamento, limpa e processa os dados, gera visualizações estilo BI e produz previsões futuras com intervalo de confiança — tudo em Python, executável no Google Colab.

---

## 🎯 Objetivo

Demonstrar um pipeline completo de Inteligência Analítica:

- ETL (extração, transformação e limpeza automática dos dados)
- Visualizações exploratórias e estratégicas (estilo Power BI)
- Previsão com Random Forest + intervalo de confiança via bootstrap
- Geração automática de relatório em linguagem natural (NLG)
- Suporte para o usuário substituir o dataset e gerar seu próprio dashboard

---

## 🧠 Como funciona

O notebook `notebooks/bi_dashboard_pipeline.ipynb` orquestra os módulos de `src/`:

```
load_data.py        → identifica automaticamente coluna de datas, coluna de valores e formatação
preprocessing.py     → limpeza de valores ausentes, padronização de datas, ordenação temporal
metrics.py           → KPIs, variações percentuais, médias móveis, sazonalidade básica
forecasting.py       → RandomForestRegressor + lags, intervalo de confiança via bootstrap (90%)
visualization.py     → gráficos interativos (Plotly): série temporal, barras, tendência
nlg_agent.py         → relatório automático em texto a partir dos resultados
```

Para usar seus próprios dados, salve o arquivo em `data/user_uploads/`, selecione-o na célula de configuração do notebook e rode tudo novamente — não é necessário alterar código.

---

## 🛠️ Tecnologias

Python 3.10+ • Pandas • NumPy • Scikit-learn (RandomForestRegressor) • Plotly • Google Colab

Lista completa em [`requirements.txt`](./requirements.txt).

---

## 📂 Estrutura

```
bi-ia-dashboard/
├── notebooks/
│   └── bi_dashboard_pipeline.ipynb   # Notebook principal (orquestrador)
├── src/
│   ├── load_data.py
│   ├── preprocessing.py
│   ├── metrics.py
│   ├── forecasting.py
│   ├── visualization.py
│   └── nlg_agent.py
├── data/
│   ├── examples/sample_sales.csv     # Dataset de exemplo
│   └── user_uploads/                 # Onde o usuário coloca seus próprios dados
├── dashboard/
│   └── exports/                      # Saída gerada: HTML, CSV, relatório NLG
└── requirements.txt
```

---

## 🚀 Como executar

```bash
git clone https://github.com/vitorsantoszoo/vitorhugo-portfolio.git
cd vitorhugo-portfolio/projetos/bi-ia-dashboard
pip install -r requirements.txt
```

Abra `notebooks/bi_dashboard_pipeline.ipynb` (Colab ou Jupyter local) e execute todas as células. Por padrão ele usa `data/examples/sample_sales.csv`; para usar outro dataset, salve-o em `data/user_uploads/` e aponte o notebook para ele.

---

## 📈 Resultados / Status

✅ Pipeline completo funcional: ETL → métricas → previsão → visualização → relatório NLG  
✅ Exportações (HTML, CSV, relatório de texto) salvas em `dashboard/exports/`  
✅ Previsão com Random Forest + intervalo de confiança de 90% via bootstrap (80 simulações)

---

## 🌱 Próximos passos

- Exportar dashboard consolidado em um único HTML
- Adicionar comparação Forecast vs. Meta
- Heatmap de sazonalidade

---

## 📫 Contato

📧 **Email:** vitoor.hugoo@hotmail.com  
🔗 **LinkedIn:** [linkedin.com/in/vitor-hugo-3861391b8](https://www.linkedin.com/in/vitor-hugo-3861391b8/)  
💻 **GitHub:** [github.com/vitorsantoszoo](https://github.com/vitorsantoszoo)
