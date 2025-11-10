# Classificador de Risco de Incidentes (UNSW-NB15)

Este projeto utiliza técnicas de Machine Learning aplicadas ao dataset UNSW-NB15 para classificar diferentes tipos de ataques cibernéticos com base em atributos de tráfego de rede capturados em nível de fluxo.

Mais importante do que classificar ataques, este projeto **explica** como o modelo toma decisões — usando métodos avançados de interpretabilidade.

---

## Objetivos do Projeto

- Classificar categorias de ataques cibernéticos
- Analisar quais variáveis influenciam o risco de incidente
- Construir visualizações profissionais a partir de atributos de rede
- Utilizar SHAP para explicabilidade de predição individual

---

## Técnicas utilizadas

| Etapa | Tecnologias / Métodos |
|------:|------------------------|
| Data Loading | KaggleHub (download direto do UNSW-NB15) |
| Pré-processamento | Pandas, Normalização, One-Hot Encoding |
| EDA | Gráficos interpretativos (Protocol / Service / State) |
| Modelo | LightGBM (Multi-Classe) |
| Interpretação | SHAP → Summary Plot + Feature Ranking + Waterfall |

---

## Resultados principais

- Identificação das categorias de ataque predominantes
- Ranking real das variáveis mais relevantes para ataques **Generic**
- SHAP Waterfall explica claramente o “porquê” de uma classificação
- Visualização didática e interpretável para usuários não técnicos

---

## Execução

Este projeto foi desenvolvido e executado via Google Colab.

Arquivos necessários:

- o notebook principal → `Classificador de Risco de Incidentes.ipynb`

---

## Dataset

Fonte: UNSW-NB15 — dataset público para pesquisa de Intrusion Detection.

---

## Status

✅ Projeto concluído com sucesso

Próximas etapas possíveis (futuras melhorias):

- Exportar modelo para API REST
- Criar dashboard visual (Streamlit)
- Testar com dados de rede capturados via pcap

---
