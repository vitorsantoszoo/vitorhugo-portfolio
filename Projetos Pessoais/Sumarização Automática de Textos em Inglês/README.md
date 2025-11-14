# 📘 Sumarização Automática de Textos com Transformers (DistilBART)

Este projeto demonstra como utilizar modelos pré-treinados da biblioteca **Hugging Face Transformers**
para realizar **resumo automático de textos** em inglês, utilizando o modelo
`sshleifer/distilbart-cnn-12-6`, uma versão compacta e eficiente do BART.

---

## 🎯 Objetivo
Aplicar um modelo *encoder-decoder* pré-treinado para gerar resumos coerentes a partir de textos
curtos e médios, demonstrando um exemplo prático de IA aplicada a Processamento de Linguagem Natural (NLP).

O projeto inclui:
- Uso do pipeline de sumarização;
- Formatação organizada da saída;
- Tradução manual do resumo para PT-BR;
- Análise interpretativa dos resultados.

---

## 🧠 Sobre o Modelo Utilizado
O **DistilBART CNN-12-6** é uma versão reduzida do modelo BART, treinado no dataset CNN/DailyMail
para tarefas de summarization.  
Ele é rápido, leve e produz resumos de boa qualidade em inglês.

---

## ⚙️ Tecnologias Utilizadas
- Python  
- Google Colab  
- Hugging Face Transformers  
- Modelo: `sshleifer/distilbart-cnn-12-6`

---

## 📦 Estrutura do Notebook
O notebook contém:

1. **Instalação das bibliotecas**
2. **Carregamento do modelo**
3. **Definição do texto de entrada**
4. **Geração do resumo**
5. **Formatação legível da saída**
6. **Tradução manual do resumo**
7. **Comentário interpretativo**

---

## 📝 Exemplo de Uso

```python
from transformers import pipeline

summarizer = pipeline(
    task="summarization",
    model="sshleifer/distilbart-cnn-12-6"
)

resumo = summarizer(
    text,
    max_length=60,
    min_length=25
)[0]["summary_text"]

print(resumo)

