import json
import os
import random
import time
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
# Seleção de exame / domínio / subdomínio
# -------------------------------
exam_choice = st.selectbox(
    "📌 Qual exame deseja estudar?",
    ["Core 1 (220-1201)", "Core 2 (220-1202)"],
    key="exam_select"
)

qbank = core1_qbank if exam_choice == "Core 1 (220-1201)" else core2_qbank
questions = qbank["questions"]

domains = sorted(set(q["domain"] for q in questions))
domain_choice = st.selectbox("📂 Selecione um domínio:", domains, key="domain_select")

subdomains = sorted(set(q["subdomain"] for q in questions if q["domain"] == domain_choice))
subdomain_choice = st.selectbox("🧩 Selecione um subdomínio:", subdomains, key="subdomain_select")

# 🔒 Evitar texto digitável inválido no selectbox
if subdomain_choice not in subdomains:
    subdomain_choice = subdomains[0]

# -------------------------------
# Reset de estado ao mudar domínio/subdomínio
# -------------------------------
if "last_domain" not in st.session_state or "last_subdomain" not in st.session_state:
    st.session_state["last_domain"] = None
    st.session_state["last_subdomain"] = None

if (st.session_state["last_domain"] != domain_choice) or (st.session_state["last_subdomain"] != subdomain_choice):
    st.session_state["current_question"] = None
    st.session_state["answered_correctly"] = False
    st.session_state["last_domain"] = domain_choice
    st.session_state["last_subdomain"] = subdomain_choice

filtered_questions = [q for q in questions if q["subdomain"] == subdomain_choice]

# 🔄 Se houver mais de 10, sorteia 10 diferentes
if len(filtered_questions) > 10:
    filtered_questions = random.sample(filtered_questions, 10)

st.markdown(f"## 🎯 Modo Quiz — {domain_choice}")
progress = load_progress()

# -------------------------------
# Estado do Quiz
# -------------------------------
if "current_question" not in st.session_state:
    st.session_state["current_question"] = None
if "answered_correctly" not in st.session_state:
    st.session_state["answered_correctly"] = False

# Selecionar nova questão se nenhuma estiver ativa
if st.session_state["current_question"] is None and filtered_questions:
    st.session_state["current_question"] = random.choice(filtered_questions)
    st.session_state["answered_correctly"] = False

q = st.session_state["current_question"]

# -------------------------------
# Interface do Quiz
# -------------------------------
if not filtered_questions:
    st.info("Ainda não há questões disponíveis para este subdomínio.")
else:
    st.markdown(f"### Subdomínio: **{q['subdomain']}**")
    st.write("---")
    st.markdown(f"**Pergunta:** {q['stem_md']}")

    # 🎲 Embaralhar opções (sem alterar a correta)
    options_shuffled = list(q["options"].items())
    random.shuffle(options_shuffled)

    # Mapeamento para saber qual é a resposta correta
    answer_map = {opt: key for key, opt in q["options"].items()}
    correct_answer_text = q["options"][q["answer"]]

    # Exibir opções
    choice_text = st.radio(
        "Escolha a alternativa correta:",
        options=[opt for _, opt in options_shuffled],
        index=None,
        key=f"choice_{q['id']}"
    )

    # Verificação de resposta
    if st.button("Responder"):
        if choice_text is None:
            st.warning("⚠️ Você precisa escolher uma alternativa antes de responder.")
        elif choice_text == correct_answer_text:
            st.success("✅ Resposta Correta!")
            st.session_state["answered_correctly"] = True
            mark_as_seen(exam_choice, domain_choice, subdomain_choice, q["id"])
            time.sleep(1)
            # Pular automaticamente
            st.session_state["current_question"] = random.choice(filtered_questions)
            st.session_state["answered_correctly"] = False
            st.rerun()
        else:
            st.error("❌ Resposta Incorreta! Tente novamente.")

    # Barra de progresso
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
