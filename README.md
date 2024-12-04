# Autômatos Celulares e Estudos em Modelagem Matemático-Computacional Aplicada à Epidemiologia
Repositório destinado aos meus estudos, códigos, simulações e experimentos relacionados à disciplina de Modelagem Matemático-Computacional para Epidemiologia Computacional na UFRPE. Este espaço é dedicado a registrar o aprendizado e compartilhar ferramentas, conceitos e implementações de Autômatos Celulares (Cellular Automata - CA) e outros tópicos da área.

--- 

## **Índice**
- [Visão Geral](#visão-geral)
- [Estrutura do Repositório](#estrutura-do-repositório)
- [Pré-requisitos e Configuração](#pré-requisitos-e-configuração)
- [Exemplos e Projetos](#exemplos-e-projetos)
- [Referências e Recursos](#referências-e-recursos)

---

## **Visão Geral**
Este repositório contém:
- Implementações de **Autômatos Celulares** com foco em aplicações em fenômenos naturais e sociais.
- Simulações relacionadas a modelos como o *Game of Life* e outros autômatos unidimensionais e bidimensionais.
- Experimentos ligados ao estudo de complexidade, ordem, e auto-organização em sistemas computacionais.
- Anotações e materiais de estudo relacionados ao livro **Cellular Automata** de Joel Schif e outras referências importantes.

---

## **Estrutura do Repositório**
A organização do repositório segue uma estrutura modular para facilitar o acesso e o uso dos conteúdos:

```plaintext
📂 /src
    ├── game_of_life.py          # Implementação do Game of Life
    ├── elementary_ca.py         # Autômatos celulares elementares (Regra 110, etc.)
    ├── epidemiology_model.py    # Modelos epidemiológicos baseados em autômatos celulares
    └── utils.py                 # Funções auxiliares para visualização e análise

📂 /notes
    ├── ca_intro.md           # Introdução aos autômatos celulares
    ├── wolfram_classes.md    # Classes de comportamento dos autômatos celulares de Wolfram
    └── epidemics.md          # Simulações de propagação de doenças

📂 /examples
    ├── langtons_ant             # Exemplo da formiga de Langton (Capítulo 6 do livro)
    └── ulam_spiral              # Experimentos com a Espiral de Ulam

📂 /docs
    ├── SUMMARY.md               # Resumo do aprendizado e anotações
    ├── INSTALL.md               # Guia de instalação e execução dos scripts
    └── FAQ.md                   # Respostas às perguntas frequentes

📂 /images
    ├── ca_simulation.gif        # GIFs de simulações
    └── ulam_visualization.png   # Visualização da espiral de Ulam
```

## Pré-requisitos e Configuração
Para executar os scripts e notebooks deste repositório, você precisará de"
- Python 3.8+
- Bibliotecas recomendadas:
    - numpy para manipulação de matrizes.
    - matplotlib e seaborn para visualização.

### Passos para Configuração
1. Clone este repositório:
    ```bash
    git clone https://github.com/notsogreatdavi/cellular-automata.git
    cd cellular-automata
    ```

2. Instale as depend6encia com o pip:
   ```bash
   pip install -r requirements.txt
    ```
--- 

## Exemplos e Projetos
Aqui estão alguns exemplos e projetos que você encontrará neste repositório:

### 1. Game of Life
Uma implementação clássica do autômato celular bidimensional proposto por John Conway. Veja o notebook ou execute o script para observar a evolução do padrão com base nas regras locais.

### 2. Regra 110
Uma simulação de um autômato celular unidimensional que demonstra comportamento caótico e foi provado ser Turing-completo.

### 3. Modelos Epidemiológicos
Simulações de propagação de doenças utilizando autômatos celulares. Explore o impacto de diferentes variáveis como taxa de transmissão, quarentena, e vacinação.

### 4. Formiga de Langton
Um exemplo fascinante de como regras simples podem levar à complexidade. O comportamento emergente é explorado no contexto de sistemas auto-organizáveis.

 ## Referências e Recursos
 - Joel Schif, Cellular Automata (livro base para muitos dos exemplos deste repositório.
 - Stephen Wolfram, A New Kind of Science.
 - MCell - Simulador de autômatos celulares.
