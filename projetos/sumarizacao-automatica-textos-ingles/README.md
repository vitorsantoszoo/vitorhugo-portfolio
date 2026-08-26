# 📘 Sumarização Automática de Textos com Transformers (DistilBART)

Resumo automático de textos em inglês usando o modelo pré-treinado `sshleifer/distilbart-cnn-12-6` (versão compacta do BART), da biblioteca Hugging Face Transformers.

---

## 🎯 Objetivo

Aplicar um modelo *encoder-decoder* pré-treinado para gerar resumos coerentes a partir de textos curtos e médios, demonstrando um exemplo prático de IA aplicada a Processamento de Linguagem Natural (NLP). O notebook cobre: uso do pipeline de sumarização, formatação da saída, tradução manual do resumo para PT-BR e uma análise interpretativa dos resultados.

---

## 🧠 Sobre o modelo

**DistilBART CNN-12-6** é uma versão reduzida do BART, treinada no dataset CNN/DailyMail para tarefas de summarization. É rápido, leve e produz resumos de boa qualidade em inglês.

---

## 🛠️ Tecnologias

Python • Google Colab • Hugging Face Transformers (`sshleifer/distilbart-cnn-12-6`) • PyTorch (backend do pipeline)

---

## 🚀 Como executar

```bash
git clone https://github.com/vitorsantoszoo/vitorhugo-portfolio.git
cd vitorhugo-portfolio/projetos/sumarizacao-automatica-textos-ingles
pip install -r requirements.txt
```

Abra `notebooks/Sumarização_cleaned.ipynb` no Colab (ou Jupyter local) e execute célula por célula: instalação, carregamento do modelo, texto de entrada, geração e formatação do resumo.

```python
from transformers import pipeline

summarizer = pipeline(task="summarization", model="sshleifer/distilbart-cnn-12-6")

resumo = summarizer(text, max_length=60, min_length=25)[0]["summary_text"]
print(resumo)
```

---

## 📈 Resultados

O pipeline gera resumos coerentes e concisos a partir de textos em inglês, com formatação legível da saída e tradução manual para PT-BR incluída no notebook como parte da análise interpretativa.

---

## 📫 Contato

📧 **Email:** vitoor.hugoo@hotmail.com  
🔗 **LinkedIn:** [linkedin.com/in/vitor-hugo-3861391b8](https://www.linkedin.com/in/vitor-hugo-3861391b8/)  
💻 **GitHub:** [github.com/vitorsantoszoo](https://github.com/vitorsantoszoo)
