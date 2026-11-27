import tkinter as tk
from random import choice, shuffle

janela = tk.Tk()
janela.title("Jogo da Memória")
janela.geometry('800x600')
janela.config(bg='black')
janela.attributes("-fullscreen", True)

def alternar_tela_cheia(event=None):
    estado_atual = janela.attributes("-fullscreen")
    janela.attributes("-fullscreen", not estado_atual)

janela.bind("<F11>", alternar_tela_cheia)

# conjuntos de emojis
conjuntos_emojis = [
    ["🚀", "🪐", "🛸", "👽"],
    ["🐼", "🐯", "🦊", "🐻"],
    ["🍄", "🌿", "🦋", "🔮"],
    ["🎮", "🎲", "🏆", "💎"],
    ["🍕", "🍔", "🌮", "🍩"],
    ["🐙", "🦈", "🐢", "🐬"]
]

def gerar_cartas():
    cartas = choice(conjuntos_emojis) * 2
    shuffle(cartas)
    return cartas

cartas = gerar_cartas()

botoes = []
primeira_carta = None
segunda_carta = None
tentativas = 0
verificando = False

# status e contator
status_label = tk.Label(janela,
	text='Encontre os pares iguais!',
	fg='green',
	font=("TkFixedFont", 14, 'bold')
)
status_label.config(bg='black')
status_label.pack(pady=10)

tentativas_label = tk.Label(janela,
	text=">>> Tentativas: <<<",
	fg='green',
	font=("TkFixedFont", 12)
)
tentativas_label.config(bg='black')
tentativas_label.pack(pady=5)

# tabuleiro e sua configuração
tabuleiro = tk.Frame(janela)
tabuleiro.config(bg='Black')
tabuleiro.pack(expand=True, fill="both")

for i in range(4):
    tabuleiro.columnconfigure(i, weight=1)

for i in range(2):
    tabuleiro.rowconfigure(i, weight=1)

def reiniciar_jogo():
    global cartas, primeira_carta, segunda_carta, tentativas, verificando
	
    cartas = gerar_cartas()
    primeira_carta = None
    segunda_carta = None
    tentativas = 0
    verificando = False

    tentativas_label.config(text=">>> Tentativas: 0 <<<")
    status_label.config(text="Encontre os pares!")

    for botao in botoes:
        botao.config(text="?", bg="black", state="normal")

def verificar_vitoria():
    for botao in botoes:
        if botao["text"] == "?":
            return

    status_label.config(
        text=f"✧･ﾟ: *✧･ﾟ:* Parabéns! Você encontrou todos os pares em {tentativas} tentativas! *:･ﾟ✧*:･ﾟ✧",
        font=('TkFixedFont', 14, 'bold')
    )

def verificar_par():
    global primeira_carta, segunda_carta, verificando

    if cartas[primeira_carta] != cartas[segunda_carta]:
        botoes[primeira_carta].config(text="?")
        botoes[segunda_carta].config(text="?")
    else:
        botoes[primeira_carta].config(bg="green", state="disabled")
        botoes[segunda_carta].config(bg="green", state="disabled")

    primeira_carta = None
    segunda_carta = None
    verificando = False

    verificar_vitoria()

def revelar_carta(indice):
    global primeira_carta, segunda_carta, tentativas, verificando

    if verificando:
        return

    if botoes[indice]["text"] != "?":
        return

    botoes[indice]["text"] = cartas[indice]

    if primeira_carta is None:
        primeira_carta = indice

    elif segunda_carta is None and indice != primeira_carta:
        segunda_carta = indice
        tentativas += 1
        tentativas_label.config(text=f">>> Tentativas: {tentativas} <<<")
        verificando = True
        janela.after(1000, verificar_par)

# criar cartas no tabuleiro
for i in range(len(cartas)):
    botao = tk.Button(
        tabuleiro,
        text = "?",
        bg='black',
        fg='green',
        font = ("TkFixedFont", 32),
        command = lambda i = i: revelar_carta(i)
    )
    botao.grid(row = i // 4, column = i % 4, padx = 10, pady = 10, sticky = "nsew")
    botoes.append(botao)
    
# reiniciar ou acabar com tudo
frame_btn = tk.Frame(
	janela,
    bg='black'
)
frame_btn.pack(pady = 20)

botao_reiniciar = tk.Button(
    frame_btn,
    text="Jogar Novamente",
    fg='green',
    bg='black',
    font=("TkFixedFont", 12),
    command=reiniciar_jogo
)
botao_reiniciar.grid(row = 0, column = 0, pady = 20)

botao_fechar = tk.Button(
	frame_btn,
	text = "Fechar Jogo",
	fg='green',
	bg='black',
	font = ("TkFixedFont", 12),
	command = janela.destroy
)
botao_fechar.grid(row = 0, column = 1, padx = 10)

janela.mainloop()
