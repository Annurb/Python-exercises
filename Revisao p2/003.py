import random
while True:
    menu = int(input(""" 
    [1] Preencher o tabuleiro lendo valores do teclado
    [2] Preencher o tabuleiro randomicamente
    [3] encerrar o programa
"""))
    if menu == 2:
        matriz = []
        for c in range(9):
            linha = []
            for d in range(10):
                objeto = random.randint(0, 2)
                linha.append(objeto)
            matriz.append(linha)
        print(matriz)
        pretas = 0
        brancas = 0
        vencedor = 0
        jogador = 0
        for l in range(len(matriz)):
            for s in range(len(matriz)):
                if s == 0:
                    jogador = matriz[l][s]
                else:
                    if s+5< 10:
                        if all( matriz[l][s+k] == jogador for k in range(5)):
                            vancedor = jogador
                
        print(vencedor)

    if menu == 3:
        break