n, m = map(int, input().split())
pontuacao = 0
total = []
matriz = []
somatoria = []
for c in range(n):
    jogador = list(map(int, input().split()))
    matriz.append(jogador[:])
    jogador = []

for i in range(n):
    gols = matriz[i]
    marcou = True
    for g in gols:
        if g == 0:
            marcou = False
            break
    if marcou:
        pontuacao +=1

    total = 0
    for g in gols:
        total+=g
    somatoria.append(total)

max = 0
for t in somatoria:
    if t> max:
        max = t

artilheiros = []
for j in range(n):
    if somatoria[j] == max:
        artilheiros.append(j+1)
print(f'Número de jogadores que pontuaram em todas as partidas: {pontuacao}' )   
print(f'Artilehiro(s): jogador {artilheiros}({max} gols)')