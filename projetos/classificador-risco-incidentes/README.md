# Classificador de Risco de Incidentes (UNSW-NB15)

Este projeto utiliza técnicas de Machine Learning aplicadas ao dataset UNSW-NB15 para classificar diferentes tipos de ataques cibernéticos com base em atributos de tráfego de rede capturados em nível de fluxo.

Mais importante do que classificar ataques, este projeto **explica** como o modelo toma decisões usando métodos avançados de interpretabilidade.

---

## Objetivos do Projeto

- Classificar categorias de ataques cibernéticos
- Analisar quais variáveis influenciam o risco de incidente
- Construir visualizações profissionais a partir de atributos de rede
- Utilizar SHAP para explicabilidade de predição individual

---

## Por que este projeto é útil?

Este projeto é útil porque transforma dados brutos de tráfego de rede em **inteligência acionável** permitindo que um analista de segurança entenda não apenas “se” há risco, mas **por que** o modelo considera algo como ataque.

Diferente de classificadores comuns, aqui o foco não é só prever mas **explicar** o que está influenciando o risco.

Isso pode ajudar um usuário em situações reais, como por exemplo:

- Analistas SOC que querem entender quais protocolos/serviços estão mais associados a incidentes
- Equipes de Blue Team que desejam priorizar onde atuar primeiro
- Profissionais que precisam justificar decisões baseadas em modelo para auditoria / compliance
- Alguém estudando cibersegurança e querendo enxergar o “cérebro” de um classificador moderno

Em resumo:

Este projeto não é apenas uma classificação de ataques, ele ajuda a **tomar decisão** e **priorizar risco**.

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

## Cenários reais de aplicação

Este tipo de modelo pode ser aplicado como apoio em diferentes etapas do ciclo de detecção e resposta em Segurança da Informação, tais como:

- **SOC / SIEM**: priorização de alertas com maior probabilidade de ataque real
- **Threat Hunting**: identificação de padrões comportamentais em fluxos de rede
- **Análise Forense**: apoio na interpretação de tráfego suspeito após um incidente
- **Redução de Ruído Operacional**: foco nas features mais decisivas (explicabilidade SHAP)
- **Educação e Capacitação**: demonstração prática de como algoritmos realmente “enxergam” o tráfego de rede

O modelo aqui desenvolvido pode ser usado como camada adicional de decisão, como filtro preliminar ou como componente de um pipeline maior de detecção / classificação de risco.

---

## Status

✅ Projeto concluído com sucesso

Próximas etapas possíveis (futuras melhorias):

- Exportar modelo para API REST
- Criar dashboard visual (Streamlit)
- Testar com dados de rede capturados via pcap

---
