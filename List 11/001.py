n = int(input())
soma = 0
dicionario = {}
dicionario2 = {}

for d in range(n):
    m = int(input())
    for c in range(m):
        chave, valor = input().split()
        valor = float(valor)
        dicionario[chave] = valor

    p = int(input())
    for tamanho in range(p):
        chave2, valor2 = input().split()
        valor2 = float(valor2)
        dicionario2[chave2] = valor2

        for k, v in dicionario.items():
            if k == chave2:
                multiplica = v*valor2
                soma+=multiplica
    print(f"R$ {soma:.2f}")

