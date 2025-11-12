# 🗣️ NLP Agent — Assistente Textual Inteligente

Este módulo implementa um **mini agente de linguagem natural (NLP)** que interpreta mensagens do usuário e responde com base em intenções pré-definidas.

---

## ⚙️ Como funciona
1. Recebe uma entrada de texto (mensagem do usuário).  
2. Identifica a **intenção** (saudação, projeto, visão, despedida, etc.) por meio de palavras-chave.  
3. Retorna uma **resposta aleatória** dentro do conjunto associado àquela intenção.  
4. Caso nenhuma palavra-chave seja reconhecida, usa uma resposta genérica (“default”).  

---

## 🧠 Objetivo
Simular o comportamento de um **agente de conversa inteligente**, que em versões futuras poderá ser integrado com um modelo LLM real (como GPT, Gemini, Mistral etc.), ou combinado com outros agentes do projeto (por exemplo, o Vision Agent e o Decision Agent).

---

## ▶️ Como executar no Google Colab
1. Certifique-se de que o arquivo `nlp_agent.py` está na pasta `agents/`.  
2. Instale as dependências básicas (se necessário):  
   ```python
   !pip install numpy pandas
   ```
---

