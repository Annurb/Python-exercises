n = int(input())
dicionario = {'EPR':'EPR', 'EHD':'EHD'}
epr = ehd = intruso = 0
for c in range(n):
    chave, valor = input().split()
    if valor in dicionario.values():
        if dicionario.get(valor) == 'EPR':
            epr+=1
        elif dicionario.get(valor) == 'EHD':
            ehd+=1
    else:
        intruso+=1
print(f'EPR: {epr}')
print(f'EHD: {ehd}')
print(f'INTRUSOS: {intruso}')
