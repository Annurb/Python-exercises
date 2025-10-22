m, n = map(int, input().split())
dicionario = {}
for c in range(m):
    chave, valor = input().split()
    valor = int(valor)
    dicionario[chave] = valor

for s in range(n):
    texto = input().split()
    soma = 0
    for d in range(len(texto)):
        if (texto[d] in dicionario):
            soma += dicionario.get(texto[d])
    print(soma)