# 🚀 Guia Completo: GitHub + Deploy Web do CertMind V2

## 📋 Índice
1. [Preparação dos Arquivos](#preparacao)
2. [Upload no GitHub](#github)
3. [Deploy no Streamlit Cloud](#deploy)
4. [Teste da Aplicação](#teste)

---

## 📁 Preparação dos Arquivos {#preparacao}

### Estrutura de Pastas que Você Precisa Criar

```
CertMind/
├── data/
│   ├── core1_questions_v2.json
│   ├── core2_questions_v2.json
│   └── progress_v2.json
├── modules/
│   ├── spaced_repetition.py
│   ├── progress_manager_v2.py
│   └── analytics.py
├── utils/
│   └── data_migration.py
├── app_v2.py
├── requirements.txt
├── README_V2.md
├── QUICK_START.md
└── .gitignore
```

### Arquivos que Você Já Tem (no workspace)

Todos os arquivos estão prontos em `/workspace/certmind_v2/`

---

## 🌐 Upload no GitHub (Sem Terminal!) {#github}

### Passo 1: Criar Repositório no GitHub

1. Acesse **https://github.com**
2. Faça login na sua conta
3. Clique no botão **"+" (New repository)** no canto superior direito
4. Preencha:
   - **Repository name:** `CertMind` (ou o nome que preferir)
   - **Description:** "Assistente inteligente de estudos para certificações de TI com Spaced Repetition"
   - Deixe como **Public** (para poder fazer deploy gratuito)
   - ✅ Marque **"Add a README file"**
   - ✅ Marque **"Add .gitignore"** e selecione **"Python"**
5. Clique em **"Create repository"**

### Passo 2: Criar Estrutura de Pastas no GitHub

#### 2.1 Criar pasta `data/`
1. No repositório criado, clique em **"Add file"** → **"Create new file"**
2. Digite: `data/.gitkeep`
3. Role até o final e clique em **"Commit new file"**

#### 2.2 Criar pasta `modules/`
1. Clique em **"Add file"** → **"Create new file"**
2. Digite: `modules/.gitkeep`
3. Clique em **"Commit new file"**

#### 2.3 Criar pasta `utils/`
1. Clique em **"Add file"** → **"Create new file"**
2. Digite: `utils/.gitkeep`
3. Clique em **"Commit new file"**

### Passo 3: Upload dos Arquivos

Agora vamos fazer upload de cada arquivo na pasta correta:

#### 3.1 Upload dos arquivos de dados

**📂 Pasta `data/`:**

1. Clique na pasta **`data/`**
2. Clique em **"Add file"** → **"Upload files"**
3. Faça upload de:
   - `core1_questions_v2.json`
   - `core2_questions_v2.json`
   - `progress_v2.json`
4. Clique em **"Commit changes"**

**Onde encontrar esses arquivos no seu computador:**
- Baixe do workspace: `/workspace/certmind_v2/data/`

#### 3.2 Upload dos módulos Python

**📂 Pasta `modules/`:**

1. Volte para a raiz do repositório (clique no nome do repo)
2. Clique na pasta **`modules/`**
3. Clique em **"Add file"** → **"Upload files"**
4. Faça upload de:
   - `spaced_repetition.py`
   - `progress_manager_v2.py`
   - `analytics.py`
5. Clique em **"Commit changes"**

**Onde encontrar:** `/workspace/certmind_v2/` (arquivos principais)

#### 3.3 Upload da pasta utils

**📂 Pasta `utils/`:**

1. Volte para a raiz do repositório
2. Clique na pasta **`utils/`**
3. Clique em **"Add file"** → **"Upload files"**
4. Faça upload de:
   - `data_migration.py`
5. Clique em **"Commit changes"**

#### 3.4 Upload dos arquivos principais

**📂 Raiz do repositório:**

1. Volte para a raiz do repositório
2. Clique em **"Add file"** → **"Upload files"**
3. Faça upload de:
   - `app_v2.py`
   - `requirements.txt`
   - `QUICK_START.md`
4. Clique em **"Commit changes"**

#### 3.5 Substituir o README

1. Na raiz do repositório, clique no arquivo **`README.md`**
2. Clique no ícone de **lápis (Edit)** no canto direito
3. Apague todo o conteúdo
4. Abra o arquivo `README_V2.md` do workspace
5. Copie todo o conteúdo e cole no GitHub
6. Clique em **"Commit changes"**

---

## ☁️ Deploy no Streamlit Cloud (Testar via Web) {#deploy}

### Passo 1: Criar Conta no Streamlit Cloud

1. Acesse **https://share.streamlit.io/**
2. Clique em **"Sign up"**
3. Escolha **"Continue with GitHub"**
4. Autorize o Streamlit a acessar seus repositórios

### Passo 2: Fazer Deploy do App

1. No painel do Streamlit Cloud, clique em **"New app"**
2. Preencha:
   - **Repository:** Selecione `seu-usuario/CertMind`
   - **Branch:** `main` (ou `master`)
   - **Main file path:** `app_v2.py`
3. Clique em **"Deploy!"**

### Passo 3: Aguardar Deploy

- O Streamlit Cloud vai:
  1. ✅ Clonar seu repositório
  2. ✅ Instalar as dependências do `requirements.txt`
  3. ✅ Iniciar a aplicação
  4. ✅ Gerar uma URL pública

**Tempo estimado:** 2-5 minutos

### Passo 4: Acessar Sua Aplicação

Após o deploy concluir, você receberá uma URL como:
```
https://seu-usuario-certmind-app-v2-abc123.streamlit.app
```

**🎉 Sua aplicação está no ar!**

---

## 🧪 Teste da Aplicação {#teste}

### Checklist de Testes

#### ✅ Teste 1: Página Principal (Quiz)
1. Acesse a URL do seu app
2. Verifique se o **título "CertMind V2"** aparece
3. Veja se os **domínios (Core 1 e Core 2)** estão disponíveis
4. Selecione um domínio
5. Clique em **"Iniciar Quiz"**

#### ✅ Teste 2: Responder Questões
1. Leia a pergunta que aparece
2. Selecione uma resposta (A, B, C ou D)
3. Clique em **"Confirmar Resposta"**
4. Verifique se aparece:
   - ✅ Resposta correta/incorreta
   - 📝 Explicação detalhada
   - 📊 Estatísticas da questão

#### ✅ Teste 3: Dashboard
1. Clique na aba **"📊 Dashboard"** no menu lateral
2. Verifique se aparecem:
   - Total de questões respondidas
   - Taxa de acerto
   - Nível de domínio por tópico
   - Gráficos de progresso

#### ✅ Teste 4: Spaced Repetition
1. Responda algumas questões (pelo menos 5)
2. Alterne entre respostas certas e erradas
3. Veja no Dashboard se as questões com desempenho ruim aparecem como **"Áreas que precisam de atenção"**
4. Volte ao Quiz e veja se o sistema prioriza questões que você errou

#### ✅ Teste 5: Persistência de Dados
1. Responda algumas questões
2. **Recarregue a página** (F5)
3. Verifique se seu progresso foi mantido
4. Vá ao Dashboard e confirme que as estatísticas estão salvas

---

## 🔧 Solução de Problemas Comuns

### Problema 1: "Error: Module not found"
**Causa:** O `requirements.txt` não foi enviado ou está incorreto

**Solução:**
1. Verifique se o arquivo `requirements.txt` está na raiz do repositório
2. Conteúdo deve ser exatamente:
   ```
   streamlit==1.31.0
   pandas==2.0.3
   plotly==5.18.0
   ```
3. Faça redeploy no Streamlit Cloud

### Problema 2: "FileNotFoundError: data/core1_questions_v2.json"
**Causa:** A pasta `data/` não foi criada ou os arquivos JSON não foram enviados

**Solução:**
1. Verifique se a pasta `data/` existe no repositório
2. Confirme que os 3 arquivos JSON estão dentro dela
3. Faça redeploy

### Problema 3: "Import Error: cannot import spaced_repetition"
**Causa:** Os módulos não estão na pasta `modules/` ou falta o `__init__.py`

**Solução:**
1. Vá para a pasta `modules/` no GitHub
2. Clique em **"Add file"** → **"Create new file"**
3. Nome: `__init__.py` (deixe vazio)
4. Commit
5. Verifique se os 3 arquivos .py estão lá
6. Faça redeploy

### Problema 4: App fica carregando infinitamente
**Causa:** Erro no código ou dependência incompatível

**Solução:**
1. No Streamlit Cloud, clique em **"Manage app"**
2. Clique em **"View logs"**
3. Procure por mensagens de erro em vermelho
4. Me envie o erro para eu te ajudar a corrigir

---

## 📱 Compartilhar Sua Aplicação

Depois que tudo estiver funcionando:

1. Copie a URL do seu app (ex: `https://seu-usuario-certmind.streamlit.app`)
2. Compartilhe com quem quiser!
3. A aplicação está **100% funcional via web**, sem necessidade de instalar nada

**Dica:** Adicione essa URL no README do seu GitHub para facilitar o acesso!

---

## 🎯 Resumo Visual do Processo

```
Passo 1: GitHub                    Passo 2: Streamlit Cloud
┌─────────────────┐               ┌─────────────────┐
│ Criar Repo      │──────────────▶│ Conectar GitHub │
│ Upload Arquivos │               │ Selecionar Repo │
│ Estruturar      │               │ Deploy App      │
└─────────────────┘               └─────────────────┘
                                           │
                                           ▼
                                  ┌─────────────────┐
                                  │ App Online! 🎉  │
                                  │ URL Pública     │
                                  └─────────────────┘
```

---

## 🆘 Precisa de Ajuda?

Se encontrar qualquer problema:
1. Tire um **print da tela**
2. Copie a **mensagem de erro** completa
3. Me envie e eu te ajudo a resolver!

**Boa sorte com o deploy! 🚀**
