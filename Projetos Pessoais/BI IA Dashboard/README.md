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

Este projeto foi projetado para ser modular, extensível e totalmente executável pelo notebook principal:

```
/notebooks/bi_dashboard_pipeline.ipynb
```
Esse notebook funciona como orquestrador de todo o pipeline:

● 📥 Carregamento inteligente de dados `(load_data.py)`

● 🧹 Limpeza e preparação automática `(preprocessing.py)`

● 📊 Cálculo de métricas e agregações `(metrics.py)`

● 🤖 Previsões com IA — Random Forest + Intervalo de Confiança `(forecasting.py)`

● 📈 Visualizações interativas estilo BI `(visualization.py)`

● 📝 Geração automática de relatório NLG `(nlg_agent.py)`

● 💾 Exportação opcional para HTML / PNG / PDF `(dashboard/exports/)`
---

## 🟩 1️⃣ Coloque seus dados na pasta correta

O dataset deve ser salvo em:

```
data/user_uploads/seu_arquivo.csv
```
✔️ O pipeline reconhece automaticamente:

● A coluna de datas

● A coluna de valores (faturamento / vendas / lucro)

● Formatações diferentes (`YYYY-MM-DD`, `DD/MM/YYYY`, etc.)

Se preferir, você também pode usar o dataset de exemplo:

```
data/examples/sample_sales.csv
```
## 🟦 2️⃣ Abra o notebook principal

Acesse:

```
notebooks/bi_dashboard_pipeline.ipynb
```
E clique em Runtime > Run all (Executar tudo).
---
## 🟧 3️⃣ O pipeline fará automaticamente:
✔️ Carregamento inteligente

O módulo load_data.py identifica:

● Coluna de datas

● Coluna numérica principal

● Formatação

● Frequência da série

✔️ Pré-processamento completo

preprocessing.py faz:

● Limpeza de valores ausentes

● Padronização de datas

● Ordenação temporal

● Transformação mensal/semanal se necessário

✔️ Cálculo de métricas e KPIs

metrics.py calcula:

● Totals

● Variações percentuais

● Médias móveis

● Melhores e piores períodos

● Sazonalidade básica

✔️ Dashboard interativo

● Visualization.py renderiza:

● Gráfico de série temporal

● Gráfico de barras

● Variação percentual

● Heatmaps (opcional)

● Linhas de tendência

✔️ Previsão com intervalo de confiança

forecasting.py usa:

● RandomForest + lags

● Bootstrap (80 simulações)

● IC 90%

● Gráfico premium estilo Power BI

✔️ Relatório automático NLG

nlg_agent.py gera:

● Texto descritivo sobre o dataset

● Insights principais

● Análise da tendência

● Avaliação da previsão

● Sugestões de ação

O relatório é salvo em:

```
dashboard/reports/
```
---
## 🟨 4️⃣ Exportações (opcional)

O notebook pode gerar automaticamente:

📄 PDF

🌐 HTML

🖼️ Imagens dos gráficos (PNG/JPG)

🧾 Relatório completo NLG

Os arquivos ficam em:

```
dashboard/exports/
```
## 🟪 5️⃣ Substituindo o dataset

Para usar seu próprio arquivo:

1. Coloque o arquivo em:

```
data/user_uploads/
```
2. No notebook, selecione o nome do arquivo na célula de configuração

3. Execute tudo novamente

Não é necessário alterar código.
---
##🟫 Requisitos

```
pandas
numpy
scikit-learn
plotly
```
(O notebook principal cuida das instalações automaticamente no Colab.)
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


