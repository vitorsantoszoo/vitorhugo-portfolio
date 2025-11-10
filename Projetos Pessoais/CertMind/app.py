import json
import streamlit as st

st.set_page_config(
    page_title="CertMind — Estudo para Certificações",
    layout="centered",
    page_icon="🧠"
)

st.markdown("""
# 🧠 **CertMind**
### Aprendizado assistido para certificações técnicas internacionais
---
Este aplicativo permite estudar conteúdos oficiais de certificações como CompTIA A+ de forma organizada e estruturada.

Selecione abaixo o exame e o domínio para visualizar os tópicos em português.
""")

# -------------------------------
# Carregar JSONs
# -------------------------------
@st.cache_data
def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

core1_pt = load_json("data/core1_pt.json")
core2_pt = load_json("data/core2_pt.json")

# -------------------------------
# Seleção de EXAME
# -------------------------------
exam_choice = st.selectbox(
    "📌 Qual exame deseja estudar?",
    ["Core 1 (220-1201)", "Core 2 (220-1202)"]
)

data = core1_pt if exam_choice == "Core 1 (220-1201)" else core2_pt

# -------------------------------
# Seleção de DOMÍNIO
# -------------------------------
domain_choice = st.selectbox(
    "📂 Selecione um domínio:",
    list(data.keys())
)

subdomains = data[domain_choice]

# -------------------------------
# Exibir subdomínios + bullets
# -------------------------------
st.markdown(f"## 📑 Domínio selecionado: **{domain_choice}**")
st.write("---")

for sub in subdomains:
    st.markdown(f"### {sub}")
    for bullet in subdomains[sub]:
        st.markdown(f"- {bullet}")
    st.write("")

st.write("---")
st.markdown("Feito com ❤️ para estudo profissional.")
