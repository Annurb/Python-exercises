n, m = map(int, input().split())
matriz = []
for c in range(n):
    jogador = []
    jogador = list(map(int, input().split()))
    matriz.append(jogador[:])
for linha in range(n):
    for coluna in range(m):
        
print(matriz)