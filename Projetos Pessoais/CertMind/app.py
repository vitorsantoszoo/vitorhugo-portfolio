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

Este aplicativo **não é um curso teórico** – e **não** traz textos explicativos.  
Ele mostra os **Objetivos Oficiais da CompTIA** (o que cai na prova) e gera **questões simuladas** com base nesses tópicos, para treinar **recordação ativa**:

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
# Carregar bancos de questões (MCQ geradas)
# -------------------------------
core1_qbank = load_json("core1_questions.json")
core2_qbank = load_json("core2_questions.json")

def questions_for_domain(qbank: dict, domain_title: str):
    """Filtra questões do domínio selecionado."""
    return [
        q for q in qbank.get("questions", [])
        if q["domain"] == domain_title
    ]

qbank = core1_qbank if exam_choice == "Core 1 (220-1201)" else core2_qbank
domain_questions = questions_for_domain(qbank, domain_choice)

# -------------------------------
# 🎯 Modo Quiz — Pratique com questões reais (v2)
# -------------------------------
progress = load_progress()
st.markdown("## 🎯 Modo Quiz — Pratique com questões reais")

if domain_questions:
    # Seleciona questão aleatória
    q = random.choice(domain_questions)
    st.markdown(f"### 🧩 Questão sobre: **{q['subdomain']}**")
    st.write("---")

    # Enunciado explicativo
    st.markdown(
        f"**Pergunta:**\n\n{q['stem_md']} "
        "\n\nEscolha a alternativa correta abaixo:"
    )

    # Sessão de estado para armazenar tentativa e acerto
    if "answered_correctly" not in st.session_state:
        st.session_state["answered_correctly"] = False
        st.session_state["last_question_id"] = q["id"]

    # Se nova questão, resetar estado
    if st.session_state["last_question_id"] != q["id"]:
        st.session_state["answered_correctly"] = False
        st.session_state["last_question_id"] = q["id"]

    # Exibe alternativas
    choice = st.radio(
        "Alternativas:",
        options=["A", "B", "C", "D"],
        format_func=lambda x: f"{x}) {q['options'][x]}",
        index=None,
        key=f"choice_{q['id']}"
    )

    correct = q["answer"]

    # Botão de resposta
    if st.button("Responder"):
        if choice is None:
            st.warning("Escolha uma alternativa antes de responder.")
        elif choice == correct:
            st.success(f"✅ Resposta Correta! Alternativa {correct}) {q['options'][correct]}")
            st.session_state["answered_correctly"] = True
            mark_as_seen(exam_choice, domain_choice, q["subdomain"], q["id"])
        else:
            st.error(f"❌ Resposta Incorreta! Tente novamente.")
            st.session_state["answered_correctly"] = False

    # Exibe progresso
    seen = sum([
        1 for _q in domain_questions
        if _q["id"] in set(progress.get(exam_choice, {}).get(domain_choice, {}).get(_q["subdomain"], []))
    ])
    total = len(domain_questions)
    pct = (seen / total * 100) if total else 0.0
    st.progress(pct / 100)
    st.markdown(f"### Progresso neste domínio: `{pct:.1f}%`")

    # Mostra botão "Próxima questão" somente após acerto
    if st.session_state["answered_correctly"]:
        if st.button("Próxima questão 🔁"):
            st.session_state["answered_correctly"] = False
            st.experimental_rerun()

else:
    st.info("Ainda não há questões geradas para este domínio.")

st.write("---")
st.markdown("Feito com ❤️ para estudo profissional.")
