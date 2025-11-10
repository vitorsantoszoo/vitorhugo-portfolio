# Classificador de Risco de Incidentes de Segurança

Projeto desenvolvido em Python utilizando Machine Learning para classificar o nível de severidade (Low / Medium / High) de incidentes de segurança cibernética, baseado em atributos reais de tráfego, indicadores de ataque e metadados técnicos.

O modelo utiliza o dataset **"Cyber Security Attacks Dataset"** disponível publicamente no Kaggle.

---

## Objetivo

Criar um classificador supervisionado capaz de prever a **Severity Level** de um incidente, permitindo priorização inteligente e tomada de decisão em resposta a ameaças.

---

## Tecnologias e bibliotecas utilizadas

- Python
- Pandas
- NumPy
- Scikit-Learn
- LightGBM
- Pipeline (sklearn)
- KaggleHub (download automático do dataset)

---

## Etapas do projeto

- Download do dataset via KaggleHub
- Pré-processamento automático (One-Hot Encoding para categóricas)
- Split em treino / teste
- Treinamento com LightGBM Classifier
- Avaliação com classification report + matriz de confusão
- Exportação do modelo `.pkl`

---

## Dataset utilizado

Fonte:  
https://www.kaggle.com/datasets/teamincribo/cyber-security-attacks

Coluna alvo (label):
`Severity Level`

Classes previstas:
- Low
- Medium
- High

---

## Execução do Projeto (Google Colab)

```python
!pip install kagglehub
from kagglehub import dataset_download
path = dataset_download("teamincribo/cyber-security-attacks")
