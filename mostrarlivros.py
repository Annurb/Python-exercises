import tkinter as tk
from tkinter import ttk

def desenhar_livro(canvas):
    # Corpo do livro
    canvas.create_rectangle(10, 10, 70, 90, fill="#4a6cf7", outline="#924af7")

    # Lombada esquerda
    canvas.create_rectangle(10, 10, 25, 90, fill="#2f49c9", outline="#6a2fc9")

    # Linha simulando páginas
    canvas.create_line(70, 10, 70, 90, fill="#d9d9d9", width=3)


def mostrarLivros(lista):
    janela = tk.Tk()
    janela.title("Livros disponíveis")
    janela.geometry("550x500")
    janela.configure(bg="#f2f2f2")

    frame = tk.Frame(janela, bg="#f2f2f2")
    frame.pack(fill=tk.BOTH, expand=True)

    canvas = tk.Canvas(frame, bg="#f2f2f2", highlightthickness=0)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    lista_frame = tk.Frame(canvas, bg="#f2f2f2")
    canvas.create_window((0, 0), window=lista_frame, anchor="nw")

    # Criar cards
    for l in lista:
        card = tk.Frame(lista_frame, bg="white", bd=2, relief="raised")
        card.pack(pady=10, padx=15, fill="x")

        # Desenho do livro (o "icone")
        icone = tk.Canvas(card, width=80, height=100, bg="white", highlightthickness=0)
        icone.pack(side="left", padx=10)
        desenhar_livro(icone)

        # Texto do livro
        texto = (
            f"{l.titulo}\n"
            f"Autor: {l.autor}\n"
            f"Preço: R${l.preco}\n"
            f"Estoque: {l.quantidadeEstoque}"
        )
        
        info = tk.Label(card, text=texto, bg="white", anchor="w", justify="left", font=("Arial", 10))
        info.pack(side="left", padx=10)

    janela.mainloop()