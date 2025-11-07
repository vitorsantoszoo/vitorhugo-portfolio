# 📚 Resolução de Problemas com Inteligência Artificial e Aprendizagem de Máquina

Esta disciplina faz parte da **Pós-Graduação em Inteligência Artificial e Aprendizagem de Máquina** e teve como foco o uso de técnicas de IA para resolver problemas reais, desde busca e otimização até redes neurais profundas.

---

## 🧠 Conteúdo estudado

Durante as aulas foram abordados conceitos fundamentais para compreensão e aplicação prática de IA em diferentes cenários, incluindo:

### **1) Representação e Resolução de Problemas com IA**
- Conceito de agente racional
- Função de agente e programa de agente
- Percepção, atuadores, sensores
- PEAS (Performance, Environment, Actuators, Sensors)
- Ambientes de tarefa e medidas de desempenho

### **2) Busca no Espaço de Estados**
- Definição de estados, ações, sucessores
- Estratégias de busca:
  - Largura
  - Profundidade
  - Heurística
  - Busca A*
  - Dijkstra
- Aplicações de busca em roteirização e tomada de decisão

### **3) Algoritmos Genéticos (AG)**
- Conceitos de Computação Evolutiva
- Representação de cromossomos, genes e alelos
- Seleção, crossover, mutação
- População e critério de parada
- Otimização de problemas reais com AG

### **4) Redes Neurais Artificiais (RNA)**
- Neurônio artificial e comparação com neurônio biológico
- Entradas, pesos, função soma e função de ativação
- Treinamento supervisionado e não supervisionado
- Perceptron: teoria, limitações e implementação
- Multi-Layer Perceptron (MLP) e Backpropagation
- Aplicações em classificação e regressão

### **5) Deep Learning e Visão Computacional**
- Redes Neurais Convolucionais (CNN)
- Camadas de Convolução, Pooling e Fully Connected
- YOLO: detecção, segmentação e classificação de objetos
- Aplicações em problemas reais (tempo real, imagens e vídeo)

### **6) Aplicações Reais Estudadas**
- Modelos neuro-fuzzy aplicados à previsão de internações por poluição
- Aplicação de IA em gestão de recursos hídricos e controle de barragens
- IA aplicada à sustentabilidade e impacto ambiental

---

## 📂 Projeto — Otimização de Rotas com Algoritmos de Busca

### Tema: Otimização de Rotas de Entrega para E-commerce com Algoritmos de Busca

**Problema:**  
Empresas de e-commerce enfrentam o desafio de otimizar rotas de entrega para múltiplos destinos, minimizando o tempo de viagem e o custo operacional. Trata-se de um problema clássico de otimização combinatória — que cresce em complexidade conforme o número de paradas aumenta.

**Técnica Utilizada:**  
Foram aplicados algoritmos de Busca no Espaço de Estados, com foco em **A\*** e **Dijkstra**.  
Esse conjunto de algoritmos está diretamente relacionado ao Problema do Caminho Mínimo (PCM), abordado na Aula 03.

A Busca A\* é especialmente interessante porque combina:

- custo real do caminho percorrido (g)
- estimativa heurística do custo restante (h)

→ buscando soluções ótimas de forma mais eficiente do que a busca por menor custo puro.

**Justificativa:**  
A otimização de rotas tem impacto direto em custo logístico, consumo de combustível e tempo de entrega — portanto sua aplicação gera ganho real de eficiência operacional.  
Esse exemplo conecta conceitos de IA ao contexto real de e-commerce e logística urbana, variando entre Caixeiro Viajante (TSP) e Problemas de Roteamento de Veículos (VRP).

### Arquivos do Projeto

| Entrega | Tipo | Arquivo |
|---|---|---|
| Apresentação Final — Otimização de Rotas com IA | PDF | [GRUPO_MODELAR TECH_PROJETO_RESOLUÇÃO DE PROBLEMAS EM IA-AM-CD.pdf](./GRUPO_MODELAR%20TECH_PROJETO_RESOLU%C3%87%C3%83O%20DE%20PROBLEMAS%20EM%20IA-AM-CD.pdf) |

---
