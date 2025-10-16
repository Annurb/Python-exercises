def verifica_par(m):
    par = 0
    for d in matriz:
        for c in range(len(d)):
            if d[c] %2 == 0:
                par+=1
    return par

def diagonal(m):
    somadiagonal = num = acimadiagonal = somaultima = menor = 0
    diagonalsec = []
    multi =1
    for d in range(len(matriz)):
        diagonalsec.append(matriz[d][(len(matriz)-1 - d)])
        for c in range(len(matriz)):
            if c == d:
                somadiagonal += matriz[d][c]
            if c>d:
                acimadiagonal += matriz[d][c]
                num+=1
            if c == (len(matriz) - 1): 
                somaultima += matriz[d][c]
            if d == 0:
                if c == 0:
                    menor = matriz[d][c]
                else:
                    if menor > matriz[d][c]:
                        menor = matriz[d][c]
    for s in range(len(diagonalsec)):
        multi+=diagonalsec[s]
    media = somadiagonal/(len(matriz))
    mediaa = acimadiagonal/num
    return media, mediaa, multi, somaultima, menor

n = int(input())
matriz = []
for c in range(n):
    linha = []
    for d in range(n):
        num = int(input())
        linha.append(num)
    matriz.append(linha[:])
for c in range(len(matriz)):
    print(matriz[c])
somapar = verifica_par(matriz)
mediadiagonal, mediaacima, diagonalsec, somaultima, menor = diagonal(matriz)

print(somapar)
print(mediadiagonal)
print(diagonalsec)
print(mediaacima)
print(somaultima)
print(menor)