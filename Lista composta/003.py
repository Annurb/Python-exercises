import random
matriz = list()
soma = 0
n = int(input("Qual é a linha a ser analisada: "))
op = str(input("Soma ou média(S ou M): ")).upper()

for l in range(12):
    linha = []
    for c in range(12):
        num = random.randint(0,10)
        linha.append(num)
    matriz.append(linha)

print(matriz)
numeros = matriz[n-1]
for i in numeros:
    soma += i
if op == "S":
    print(f"Soma = {soma}")
if op == "M":
    media = soma/12
    print(f"Média = {media:.2f}")
