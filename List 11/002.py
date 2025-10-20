n = int(input())
dicionario2 = {}
dicionario = {}
for c in range(n):
    chave = input()
    valor = input()
    dicionario[chave] = valor

m = int(input())
for d in range(m):
    chave2 = input()
    valor2 = input()
    dicionario2[chave2] = valor2

    for k, v in dicionario.items():
        if k == valor2:
            print(chave2)
            print(v)
