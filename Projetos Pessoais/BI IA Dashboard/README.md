# 🧠 BI IA Dashboard — Inteligência Analítica com Python

Este projeto foi desenvolvido para demonstrar um fluxo completo de Análise de Dados + Visualização + Previsões com IA, totalmente implementado em Python e executável no Google Colab.

Ele simula um mini–sistema de Business Intelligence, capaz de:

✔️ Ler um dataset de vendas/faturamento
✔️ Processar e limpar dados automaticamente
✔️ Criar visualizações profissionais (estilo BI)
✔️ Gerar previsões futuras com intervalo de confiança
✔️ Permitir que qualquer usuário substitua o dataset e gere seu próprio dashboard

---

## 📊 Objetivo do Projeto

Criar um pipeline moderno e prático de Inteligência Analítica usando apenas Python, contemplando:

● ETL (extração, transformação e limpeza)

● Visualizações exploratórias e estratégicas

● Modelos de previsão usando Random Forest e lags

● Intervalo de confiança via bootstrap

● Gráficos interativos estilo Power BI

● Pipeline modular organizado em src/

Este projeto serve como:

✔️ Material de estudo
✔️ Demonstração técnica para portfólio
✔️ Base para dashboards corporativos automatizados
✔️ Exemplo de arquitetura simples de Data Analytics com IA

---

# 📁 Estrutura Completa do Projeto
```
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
```

---

## 🛠️ Tecnologias e Bibliotecas Utilizadas

Python 3.10+

● Pandas

● NumPy

● Scikit-learn

● Plotly

● RandomForestRegressor

● Bootstrap Forecasting (Intervalo de Confiança)

● Google Colab

---

## 🚀 Como Executar o Projeto

1️⃣ Substituir o dataset

Coloque seu arquivo .csv em:
```
data/raw/sales_data.csv
```
O notebook reconhece automaticamente as colunas e processa os dados.

---

2️⃣ Abrir o notebook principal

```
/notebooks/bi_dashboard_pipeline.ipynb
```

Clique em “Executar tudo”.

O pipeline irá:

1. Carregar o dataset

2. Realizar limpeza automática

3. Criar gráficos interativos

4. Gerar previsões para os próximos meses

5. Criar gráfico de previsão com intervalo de confiança

---

## 📈 Exemplo de Resultados Produzidos

✔️ Gráfico de série temporal
✔️ Crescimento percentual
✔️ Gráfico de barras dos maiores meses
✔️ Previsão com intervalo de confiança (IC 90%)
✔️ Dashboard interativo via Plotly

---

## 🤖 Previsão com Intervalo de Confiança

O projeto utiliza:

● RandomForestRegressor para previsão

● Lags automáticos

● Bootstrap com 80 simulações

● Faixa de confiança (IC 90%)

● Visualização premium estilo BI

Esse método é muito utilizado em times de Data Analytics para gerar previsões interpretáveis.

---

## 👥 Quem pode usar este projeto?

● Estudantes de IA / Data Science

● Analistas de dados

● Times de BI

● Pequenas e médias empresas

● Pessoas que querem gerar previsões rapidamente

● Usuários que querem transformar seus próprios dados em dashboards reais

---

## 📌 Como substituir o dataset

Basta subir um arquivo com estrutura semelhante:

```
date,sales
2020-01-01,15000
2020-02-01,18000
...
```
O notebook detecta automaticamente a coluna de data e valores.

---

## 📝 Próximos Passos (Roadmap)

 ● Exportar dashboard em HTML

 ● Comparação Forecast vs Meta

 ● Inclusão de Prophet

 ● Heatmap de sazonalidade

 ● Geração automática de relatório PDF

 ---

 ## 💬 Contato

Caso queira explorar ainda mais o projeto ou alguma funcionalidade específica, estou aberto a trocar ideias e evoluir este dashboard!

---


