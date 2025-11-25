import tkinter as tk
from tkinter import ttk, PhotoImage
import os
print(os.getcwd())

def centralizar_imagem(event):
    largura_janela = janela.winfo_width()
    altura_janela = janela.winfo_height()
    largura_imagem = imagem.width()
    altura_imagem = imagem.height()

    posicao_x = (largura_janela - largura_imagem) // 2
    posicao_y = (altura_janela - altura_imagem) // 2

    lbl_imagem.place(x=posicao_x, y=posicao_y)

janela = tk.Tk()
janela.title("Exibir imagem")
janela.geometry("400x250")

imagem = PhotoImage(file="pix.png")
lbl_imagem = ttk.Label(janela, image=imagem)

janela.bind("<Configure>", centralizar_imagem)

# Inicia em algum lugar (depois o centralizar_imagem ajusta)
lbl_imagem.place(x=0, y=0)

janela.mainloop()

