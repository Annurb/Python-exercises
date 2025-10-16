matriz = [[10, 'Q', 'Z'], [8, 'J', 'X'], [5, 'K'],[4, 'F', 'H', 'V', 'W', 'Y'],[3, 'B', 'C', 'M', 'P'],[2, 'D', 'G']]
nome = input().upper()
soma = 0 
for c in nome:
    for linha in matriz:
        for letra in linha:
            if c == letra:
                soma+=linha[0]
print(soma)