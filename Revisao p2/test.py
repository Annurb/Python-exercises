lista = [1, 2, 3, 4]
for elemento in lista:
    print(elemento, end = " ")

print()
matriz = [['Adriana', 1],['Cassio', 2]]
for linha in matriz:
    print(" ".join(map(str, linha)))

print(linha.count(2))
print(2 in linha)