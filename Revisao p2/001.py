#questao 1
dicionario = {}
finalistas = ""
n = int(input())
for c in range(n):
    chave, valor = input().split()
    valor = int(valor)
    dicionario[chave] = valor
maximo = max(dicionario.values())

for chave, valor in dicionario.items():
    if valor == maximo:
        if finalistas == "":
            finalistas = chave
        else:
            finalistas += f", {chave}"
print(finalistas)

