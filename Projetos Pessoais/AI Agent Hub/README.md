# 🤖 AI Agent Hub - Sistema Modular de Inteligência Artificial com Visão, Predição e Linguagem Natural

## 🧭 Visão Geral

O AI Agent Hub é um sistema modular de Inteligência Artificial desenvolvido por mim, com o objetivo de integrar diferentes agentes autônomos cada um especializado em uma função distinta da IA moderna:

● 🖼️ Visão Computacional: percepção visual automatizada;

● 📈 Aprendizagem de Máquina Preditiva: raciocínio e previsão numérica;

● 💬 Linguagem Natural (NLG): comunicação e explicação dos resultados.

Este projeto foi desenvolvido como uma síntese prática e acadêmica de estudos em IA aplicada, simulando uma arquitetura real de AI Agents com comunicação entre módulos via logs JSON.

---

## 🧩 Arquitetura do Projeto

Cada notebook do repositório representa um agente autônomo, capaz de operar de forma independente ou integrada a outros.
O fluxo de dados e conhecimento segue uma lógica de pipeline inteligente:

```
🖼️ Vision Agent     ─┬─>  📊 Gera métricas e logs JSON
📈 Predictive Agent ─┘
                    ↓
💬 Language Agent lê os logs, interpreta e produz relatório final
```

---

## 📂 Estrutura de Diretórios

AI Agent Hub/


├── notebooks/
│   ├── vision_pipeline_heuristic.ipynb     # 🧮 Agente de Visão (OpenCV + Regras)
│   ├── vision_pipeline_cnn.ipynb           # 🤖 Agente de Visão (CNN - MobileNetV2)
│   ├── predictive_pipeline.ipynb           # 📈 Agente Preditivo (Regressão Linear)
│   └── language_pipeline.ipynb             # 💬 Agente de Linguagem (NLG baseado em regras)
│
├── data/
│   ├── images/                             # Imagens originais
│   ├── images_dataset/                     # Dataset estruturado (porcas/parafusos)
│   ├── models/                             # Modelos treinados (vision_cnn.pth)
│   ├── logs/                               # Logs JSON dos agentes
│   └── samples/                            # Saídas e relatórios finais
│
└── README.md                               # Este arquivo

---

## ⚙️ Descrição dos Agentes

🖼️ 1. Vision Agent (Heuristic & CNN)

Versão Heurística (vision_pipeline_heuristic.ipynb)
Baseada em OpenCV, realiza:

● Segmentação e contagem de objetos por contornos;

● Extração de características geométricas (área, circularidade, aspecto);

● Classificação por regras simples (porca vs parafuso).

Versão CNN (vision_pipeline_cnn.ipynb)
Versão aprimorada com aprendizado profundo (PyTorch + MobileNetV2):

● Treinamento leve (transfer learning);

● Dataset real de porcas e parafusos (images_dataset/);

● Gera métricas e salva modelo (vision_cnn.pth);

● Exporta log técnico em JSON para integração.

🧠 O agente de visão simula uma inspeção industrial automatizada.

---

## 📈 2. Predictive Agent (predictive_pipeline.ipynb)

Responsável por previsão numérica com base em aprendizado supervisionado.
Nesta versão MVP:

● Simula uma regressão linear;

● Analisa variáveis sintéticas;

● Calcula erro médio e gera relatório preditivo em JSON.

📊 O agente de predição representa o raciocínio quantitativo dentro do Hub.

---

## 💬 3. Language Agent (language_pipeline.ipynb)

Consolida os resultados de todos os agentes em linguagem natural (NLG):

● Lê automaticamente os arquivos JSON em data/logs/;

● Interpreta métricas e status;

● Gera um relatório técnico consolidado em texto e JSON.

🗒️ Exemplo de saída:

```
📊 Relatório Consolidado de IA — AI Agent Hub
--------------------------------------------------
🧩 vision_agent_cnn: o modelo MobileNetV2 apresentou excelente desempenho, com alta precisão e estabilidade.
🧩 predictive_agent: o modelo LinearRegression realizou previsões numéricas com resultados satisfatórios e erro médio controlado.
--------------------------------------------------
📅 Data UTC: 2025-11-12 18:47:53
💡 Análise geral: Os agentes operam de forma estável e coerente, com resultados consistentes para demonstração e evolução futura.
```

💡 Esse agente atua como o “cérebro explicativo” do sistema, convertendo dados técnicos em informação compreensível.

---

## 🧰 Tecnologias Utilizadas

| Categoria               | Tecnologias                            |
| ----------------------- | -------------------------------------- |
| Linguagem principal     | Python 3                               |
| Frameworks de IA        | PyTorch, OpenCV, Scikit-learn          |
| Bibliotecas científicas | NumPy, Pandas, Matplotlib              |
| Geração de linguagem    | Regras e templates (NLG)               |
| Ambiente de execução    | Google Colab (CPU)                     |
| Armazenamento           | Estrutura de diretórios local / GitHub |
| Documentação            | Markdown, JSON logs                    |

---

## 🚀 Como Executar o Projeto

1️⃣ Clonar o repositório

```
git clone https://github.com/<seu_usuario>/AI-Agent-Hub.git
cd AI-Agent-Hub
```

2️⃣ Abrir os notebooks no Google Colab

1. Abra Google Colab (https://colab.research.google.com/).

2. Faça upload dos notebooks da pasta notebooks/.

3. Execute célula por célula (CPU é suficiente)

3️⃣ Estrutura de execução recomendada

| Ordem | Notebook                          | Descrição                   |
| :---: | :-------------------------------- | :-------------------------- |
|  1️⃣  | `vision_pipeline_heuristic.ipynb` | Processamento visual básico |
|  2️⃣  | `vision_pipeline_cnn.ipynb`       | Treinamento do modelo CNN   |
|  3️⃣  | `predictive_pipeline.ipynb`       | Simulação preditiva         |
|  4️⃣  | `language_pipeline.ipynb`         | Geração do relatório final  |

---

## 📈 Resultados

✅ Modelos treinados: vision_cnn.pth

✅ Logs JSON: salvos em data/logs/

✅ Relatório final: disponível em data/samples/language_agent_report.txt

✅ Acurácia do modelo de visão (CNN): ~90%+

✅ Execução 100% em CPU (Colab)

---

## 🧩 Aplicabilidade

O AI Agent Hub pode ser expandido para:

🏭 Inspeção industrial automatizada

🚚 Otimização logística e preditiva

📋 Sistemas de relatórios inteligentes (NLG)

🧠 Simulação de agentes cognitivos autônomos

Este projeto serve como base modular para aplicações futuras que integrem percepção, raciocínio e linguagem, pilares fundamentais da Inteligência Artificial moderna.

---

## 🧑‍💻 Autor

Vitor Hugo
Desenvolvedor em formação e entusiasta de Inteligência Artificial
📘 Projeto desenvolvido como parte dos estudos em IA Aplicada e Aprendizagem de Máquina

### 📫 **Contato**
📧 E-mail: vitoor.hugoo@hotmail.com  
🔗 LinkedIn: [https://www.linkedin.com/in/vitor-hugo-3861391b8](#)  
💻 GitHub: [https://github.com/vitorsantoszoo](#)

---

## 🌱 Próximos Passos

 Adicionar salvamento de modelo preditivo (predictive_model.pkl)

 Automatizar pipeline via script unificado

 Criar interface web (Streamlit ou Flask)

 Expandir NLG para modelo generativo leve (DistilGPT-2)

 ---

 🧠 “Integrar visão, raciocínio e linguagem é o primeiro passo para uma IA realmente inteligente.”

 ---

 
