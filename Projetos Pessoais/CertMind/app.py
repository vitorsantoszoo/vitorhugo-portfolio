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
import os

BASE_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(BASE_DIR, "data")

@st.cache_data
def load_json(filename):
    path = os.path.join(DATA_DIR, filename)
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

core1_pt = load_json("core1_pt.json")
core2_pt = load_json("core2_pt.json")

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
st.markdown

# -------------------------------
# 🎯 Modo Quiz — recordação ativa (PT)
# -------------------------------

import random
from progress_manager import mark_as_seen, load_progress

progress = load_progress()

# gerar lista de (subdomínio, bullet)
pairs = [
    (sub, bullet)
    for sub in subdomains
    for bullet in subdomains[sub]
]

if pairs:
    sub_sel, bullet_pt = random.choice(pairs)

    st.markdown("## 🎯 Modo Quiz")
    st.markdown(f"### Subdomínio: **{sub_sel}**")
    st.markdown(f"**Item:**")
    st.markdown(f"> {bullet_pt}")

    # marca automaticamente como visto
    mark_as_seen(exam_choice, domain_choice, sub_sel, bullet_pt)

    # progresso
    total = len(pairs)
    seen = sum([
        len(progress.get(exam_choice, {}).get(domain_choice, {}).get(s, []))
        for s in subdomains
    ])
    pct = (seen / total) * 100 if total > 0 else 0

    st.markdown(f"### Progresso neste domínio: `{pct:.1f}%`")

else:
    st.info("Não há itens neste domínio.")

st.write("---")
st.markdown("Feito com ❤️ para estudo profissional.")
