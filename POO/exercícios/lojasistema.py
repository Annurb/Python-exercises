from loja import Loja_de_roupas

lista = []

while True:
    cadastro = input("Deseja Cadastrar mais produtos? ").lower()
    if cadastro == "N":
        break
    nome, preco, quantidade = input().split()
    produto = Loja_de_roupas(nome, preco, quantidade)

    lista.append(produto)

    for c in range(len(lista)):
        print(lista[c].nome)
        print(lista[c].consulta_preco())

