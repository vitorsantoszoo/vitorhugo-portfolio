import json
import os
import random
import streamlit as st
from progress_manager import mark_as_seen, load_progress

# -------------------------------
# Configuração inicial
# -------------------------------
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
Ele mostra **questões simuladas baseadas nos Objetivos Oficiais da CompTIA A+**:

- Core 1 (220-1201)
- Core 2 (220-1202)

A proposta do CertMind é:
**→ Treinar recordação ativa**  
**→ Fixar os tópicos que realmente caem na prova**

Escolha abaixo o exame e pratique!
""")

# -------------------------------
# Carregar bancos de questões
# -------------------------------
BASE_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(BASE_DIR, "data")

@st.cache_data
def load_json(filename):
    path = os.path.join(DATA_DIR, filename)
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

core1_qbank = load_json("core1_questions_refined.json")
core2_qbank = load_json("core2_questions_refined.json")

# -------------------------------
# Selecionar exame / domínio / subdomínio
# -------------------------------
exam_choice = st.selectbox(
    "📌 Qual exame deseja estudar?",
    ["Core 1 (220-1201)", "Core 2 (220-1202)"]
)

qbank = core1_qbank if exam_choice == "Core 1 (220-1201)" else core2_qbank
questions = qbank["questions"]

# Domínio e subdomínio
domains = sorted(set(q["domain"] for q in questions))
domain_choice = st.selectbox("📂 Selecione um domínio:", domains)

subdomains = sorted(set(q["subdomain"] for q in questions if q["domain"] == domain_choice))
subdomain_choice = st.selectbox("🧩 Selecione um subdomínio:", subdomains)

filtered_questions = [q for q in questions if q["subdomain"] == subdomain_choice]

st.markdown(f"## 🎯 Modo Quiz — {domain_choice}")
progress = load_progress()

# -------------------------------
# Estado do Quiz
# -------------------------------
if "current_question" not in st.session_state:
    st.session_state["current_question"] = None
if "answered" not in st.session_state:
    st.session_state["answered"] = False
if "answered_correctly" not in st.session_state:
    st.session_state["answered_correctly"] = False

# Selecionar nova questão apenas se nenhuma estiver ativa
if st.session_state["current_question"] is None and filtered_questions:
    st.session_state["current_question"] = random.choice(filtered_questions)
    st.session_state["answered"] = False
    st.session_state["answered_correctly"] = False

q = st.session_state["current_question"]

if not filtered_questions:
    st.info("Ainda não há questões disponíveis para este subdomínio.")
else:
    st.markdown(f"### Subdomínio: **{q['subdomain']}**")
    st.write("---")
    st.markdown(f"**Pergunta:** {q['stem_md']}")

    # Escolha
    choice = st.radio(
        "Escolha a alternativa correta:",
        options=["A", "B", "C", "D"],
        format_func=lambda x: f"{x}) {q['options'][x]}",
        index=None,
        key=f"choice_{q['id']}"
    )

    correct = q["answer"]

    # Botão de resposta
    if st.button("Responder") and not st.session_state["answered"]:
        if choice is None:
            st.warning("⚠️ Você precisa escolher uma alternativa antes de responder.")
        elif choice == correct:
            st.success(f"✅ Resposta Correta! Alternativa {correct}) {q['options'][correct]}")
            st.session_state["answered_correctly"] = True
            st.session_state["answered"] = True
            mark_as_seen(exam_choice, domain_choice, subdomain_choice, q["id"])
        else:
            st.error(f"❌ Resposta Incorreta! Tente novamente.")
            st.session_state["answered_correctly"] = False
            st.session_state["answered"] = True

    # Mostra feedback se já respondeu
    if st.session_state["answered"]:
        if st.session_state["answered_correctly"]:
            if st.button("Próxima questão 🔁"):
                st.session_state["current_question"] = random.choice(filtered_questions)
                st.session_state["answered"] = False
                st.session_state["answered_correctly"] = False
                st.rerun()
        else:
            st.info("🔁 Tente novamente. Escolha outra alternativa e clique em **Responder**.")

    # Progresso
    seen = sum([
        1 for _q in filtered_questions
        if _q["id"] in set(progress.get(exam_choice, {}).get(domain_choice, {}).get(subdomain_choice, []))
    ])
    total = len(filtered_questions)
    pct = (seen / total * 100) if total else 0.0
    st.progress(pct / 100)
    st.markdown(f"### Progresso neste subdomínio: `{pct:.1f}%`")

st.write("---")
st.markdown("Feito com ❤️ para estudo profissional.")
