import tkinter as tk
from tkinter import messagebox
import random

jogadas = ["Pedra", "Papel", "Tesoura"]

def verificar_vencedor(jogada_jogador, jogada_computador):
    if jogada_jogador == jogada_computador:
        return "Empate!"
    elif (
        (jogada_jogador == "Pedra" and jogada_computador == "Tesoura") or
        (jogada_jogador == "Papel" and jogada_computador == "Pedra") or
        (jogada_jogador == "Tesoura" and jogada_computador == "Papel")
    ):
        return "Você venceu!"
    else:
        return "Você perdeu!"

def jogar(jogada_jogador):
    jogada_computador = random.choice(jogadas)
    resultado = verificar_vencedor(jogada_jogador, jogada_computador)
    messagebox.showinfo("Resultado", f"Você escolheu: {jogada_jogador}\nComputador escolheu: {jogada_computador}\n\n{resultado}")

window = tk.Tk()
window.title("Jokempo")

label = tk.Label(window, text="Escolha sua jogada:")
label.pack()

button_pedra = tk.Button(window, text="Pedra", command=lambda: jogar("Pedra"))
button_pedra.pack()

button_papel = tk.Button(window, text="Papel", command=lambda: jogar("Papel"))
button_papel.pack()

button_tesoura = tk.Button(window, text="Tesoura", command=lambda: jogar("Tesoura"))
button_tesoura.pack()

window.mainloop()
