# 🧠 CertMind — Study Assistant for IT Certifications

O **CertMind** é um projeto pessoal desenvolvido para auxiliar no estudo de certificações técnicas da área de TI.  

O objetivo é transformar PDFs oficiais, exam objectives e materiais estruturados em **conteúdo navegável**, claro e interativo — permitindo revisão de tópicos, estudo organizado por domínio, e futuramente quizzes inteligentes.

Atualmente, o CertMind já suporta:

### ✅ CompTIA A+ (V15)
- Core 1 (220-1201)
- Core 2 (220-1202)

### 🚀 Expansão futura planejada
O projeto foi pensado para ser universal não apenas para CompTIA.

Serão incluídas no futuro (pipeline planejado):

- CompTIA Network+ / Security+
- Cisco (CCNA, CyberOps)
- EXIN (ISO 27001, DPO)
- ITIL Foundation
- AWS Cloud Practitioner

---

## 🧩 Como o CertMind funciona

1) Os PDFs oficiais são baixados
2) Os exam objectives são mapeados automaticamente
3) São extraídos domínios, subdomínios e bullet points
4) Todo conteúdo é traduzido por IA (Marian)
5) O conteúdo final é disponibilizado em JSON
6) O app Streamlit lê os arquivos JSON e exibe para estudo

---

## 📂 Estrutura do projeto

```
CertMind/
├─ data/
│ ├─ core1_en.json
│ ├─ core1_pt.json
│ ├─ core2_en.json
│ └─ core2_pt.json
├─ app.py
├─ requirements.txt
└─ README.md ← este arquivo
```
---

## ▶ Como executar localmente

```bash
pip install -r requirements.txt
streamlit run app.py
```
---

| funcionalidade                       |         status        |
| ------------------------------------ | :-------------------: |
| extração automática dos PDFs         |           ✅           |
| parser Core1 / Core2                 |           ✅           |
| tradução IA EN→PT                    |           ✅           |
| UI Streamlit — navegação por domínio |           ✅           |
| modo quiz com geração dinâmica       | 🚧 em desenvolvimento |

---

🎯 propósito

CertMind nasceu para facilitar o estudo e a memorização dos exam objectives — criando uma ponte entre PDFs técnicos e estudo estruturado real.

Ele serve para qualquer pessoa que esteja estudando certificações, especialmente:

- estudantes iniciando carreira em TI

- candidatos a certificações

- profissionais querendo relembrar tópicos

- autodidatas que precisam de estrutura

---

Feito e mantido por Vitor Hugo.
Foco em segurança, proteção de dados e mitigação de riscos.

---
