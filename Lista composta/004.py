import random
matriz = []

op = str(input("Soma ou média (S ou M)? ")).upper()
opcao = int(input("Qual é a opção de preenchimento? 1 - randômica, 2 - digitada "))
t = int(input("Qual é o tamanho da matriz? "))
soma = 0
for l in range(t):
    linha = []
    for c in range(t):
        if opcao == 1:
            num = random.randint(-10, 10)
        else:
            num = int(input("Digite o número: "))
        if c<l:
            soma +=num
        linha.append(num)
    matriz.append(linha)

print(matriz)
if op == "S":
    print(f"A soma é {soma}")
else:
    media = soma/t
    print(f"A média é {media:.2f}")

