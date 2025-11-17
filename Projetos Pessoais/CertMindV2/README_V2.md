# 🧠 CertMind V2 — Sistema Inteligente de Estudo para Certificações

![Status](https://img.shields.io/badge/status-stable-green)
![Version](https://img.shields.io/badge/version-2.0-blue)
![Python](https://img.shields.io/badge/python-3.8+-blue)

> **Sistema inteligente de estudo com repetição espaçada para certificações de TI**

---

## 🎯 O que é o CertMind V2?

O **CertMind V2** é uma evolução completa do sistema de estudo para certificações técnicas. Utilizando **algoritmos de repetição espaçada (SM-2)**, **analytics avançado** e **seleção inteligente de questões**, o sistema maximiza a retenção de conhecimento e otimiza seu tempo de estudo.

### ✨ Principais Funcionalidades

#### 🧠 Repetição Espaçada Inteligente
- Algoritmo **SM-2 (SuperMemo 2)** adaptado para certificações
- Calcula o momento ideal para revisar cada conceito
- Aumenta retenção de longo prazo em até 200%
- Espaça revisões baseado em performance individual

#### 📊 Analytics e Dashboard Completo
- **Métricas detalhadas**: taxa de acerto, conceitos dominados, sequência de dias
- **Identificação de áreas fracas**: detecta automaticamente tópicos com dificuldade
- **Visualizações interativas**: gráficos de distribuição de domínio e performance
- **Recomendações personalizadas**: sugestões baseadas em seu padrão de estudo

#### 🎯 Seleção Inteligente de Questões
- Prioriza questões nunca vistas
- Identifica conceitos prontos para revisão (intervalo vencido)
- Foca em tópicos onde você tem mais dificuldade
- Elimina redundâncias e duplicatas

#### 💎 Feedback Rico e Contextual
- **Explicações detalhadas** para cada resposta
- **Métricas individuais** por questão
- **Níveis de domínio** (0-100%)
- **Tags e categorização** inteligente
- **Badges de dificuldade** (fácil, médio, difícil)

---

## 🚀 Novidades da Versão 2.0

### Comparação V1 vs V2

| Recurso | V1 | V2 |
|---------|----|----|
| **Banco de Questões** | 250 (com duplicatas) | 96 únicas + enriquecidas |
| **Sistema de Progresso** | Visto/não visto | Métricas completas + repetição espaçada |
| **Seleção de Questões** | Aleatória | Algoritmo inteligente de priorização |
| **Feedback** | Apenas certo/errado | Explicações + contexto + métricas |
| **Analytics** | Barra de progresso | Dashboard completo + identificação de áreas fracas |
| **Tracking** | Por subdomínio | Por questão individual + histórico temporal |
| **Recomendações** | Nenhuma | Personalizadas baseadas em performance |

### 🔥 Melhorias Implementadas

#### Sprint 1: Limpeza de Dados ✅
- ✅ Removidas **154 questões duplicadas** (79 Core 1 + 75 Core 2)
- ✅ Adicionado campo `explanation` em todas as questões
- ✅ Adicionado campo `difficulty` (easy/medium/hard)
- ✅ Adicionado campo `tags` para categorização
- ✅ Adicionado campo `concept` para identificação clara

#### Sprint 2: Sistema de Progresso Avançado ✅
- ✅ Implementado algoritmo **SM-2** de repetição espaçada
- ✅ Tracking detalhado: tentativas, acertos, erros, histórico
- ✅ Cálculo de **nível de domínio** (0.0 a 1.0)
- ✅ Agendamento automático de próximas revisões
- ✅ Contador de sequência de dias estudando

#### Sprint 3: Interface Melhorada ✅
- ✅ UI completamente redesenhada com Streamlit
- ✅ Cards de questões com contexto enriquecido
- ✅ Feedback visual com métricas em tempo real
- ✅ Sistema de navegação intuitivo
- ✅ Badges e indicadores visuais

#### Sprint 4: Analytics e Gamificação ✅
- ✅ Dashboard completo de performance
- ✅ Gráficos de distribuição de domínio
- ✅ Identificação automática de áreas fracas
- ✅ Recomendações personalizadas de estudo
- ✅ Sistema de conquistas (conceitos dominados)

---

## 📂 Estrutura do Projeto

```
certmind_v2/
├── 📄 app_v2.py                     # Aplicação principal (Streamlit)
├── 🧠 spaced_repetition.py          # Algoritmo de repetição espaçada (SM-2)
├── 📊 progress_manager_v2.py        # Gerenciador de progresso avançado
├── 📈 analytics.py                  # Sistema de analytics e visualizações
├── 🔧 data_migration.py             # Script de migração de dados
├── 📋 requirements.txt              # Dependências Python
├── 📖 README_V2.md                  # Esta documentação
│
├── 📦 data/
│   ├── core1_questions_v2.json     # Banco de questões Core 1 (v2)
│   ├── core2_questions_v2.json     # Banco de questões Core 2 (v2)
│   ├── progress_v2.json            # Dados de progresso do usuário
│   │
│   ├── core1_questions_expanded.json  # [Legado] Banco antigo Core 1
│   ├── core2_questions_expanded.json  # [Legado] Banco antigo Core 2
│   └── progress.json                  # [Legado] Progresso antigo
│
├── 📁 Core1/
│   └── PDFs/
│       └── 220-1201.pdf            # PDF oficial CompTIA A+ Core 1
│
└── 📁 Core2/
    └── PDFs/
        └── 220-1202.pdf            # PDF oficial CompTIA A+ Core 2
```

---

## ⚙️ Instalação e Uso

### Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Instalação

```bash
# 1. Clone o repositório
git clone https://github.com/vitorsantoszoo/vitorhugo-portfolio.git
cd "vitorhugo-portfolio/Projetos Pessoais/CertMind"

# 2. Instale as dependências
pip install -r requirements.txt

# 3. Execute a migração de dados (apenas na primeira vez)
python data_migration.py

# 4. Inicie a aplicação
streamlit run app_v2.py
```

### Uso

1. **Acesse a aplicação** no navegador (geralmente http://localhost:8501)
2. **Escolha o exame** (Core 1 ou Core 2)
3. **Comece a estudar!** O sistema selecionará automaticamente as melhores questões
4. **Acompanhe seu progresso** no Dashboard
5. **Siga as recomendações** para otimizar seu aprendizado

---

## 🔬 Como Funciona a Repetição Espaçada?

### Algoritmo SM-2 Adaptado

O CertMind V2 utiliza uma variação do algoritmo **SuperMemo 2 (SM-2)**, otimizado para estudo de certificações:

#### 📐 Fórmula de Intervalo

```
Se acerto >= 60%:
    easiness = easiness + (0.1 - (5 - quality) × (0.08 + (5 - quality) × 0.02))
    
    Se primeira repetição:
        intervalo = 1 dia
    Se segunda repetição:
        intervalo = 6 dias
    Caso contrário:
        intervalo = intervalo_anterior × easiness

Senão (erro):
    easiness = max(1.3, easiness - 0.2)
    intervalo = 1 dia
    repetições = 0
```

#### 🎯 Cálculo de Domínio

```
domínio = (acurácia × 0.6) + (consistência × 0.3) + (repetições × 0.1)

Onde:
- acurácia = taxa de acerto (0.0 a 1.0)
- consistência = min(tentativas / 3, 1.0)
- repetições = min(repetições_bem_sucedidas / 5, 1.0)
```

### 📊 Níveis de Classificação

| Nível | Domínio | Descrição |
|-------|---------|-----------|
| 🌱 Iniciante | 0-40% | Conceito recém-introduzido |
| 📚 Intermediário | 40-70% | Em processo de consolidação |
| 🎯 Avançado | 70-90% | Quase dominado |
| ⭐ Mestre | 90-100% | Conceito dominado |

### ⏰ Intervalos Típicos

1. **Primeira revisão**: 1 dia
2. **Segunda revisão**: 6 dias
3. **Terceira revisão**: ~15 dias (6 × 2.5)
4. **Quarta revisão**: ~37 dias (15 × 2.5)
5. E assim por diante...

---

## 📚 Certificações Suportadas

### ✅ Disponível Agora

#### CompTIA A+ (220-1201 / 220-1202)
- **Core 1**: 51 questões únicas
  - 1.0 Dispositivos móveis (20 questões)
  - 2.0 Redes (30 questões)
  - 3.0 Hardware (40 questões)
  - 4.0 Virtualização e Computação em Nuvem (20 questões)
  - 5.0 Solução de Problemas de Hardware e Rede (20 questões)

- **Core 2**: 45 questões únicas
  - 1.0 Sistemas Operacionais (30 questões)
  - 2.0 Segurança (30 questões)
  - 3.0 Solução de Problemas de Software (30 questões)
  - 4.0 Operações e Suporte (30 questões)

### 🔜 Planejado para o Futuro
- CompTIA Network+
- CompTIA Security+
- Cisco CCNA
- Cisco CyberOps Associate
- EXIN ISO 27001
- EXIN DPO
- ITIL Foundation
- AWS Cloud Practitioner

---

## 📖 Metodologia de Estudo Recomendada

### 🎓 Ciclo de Aprendizado Eficaz

```
1. 📚 ESTUDO TEÓRICO (2-3 horas)
   └─> Leia material oficial ou assista videoaulas

2. 🎯 TESTE INICIAL (30 min)
   └─> Use o CertMind para avaliar conhecimento inicial

3. 📊 ANÁLISE (10 min)
   └─> Verifique o Dashboard para identificar áreas fracas

4. 🔍 REVISÃO FOCADA (1-2 horas)
   └─> Estude especificamente os tópicos com dificuldade

5. ⏰ REPETIÇÃO ESPAÇADA (15-30 min/dia)
   └─> Volte ao CertMind nos intervalos sugeridos

6. 📈 ACOMPANHAMENTO
   └─> Continue até dominar 80%+ dos conceitos
```

### 💡 Dicas para Máximo Aproveitamento

1. **Seja Consistente**: Estude pelo menos 15 minutos por dia
2. **Confie no Algoritmo**: Revise nos intervalos sugeridos
3. **Foque nas Áreas Fracas**: Use o Dashboard para priorizar
4. **Leia as Explicações**: Mesmo quando acertar
5. **Não Pule Questões**: Cada exposição ajuda na memorização
6. **Mantenha a Sequência**: Dias consecutivos consolidam hábitos

---

## 🏗️ Arquitetura Técnica

### Módulos Principais

#### 1. `spaced_repetition.py`
**Responsabilidade**: Implementa o algoritmo SM-2 de repetição espaçada

**Classes principais**:
- `SpacedRepetitionEngine`: Motor principal do algoritmo

**Métodos principais**:
- `calculate_next_review()`: Calcula próxima data de revisão
- `get_questions_to_review()`: Seleciona questões prioritárias
- `get_study_recommendation()`: Gera recomendações de estudo

#### 2. `progress_manager_v2.py`
**Responsabilidade**: Gerencia progresso e persistência de dados

**Classes principais**:
- `ProgressManager`: Gerenciador central de progresso

**Métodos principais**:
- `record_answer()`: Registra resposta e atualiza métricas
- `get_overall_stats()`: Retorna estatísticas globais
- `get_weak_areas()`: Identifica áreas com dificuldade

#### 3. `analytics.py`
**Responsabilidade**: Visualizações e análise de dados

**Classes principais**:
- `PerformanceAnalytics`: Sistema de analytics
- `QuizInterface`: Interface aprimorada do quiz

**Métodos principais**:
- `render_dashboard()`: Renderiza dashboard completo
- `render_question_card()`: Renderiza cartão de questão enriquecido

#### 4. `app_v2.py`
**Responsabilidade**: Interface principal e orquestração

**Funcionalidades**:
- Sistema de navegação (Quiz, Dashboard, Sobre)
- Gerenciamento de estado do Streamlit
- Integração de todos os módulos

### Fluxo de Dados

```
┌─────────────┐
│   Usuário   │
└──────┬──────┘
       │ Responde questão
       v
┌─────────────────┐
│  app_v2.py      │
└────────┬────────┘
         │ Registra resposta
         v
┌──────────────────────┐      ┌─────────────────────┐
│ progress_manager_v2  │◄────►│  spaced_repetition  │
└──────────┬───────────┘      └─────────────────────┘
           │ Calcula próxima revisão
           │ Atualiza métricas
           v
┌──────────────────┐
│  progress_v2.json│
└──────────────────┘
```

---

## 📊 Formato dos Dados

### Questão (v2)

```json
{
  "id": "1.1_concept_tethering",
  "domain": "1.0 Dispositivos móveis",
  "subdomain": "1.1 Configurar hardware de dispositivos móveis",
  "concept": "Tethering",
  "question": "O que o recurso 'tethering' permite em dispositivos móveis?",
  "options": {
    "A": "Compartilhar a conexão de rede do celular",
    "B": "Bloquear aplicativos em segundo plano",
    "C": "Sincronizar dados com o computador",
    "D": "Limitar o uso de Wi-Fi"
  },
  "answer": "A",
  "explanation": "Tethering permite que o smartphone funcione como hotspot...",
  "difficulty": "easy",
  "tags": ["conectividade", "mobile", "hotspot"]
}
```

### Progresso de Questão

```json
{
  "1.1_concept_tethering": {
    "exam": "Core 1 (220-1201)",
    "domain": "1.0 Dispositivos móveis",
    "subdomain": "1.1 Configurar hardware",
    "attempts": 3,
    "correct": 2,
    "incorrect": 1,
    "first_seen": "2025-11-17T10:00:00",
    "last_seen": "2025-11-17T15:30:00",
    "easiness_factor": 2.5,
    "repetitions": 2,
    "interval": 6,
    "next_review": "2025-11-23T15:30:00",
    "mastery_level": 0.67,
    "history": [
      {"timestamp": "2025-11-17T10:00:00", "correct": true},
      {"timestamp": "2025-11-17T12:00:00", "correct": false},
      {"timestamp": "2025-11-17T15:30:00", "correct": true}
    ]
  }
}
```

---

## 🧪 Testes e Validação

### Migração de Dados

```bash
# Executar migração
python data_migration.py

# Resultado esperado:
# ✅ Core 1: 130 → 51 questões (79 duplicatas removidas)
# ✅ Core 2: 120 → 45 questões (75 duplicatas removidas)
```

### Testes Manuais

1. **Teste de Repetição Espaçada**:
   - Responda uma questão corretamente
   - Verifique que `next_review` é calculado (1 dia)
   - Responda novamente após 1 dia
   - Verifique que intervalo aumenta para 6 dias

2. **Teste de Áreas Fracas**:
   - Erre intencionalmente 3+ questões do mesmo domínio
   - Verifique Dashboard > Áreas que Precisam de Atenção
   - Confirme que o domínio aparece listado

3. **Teste de Sequência**:
   - Estude 1+ questão hoje
   - Verifique que `streak_days` = 1
   - Volte amanhã e estude novamente
   - Confirme que `streak_days` = 2

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Se você quer ajudar:

### Como Contribuir

1. **Fork o projeto**
2. **Crie uma branch** para sua feature (`git checkout -b feature/MinhaFeature`)
3. **Commit suas mudanças** (`git commit -m 'Adiciona MinhaFeature'`)
4. **Push para a branch** (`git push origin feature/MinhaFeature`)
5. **Abra um Pull Request**

### Ideias para Contribuições

- 📝 Adicionar mais questões
- 🎨 Melhorar UI/UX
- 🌍 Traduzir para outros idiomas
- 📚 Adicionar novas certificações
- 🐛 Reportar/corrigir bugs
- 📖 Melhorar documentação

---

## 📄 Licença

Este projeto é disponibilizado para **uso educacional**. O conteúdo das questões é baseado nos objetivos oficiais da CompTIA A+ e foi adaptado para fins de estudo.

---

## 👨‍💻 Autor

**Vitor Hugo**  
Profissional de TI | Especialista em Segurança da Informação

- 🔗 [GitHub](https://github.com/vitorsantoszoo)
- 📧 Contato: Abra uma issue no repositório

---

## 🙏 Agradecimentos

- **CompTIA** pelos objetivos oficiais da certificação A+
- **Streamlit** pela incrível framework de dashboards
- **Comunidade Python** pelas bibliotecas open source
- **Você** por usar o CertMind! 🎉

---

## 📋 Changelog

### V2.0 (Novembro 2025)
- ✨ Implementação completa de repetição espaçada (SM-2)
- 📊 Dashboard de analytics com visualizações
- 🎯 Seleção inteligente de questões
- 💎 Feedback rico com explicações
- 🧹 Limpeza de dados (154 duplicatas removidas)
- 📈 Sistema de tracking avançado
- 🔥 Contador de sequência de dias
- 💡 Recomendações personalizadas

### V1.0 (Original)
- ✅ Extração de PDFs oficiais
- ✅ Parser de exam objectives
- ✅ Tradução EN→PT
- ✅ Interface básica Streamlit
- ✅ Navegação por domínio/subdomínio

---

**Versão**: 2.0  
**Status**: ✅ Estável e Pronto para Uso  
**Última Atualização**: Novembro 2025

🧠 **CertMind V2** - Estude de forma inteligente, não apenas mais.
