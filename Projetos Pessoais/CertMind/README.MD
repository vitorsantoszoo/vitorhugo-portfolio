# ⚠️ **STATUS: Projeto em Desenvolvimento / Temporariamente Paralisado**

O projeto **CertMind** ainda está em fase de construção e experimentação.  
No momento, o desenvolvimento foi **pausado** para reavaliação técnica e reestruturação do sistema de quiz.  
Você pode testar a versão atual do aplicativo acessando o link abaixo:

👉 **[Acessar o App CertMind no Streamlit](https://vitorhugo-portfolio-6cvthe54edfondqyywzunj.streamlit.app/)**

Se você tiver interesse em **colaborar, contribuir com código, ou ajudar a finalizar o projeto**,  
fique à vontade para abrir uma *issue*, enviar *pull requests* ou entrar em contato.  
Toda ajuda é muito bem-vinda! 💡

---

# 🧠 CertMind — Study Assistant for IT Certifications

O **CertMind** é um projeto pessoal desenvolvido para auxiliar no estudo de certificações técnicas da área de TI.  

O objetivo é transformar PDFs oficiais, *exam objectives* e materiais estruturados em **conteúdo navegável, claro e interativo** — permitindo revisão de tópicos, estudo organizado por domínio e, futuramente, **quizzes inteligentes e personalizados**.

Atualmente, o CertMind já suporta:

### ✅ CompTIA A+ (V15)
- Core 1 (220-1201)
- Core 2 (220-1202)

---

### 🚀 Expansão futura planejada
O projeto foi pensado para ser universal — não apenas para CompTIA.

Em futuras versões, estão planejadas as seguintes certificações:

- CompTIA Network+ / Security+
- Cisco (CCNA, CyberOps)
- EXIN (ISO 27001, DPO)
- ITIL Foundation
- AWS Cloud Practitioner

---

## 🧩 Como o CertMind funciona

1. Os PDFs oficiais são baixados.  
2. Os *exam objectives* são mapeados automaticamente.  
3. São extraídos domínios, subdomínios e *bullet points*.  
4. Todo conteúdo é traduzido por IA (Marian).  
5. O conteúdo final é estruturado em arquivos JSON.  
6. O app em **Streamlit** lê esses arquivos e exibe de forma interativa para estudo.

---

## 📂 Estrutura do projeto

data/
├─ .gitkeep                        # Mantém a pasta versionada no Git
├─ core1_questions_expanded.json   # Banco completo de questões — CompTIA A+ Core 1 (220-1201)
├─ core2_questions_expanded.json   # Banco completo de questões — CompTIA A+ Core 2 (220-1202)
├─ progress.json                   # Armazena o progresso do usuário nos quizzes

---

## ▶ Como executar localmente

```bash
pip install -r requirements.txt
streamlit run app.py
```

---


| Funcionalidade                       |         Status        |
| ------------------------------------ | :-------------------: |
| Extração automática dos PDFs         |           ✅           |
| Parser Core1 / Core2                 |           ✅           |
| Tradução IA EN→PT                    |           ✅           |
| UI Streamlit — navegação por domínio |           ✅           |
| Modo Quiz — geração dinâmica         | 🚧 Em desenvolvimento |

---

🎯 Propósito

O CertMind nasceu para facilitar o estudo e a memorização dos exam objectives — criando uma ponte entre PDFs técnicos e o aprendizado prático estruturado.

É ideal para:

Estudantes iniciando na área de TI

Candidatos a certificações internacionais

Profissionais revisando tópicos técnicos

Autodidatas que buscam estrutura no aprendizado

---

Feito e mantido por Vitor Hugo
💬 Aberto a colaborações — foco em segurança, proteção de dados e aprendizado acessível.

---

