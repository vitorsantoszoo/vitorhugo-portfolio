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
# Selecionar exame
# -------------------------------
exam_choice = st.selectbox(
    "📌 Qual exame deseja estudar?",
    ["Core 1 (220-1201)", "Core 2 (220-1202)"]
)

qbank = core1_qbank if exam_choice == "Core 1 (220-1201)" else core2_qbank
questions = qbank["questions"]

# -------------------------------
# 🎯 Modo Quiz
# -------------------------------
progress = load_progress()
st.markdown("## 🎯 Modo Quiz — Pratique com questões reais")

if questions:
    q = random.choice(questions)

    st.markdown(f"### 🧩 Domínio: **{q['domain']}**")
    st.markdown(f"#### Subdomínio: {q['subdomain']}")
    st.write("---")

    st.markdown(f"**Pergunta:** {q['stem_md']}")

    # Gerar radio de alternativas
    choice = st.radio(
        "Escolha a alternativa correta:",
        options=["A", "B", "C", "D"],
        format_func=lambda x: f"{x}) {q['options'][x]}",
        index=None,
        key=f"choice_{q['id']}"
    )

    correct = q["answer"]

    # Controle de estado
    if "answered_correctly" not in st.session_state:
        st.session_state["answered_correctly"] = False
        st.session_state["last_question_id"] = q["id"]

    if st.session_state["last_question_id"] != q["id"]:
        st.session_state["answered_correctly"] = False
        st.session_state["last_question_id"] = q["id"]

    # Botão de resposta
    if st.button("Responder"):
        if choice is None:
            st.warning("⚠️ Escolha uma alternativa antes de responder.")
        elif choice == correct:
            st.success(f"✅ Resposta Correta! Alternativa {correct}) {q['options'][correct]}")
            st.session_state["answered_correctly"] = True
            mark_as_seen(exam_choice, q["domain"], q["subdomain"], q["id"])
        else:
            st.error(f"❌ Resposta Incorreta! Tente novamente.")
            st.session_state["answered_correctly"] = False

    # Exibir progresso do domínio
    seen = sum([
        1 for _q in questions
        if _q["id"] in set(progress.get(exam_choice, {}).get(_q["domain"], {}).get(_q["subdomain"], []))
    ])
    total = len(questions)
    pct = (seen / total * 100) if total else 0.0
    st.progress(pct / 100)
    st.markdown(f"### Progresso geral neste exame: `{pct:.1f}%`")

    # Botão para próxima questão (só aparece se acertar)
    if st.session_state["answered_correctly"]:
        if st.button("Próxima questão 🔁"):
            st.session_state["answered_correctly"] = False
            st.rerun()
else:
    st.info("Ainda não há questões disponíveis para este exame.")

st.write("---")
st.markdown("Feito com ❤️ para estudo profissional.")
