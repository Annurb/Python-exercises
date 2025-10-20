dicionario = {}
def diferenca(nome, valor2):
    diff = 0
    for c in range(len(nome)):
        if valor2[c] != nome[c]:
            diff +=1
    if diff >= 2:
        return 1
    else:
        return 0 
while True:
    soma = 0
    n = int(input())
    if n == 0:
        break
    for c in range(n):
        chave, valor = input().split()
        dicionario[chave] = valor
    m = int(input())
    for d in range(m):
        chave2, valor2 = input().split()
        nome = dicionario.get(chave2)
        dif = diferenca(nome, valor2)
        soma+=dif
    print(soma)