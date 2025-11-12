# Vision Agent — Analisador de Imagens

Este código executa um pipeline simples de **Visão Computacional**:
1. Lê uma imagem em formato RGB.
2. Converte para tons de cinza.
3. Aplica o método de limiarização automática de **Otsu**.
4. Identifica **componentes conectados** (objetos) na imagem.
5. Retorna o número total de objetos e as dimensões da imagem.
