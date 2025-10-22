n, m = map(int, input().split())
matriz = []
jogador = []
soma = []
pontuacao = 0
for c in range(n):
    jogador = []
    jogador = list(map(int, input().split()))
    matriz.append(jogador[:])
for l in range(n):
    for d in range(m):
        if l == 0:
            jogador.append(matriz[l][d])
            soma.append(matriz[l][d])
        else:
            jogador[d] = jogador[d]*matriz[l][d]
            jogador.pop(d+1)
            soma[d] = jogador[d]+matriz[l][d]
            jogador.pop(d+1)
print(jogador)
for num in range(len(jogador)):
    if jogador[num]>0:
        pontuacao +=1
print(soma)
print(pontuacao)
print(matriz)