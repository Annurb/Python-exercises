import random
def verifica_linha(matriz):
    for linha in range(len(matriz)):
        for coluna in range(len(matriz)):
            if matriz[linha][coluna] != 0:
                jogador = matriz[linha][coluna]
                if coluna+5 < 10:
                    contador = 1
                    for k in range(5):
                        if matriz[linha][coluna+k] != jogador:
                            contador = 0
                            break
                    if contador == 1:
                        return jogador

def verifica_coluna(matriz):
    for linha in range(len(matriz)):
        for coluna in range(len(matriz)):
            if matriz[linha][coluna] != 0:
                jogador = matriz[linha][coluna]
                if linha+5 < 10:
                    contador = 1
                    for k in range(5):
                        if matriz[linha+k][coluna] != jogador:
                            contador = 0
                            break
                    if contador == 1:
                        return jogador

def vencedor(vencedorlinha, vencedorcoluna):
        if( vencedorlinha == None and vencedorcoluna == None) or (vencedorlinha == 1 and vencedorcoluna == 2) or (vencedorlinha == 2 and vencedorcoluna ==1):
            print("Não há vencedor")
        else:
            if vencedorcoluna == None:
                print(vencedorlinha)
            else:
                print(vencedorcoluna)
    

while True:
    menu = int(input(""" 
    [1] Preencher o tabuleiro lendo valores do teclado
    [2] Preencher o tabuleiro randomicamente
    [3] encerrar o programa
"""))
    if menu == 1:
        matriz = []
        for c in range(10):
            linha = list(input().split())
            matriz.append(linha)

        vencedor(vencedorlinha, vencedorcoluna)


    if menu == 2:
        matriz = []
        for c in range(10):
            linha = []
            for d in range(10):
                objeto = random.randint(0, 2)
                linha.append(objeto)
            matriz.append(linha)

        vencedorlinha = verifica_linha(matriz)
        vencedorcoluna = verifica_coluna(matriz)
        print(vencedorlinha)
        print(vencedorcoluna)

        vencedor(vencedorlinha, vencedorcoluna)

    if menu == 3:
        break