# 🤖 APRENDIZAGEM DE MÁQUINA E VISÃO COMPUTACIONAL

Esta disciplina faz parte da **Pós-Graduação em Inteligência Artificial e Aprendizagem de Máquina** e abrangeu conceitos fundamentais de Processamento de Imagens Digitais, Visão Computacional e técnicas supervisionadas de Machine Learning aplicadas ao reconhecimento de padrões em imagens.

---

## 🧠 Conteúdos estudados na disciplina

### Visão Computacional (VC)
- Introdução ao Processamento de Imagens Digitais
- Representação de imagens (RGB, níveis de cinza, binária)
- Modelos matemáticos de imagens (função 2D f(x,y))
- Amostragem, quantização e resolução
- Estrutura de arquivos de imagem (ex.: BMP)
- Manipulação de pixels e espaço de cor
- Conversão de imagens (RGB → cinza, cinza → binária)
- Limiarização manual e automática (incluindo **método de Otsu**)
- Vizinhança de pixels (4 e 8 conexos)
- Componentes conexos com `connectedComponentsWithStats`
- Extração de objetos de interesse a partir da segmentação

### Realce e Filtragem de Imagens
- Histograma de imagens e interpretação
- Ajuste de contraste e brilho
- Operações de potência / gamma correction
- Negativo da imagem
- Filtros espaciais (máscaras / kernels)
  - Filtro média (passa-baixa)
  - Filtro mediana
  - Filtro passa-alta para realce de bordas

### Aprendizagem de Máquina para Imagens
- Reconhecimento de padrões em imagens
- Diferença entre métodos tradicionais e Deep Learning
- Introdução às **Redes Neurais Convolucionais (CNNs)**
- Uso de convolução em modelos neurais
- Aplicações em inspeção visual automática

---

## 🧩 Projeto desenvolvido nesta disciplina (Visão Computacional)

| Projeto | Descrição |
|--------|----------|
| ## 🧩 Projeto 1 — Inspeção Visual Automática [Sistema de Inspeção Visual Automática](./Sistema%20de%20Inspe%C3%A7%C3%A3o%20Visual.pdf) | Sistema de visão computacional criado para identificar, segmentar e contar parafusos e porcas em imagens industriais, classificando conjuntos aprovados ou reprovados. |

### Código do Projeto (Notebook)

| Arquivo | Conteúdo |
|--------|----------|
| [Atividade_Visão_Comp.ipynb](./Atividade_Vis%C3%A3o_Comp.ipynb) | Implementação do pipeline de visão: conversão, binarização, morfologia, extração de componentes e contagem final. |


Imagem → Pré-processamento → Binarização → Componentes Conectados → Classificação

---

## Observação

Este projeto **é prático** — diferentemente de outros módulos da pós onde houve apenas pesquisa conceitual.

Aqui foi implementado e executado um pipeline completo de visão computacional usando Python + OpenCV.

---

## 🧠 Aprendizagem de Máquina (Machine Learning) — Conteúdo estudado

Na sequência da mesma disciplina, avançamos para a parte de Aprendizagem de Máquina e Redes Neurais, aprofundando o trabalho com modelos supervisionados para classificação e regressão.

Grande parte das atividades foi desenvolvida em Python utilizando Jupyter / Google Colab, aplicando bibliotecas de Deep Learning como **PyTorch**, **scikit-learn** e **TensorFlow**.

### Temas estudados nesta etapa:

- Conceitos de redes neurais artificiais
- Neurônios, pesos, bias e funções de ativação
- Backpropagation e atualização de pesos
- Funções de custo para classificação e regressão
- Otimização com Adam e SGD
- Normalização e preparação de dados para treino
- Separação de datasets em treino / teste
- Redes Neurais com PyTorch:
  - Tensores, Autograd, gradientes
  - Construção de modelos `nn.Module`
  - treino e avaliação de modelo
- Redes neurais com scikit-learn
- Redes Neurais Convolucionais (CNN) — passo a passo
  - convolução
  - pooling
  - máscaras
  - forward/backward
- Transfer Learning (ex. VGG16)
- Aplicações em visão computacional e classificação de imagens

---

## 📂 Projetos e Atividades — Aprendizagem de Máquina

| Projeto / Atividade | Arquivo | Descrição |
|--------------------|---------|-----------|
| ## 🧠 Projeto 2 — Detecção de Pedestres com CNN (PyTorch) | [Atividade_CNN_Pedestres.ipynb](./Atividade_CNN_Pedestres.ipynb) | Implementação de uma rede neural convolucional para classificar imagens entre “pedestre” e “não pedestre”, utilizando PyTorch |
| Solução de Detecção de Pedestres com TensorFlow | [Atividade_Solucao_Deteccao_pedestre_Usando_Redes_Neurais_Tensorflow.ipynb](./Atividade_Solucao_Deteccao_pedestre_Usando_Redes_Neurais_Tensorflow.ipynb) | Construção da mesma solução utilizando TensorFlow, comparando desempenho entre frameworks |

Dataset → Conv → Pool → Dense → Output (Pedestre / Não-Pedestre)

---

**Resumo dos resultados:**  
A CNN alcançou 92% de acurácia na classificação de pedestres, com melhoria perceptível após ajuste de taxa de aprendizado e aumento do dataset.

---
