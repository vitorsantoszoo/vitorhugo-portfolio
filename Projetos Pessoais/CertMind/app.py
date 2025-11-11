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

core1_qbank = load_json("core1_questions_expanded.json")
core2_qbank = load_json("core2_questions_expanded.json")

# -------------------------------
# Selecionar exame / domínio / subdomínio
# -------------------------------
exam_choice = st.selectbox(
    "📌 Qual exame deseja estudar?",
    ["Core 1 (220-1201)", "Core 2 (220-1202)"]
)

qbank = core1_qbank if exam_choice == "Core 1 (220-1201)" else core2_qbank
questions = qbank["questions"]

# Coletar todos os domínios
domains = sorted(set(q["domain"] for q in questions))
domain_choice = st.selectbox("📂 Selecione um domínio:", domains)

# Filtrar subdomínios dentro o domínio
subdomains = sorted(set(q["subdomain"] for q in questions if q["domain"] == domain_choice))
subdomain_choice = st.selectbox("🧩 Selecione um subdomínio:", subdomains)

# Filtrar perguntas do subdomínio
filtered_questions = [q for q in questions if q["subdomain"] == subdomain_choice]

st.markdown(f"## 🎯 Modo Quiz — {domain_choice}")
progress = load_progress()

if filtered_questions:
    # Seleciona questão aleatória
    random.seed()  # garante chaves diferentes entre execuções
    q = random.choice(filtered_questions)

    st.markdown(f"### Subdomínio: **{q['subdomain']}**")
    st.write("---")
    st.markdown(f"**Pergunta:** {q['stem_md']}")

    # Gerar chave única de widget por questão + subdomínio + domínio
unique_key = f"radio_{exam_choice}_{domain_choice}_{subdomain_choice}_{q['id']}_{random.randint(1, 999999)}"

choice = st.radio(
    "Escolha a alternativa correta:",
    options=["A", "B", "C", "D"],
    format_func=lambda x: f"{x}) {q['options'][x]}",
    index=None,
    key=unique_key
)

# -------------------------------
# 🎯 Modo Quiz — com feedback completo
# -------------------------------
if filtered_questions:
    # Seleciona questão aleatória
    q = random.choice(filtered_questions)

    st.markdown(f"### Subdomínio: **{q['subdomain']}**")
    st.write("---")
    st.markdown(f"**Pergunta:** {q['stem_md']}")

    # Exibir alternativas
    choice = st.radio(
        "Escolha a alternativa correta:",
        options=["A", "B", "C", "D"],
        format_func=lambda x: f"{x}) {q['options'][x]}",
        index=None,
        key=f"choice_{q['id']}"
    )

    correct = q["answer"]

    # -------------------------------
    # Estado de sessão corrigido
    # -------------------------------
    if "answered_correctly" not in st.session_state:
        st.session_state["answered_correctly"] = False
    if "last_question_id" not in st.session_state:
        st.session_state["last_question_id"] = None

    # Resetar estado se for nova questão
    if st.session_state["last_question_id"] != q["id"]:
        st.session_state["answered_correctly"] = False
        st.session_state["last_question_id"] = q["id"]

    # -------------------------------
    # Botão de resposta com feedback
    # -------------------------------
    if st.button("Responder"):
        if choice is None:
            st.warning("⚠️ Escolha uma alternativa antes de responder.")
        elif choice == correct:
            st.success(f"✅ Resposta Correta! Alternativa {correct}) {q['options'][correct]}")
            st.session_state["answered_correctly"] = True
            mark_as_seen(exam_choice, q["domain"], q["subdomain"], q["id"])
        else:
            st.error(f"❌ Resposta Incorreta! A alternativa {choice}) não é a correta. Tente novamente.")
            st.session_state["answered_correctly"] = False

    # -------------------------------
    # Mostrar botão “Próxima questão” apenas se acertar
    # -------------------------------
    if st.session_state["answered_correctly"]:
        if st.button("Próxima questão 🔁"):
            st.session_state["answered_correctly"] = False
            st.rerun()

    # -------------------------------
    # Barra de progresso do domínio
    # -------------------------------
    seen = sum([
        1 for _q in questions
        if _q["id"] in set(progress.get(exam_choice, {}).get(_q["domain"], {}).get(_q["subdomain"], []))
    ])
    total = len(questions)
    pct = (seen / total * 100) if total else 0.0
    st.progress(pct / 100)
    st.markdown(f"### Progresso geral neste exame: `{pct:.1f}%`")

else:
    st.info("Ainda não há questões disponíveis para este subdomínio.")

st.write("---")
st.markdown("Feito com ❤️ para estudo profissional.")


st.write("---")
st.markdown("Feito com ❤️ para estudo profissional.")
