import json
import streamlit as st
import os
import random
from progress_manager import mark_as_seen, load_progress

st.set_page_config(
    page_title="CertMind — Estudo para Certificações",
    layout="centered",
    page_icon="🧠"
)

st.markdown("""
# 🧠 **CertMind**

### Estudo guiado para CompTIA A+ (Objetivos Oficiais)

---

Este aplicativo **não é um curso teórico**.  
Ele **não ensina a matéria** diretamente ele mostra **os Objetivos Oficiais da CompTIA** (blueprint da prova), que definem *o que* será cobrado nos exames:

- Core 1 (220-1201)
- Core 2 (220-1202)

Esses objetivos são exclusivamente listas de tópicos — **não possuem textos explicativos**.

A proposta do CertMind é:

**→ Mostrar o que realmente cai na prova**  
**→ Gerar questões simuladas baseadas nesses tópicos (modo Quiz)**

Assim você treina *recordação ativa* e internaliza os itens que a prova realmente cobra.

Escolha abaixo o exame e o domínio para estudar.
""")


# -------------------------------
# Carregar JSONs
# -------------------------------
BASE_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(BASE_DIR, "data")

@st.cache_data
def load_json(filename):
    path = os.path.join(DATA_DIR, filename)
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

core1_pt = load_json("core1_pt.json")
core2_pt = load_json("core2_pt.json")

# ===============================
# Estatísticas / Landing PRO
# ===============================

def contar_stats(db: dict):
    doms = len(db.keys())
    subs = sum([len(db[d]) for d in db])
    bullets = sum([len(db[d][s]) for d in db for s in db[d]])
    return doms, subs, bullets

core1_stats = contar_stats(core1_pt)
core2_stats = contar_stats(core2_pt)

st.write("### 🔍 Estatísticas do Conteúdo")
col1, col2 = st.columns(2)

with col1:
    st.markdown("**Core 1 (220-1201)**")
    st.write(f"- Domínios: {core1_stats[0]}")
    st.write(f"- Subdomínios: {core1_stats[1]}")
    st.write(f"- Bullets: {core1_stats[2]}")

with col2:
    st.markdown("**Core 2 (220-1202)**")
    st.write(f"- Domínios: {core2_stats[0]}")
    st.write(f"- Subdomínios: {core2_stats[1]}")
    st.write(f"- Bullets: {core2_stats[2]}")

st.write("---")

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

# -------------------------------
# 🎯 Modo Quiz — recordação ativa (PT)
# -------------------------------
progress = load_progress()

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

    mark_as_seen(exam_choice, domain_choice, sub_sel, bullet_pt)

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
