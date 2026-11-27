# 🧠 Jogo da Memória em Python

![Badge Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Badge Tkinter](https://img.shields.io/badge/GUI-Tkinter-green?style=for-the-badge)
![Badge Status](https://img.shields.io/badge/Status-Concluído-brightgreen?style=for-the-badge)

## Índice

* [Descrição do Projeto](#-descrição-do-projeto)
* [Status do Projeto](#-status-do-projeto)
* [Funcionalidades](#-funcionalidades)
* [Demonstração da Interface](#-demonstração-da-interface)
* [Acesso e Execução do Projeto](#-acesso-e-execução-do-projeto)
* [Arquitetura e Lógica Aplicada](#-arquitetura-e-lógica-aplicada)
* [Uso Pedagógico e Sala de Aula](#-uso-pedagógico-e-sala-de-aula)
* [Tecnologias Utilizadas](#-tecnologias-utilizadas)
* [Autores e Créditos](#-autores-e-créditos)

---

## 📖 Descrição do Projeto

O **Jogo da Memória em Python** é uma aplicação desktop desenvolvida com foco em **lógica de programação, pensamento computacional e educação** para a disciplina de **Laboratório de Programação I** do curso de **Licenciatura em Informática (2026)**.

Utilizando exclusivamente bibliotecas nativas do Python (`tkinter` e `random`), o projeto dispensa a instalação de pacotes externos e arquivos de imagem, empregando caracteres Unicode (emojis) em um tabuleiro interativo `4x2` (8 cartas / 4 pares) com estética retrô estilo terminal.

---

## 🚀 Status do Projeto

✅ **Concluído** — Versão funcional pronta para uso em sala de aula, estudos de lógica de programação e demonstrações práticas.

*(Possíveis evoluções futuras incluem níveis de dificuldade com mais cartas, cronômetro, placar de recordes e efeitos sonoros de acerto e erro.)*

---

## ⚙️ Funcionalidades

* **Partida dinâmica a cada rodada:** Sorteio automático entre múltiplos conjuntos temáticos de emojis (Espaço, Animais, Natureza, Jogos, Comida e Fundo do Mar) e embaralhamento aleatório das 8 cartas.
* **Interface retrô estilo terminal:** Visual escuro (`black` e `green`) com fonte monoespaçada (`TkFixedFont`) e grid responsivo que se adapta ao redimensionamento da janela.
* **Modo Tela Cheia (`F11`):** Inicia em modo *fullscreen* por padrão e permite alternar entre janela e tela cheia pressionando a tecla `F11`.
* **Contador de tentativas em tempo real:** Atualiza o placar a cada par virado pelo jogador.
* **Feedback visual e bloqueio inteligente:** Pares corretos ficam destacados em verde e desabilitados; em caso de erro, o jogo bloqueia cliques acidentais por 1 segundo (`after`) antes de ocultar as cartas novamente.
* **Controles rápidos:** Botões para reiniciar imediatamente a partida com um novo tema (`Jogar Novamente`) ou encerrar o programa (`Fechar Jogo`).

---

## 🖥️ Demonstração da Interface

```text
                Encontre os pares iguais!
                  >>> Tentativas: 2 <<<

   +-----------+   +-----------+   +-----------+   +-----------+
   |     ?     |   |    🚀     |   |     ?     |   |    🪐     |
   +-----------+   +-----------+   +-----------+   +-----------+

   +-----------+   +-----------+   +-----------+   +-----------+
   |     ?     |   |     ?     |   |    🚀     |   |     ?     |
   +-----------+   +-----------+   +-----------+   +-----------+

              [ Jogar Novamente ]   [ Fechar Jogo ]
```

---

## 🛠️ Acesso e Execução do Projeto

### Pré-requisitos
* **Python 3** instalado na máquina (não requer `pip install`, pois utiliza apenas módulos nativos).
* Em sistemas Linux (Debian/Ubuntu), caso o módulo gráfico não esteja ativo por padrão, instale com:
  ```bash
  sudo apt install python3-tk
  ```

### Passo a passo para rodar
1. **Clone o repositório:**
   ```bash
   git clone https://github.com/Gabryel305/jogo-da-memoria-python.git
   ```
2. **Acesse a pasta do projeto:**
   ```bash
   cd jogo-da-memoria-python
   ```
3. **Execute o jogo:**
   ```bash
   python3 jogo-da-memoria.py
   ```

---

## 🧩 Arquitetura e Lógica Aplicada

O código foi estruturado de forma modular para demonstrar os quatro pilares do **Pensamento Computacional**:

* **Decomposição:** Divisão do problema em funções pequenas e específicas (`gerar_cartas`, `revelar_carta`, `verificar_par`, `verificar_vitoria` e `reiniciar_jogo`).
* **Reconhecimento de Padrões:** Uso de divisão inteira (`i // 4`) e módulo (`i % 4`) para mapear o índice linear das 8 cartas em coordenadas `(linha, coluna)` no tabuleiro.
* **Abstração:** Representação do estado completo do jogo por meio de listas (`cartas`, `botoes`) e variáveis de controle (`primeira_carta`, `segunda_carta`, `tentativas`, `verificando`).
* **Algoritmos e Eventos:** Uso de `command=lambda i=i: revelar_carta(i)` para vincular cada botão ao seu índice e agendamento assíncrono com `janela.after(1000, verificar_par)`.

---

## 🎓 Uso Pedagógico e Sala de Aula

Por rodar offline e em qualquer computador com Python, o projeto pode ser facilmente adaptado por docentes e estudantes:
* **Personalização de conteúdo:** Substituição dos emojis na lista `conjuntos_emojis` por pares disciplinares (ex.: *termo e definição*, *país e capital*, *elemento químico e símbolo*).
* **Gamificação:** Disputas amistosas em sala para revisão de conteúdos antes de avaliações, vencendo quem concluir o tabuleiro com o menor número de tentativas.

---

## 💻 Tecnologias Utilizadas

* **[Python 3](https://www.python.org/):** Linguagem principal do projeto.
* **[Tkinter](https://docs.python.org/3/library/tkinter.html):** Construção da janela (`Tk`), rótulos (`Label`), contêineres (`Frame`), botões (`Button`), posicionamento (`pack` / `grid`) e temporizador (`after`).
* **[Random](https://docs.python.org/3/library/random.html):** Sorteio de temas (`choice`) e embaralhamento das cartas (`shuffle`).

---

## 👥 Autores e Créditos

Projeto acadêmico desenvolvido no curso de **Licenciatura em Informática** — Disciplina de **Laboratório de Programação I** (2026).

* **Docente Orientadora:**
  * Profa. Caren Vanessa Pinheiro de Castro
* **Discentes Desenvolvedores:**
  * Agenor Kayke Bastos Silva Barros
  * Antônia Joiciane da Silva e Silva
  * Arthur Chagas de Aviz
  * Edielson Cauan Santos da Silva
  * [Gabryel Pinheiro Lima](https://github.com/Gabryel305) (`@Gabryel305`)
  * João Vitor Negrão Duarte
  * Luciana Paiva do Nascimento
  * Victor Alexandre Figueiredo Trindade
* **Ferramentas de Apoio:**
  * **Google Gemini** — Auxílio no refinamento da interface gráfica (`Tkinter`), atalhos de teclado e estruturação da documentação.
