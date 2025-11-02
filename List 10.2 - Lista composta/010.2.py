def jogo(tabuleiro, linha, coluna):
    novotabuleiro = []
    for l in range(linha):
        linhatabuleiro = []
        for c in range(coluna):
            contador = 0
            if tabuleiro[l][c] == 1:
                linhatabuleiro.append(9)
            else:
                if linha != 1:
                    if l<(linha-1):
                        if tabuleiro[l+1][c] == 1:
                            contador+=1
                    if l>0:
                        if tabuleiro[l-1][c] == 1:
                            contador+=1
                if coluna != 1:
                    if c<(coluna-1):
                        if tabuleiro[l][c+1] == 1:
                            contador+=1
                    if c>0:
                        if tabuleiro[l][c-1] == 1:
                            contador+=1
                linhatabuleiro.append(contador)
        novotabuleiro.append(linhatabuleiro)
    return novotabuleiro
                
n, m = map(int, input().split())
tabuleiro = []

#Criação da matriz:
for linha in range(n):
    num = list(map(int, input().split()))
    tabuleiro.append(num)
    
novamatriz = jogo(tabuleiro, n, m)

for linha in novamatriz:
    print(" ".join(map(str, linha)))