def verifica_entrada(gotas, r):
    while len(gotas) != r:
        gotas = list(map(int, input().split()))
    return gotas

def quantos_dias(fita, f, dias):
    contador = 0
    for k in range(f):
        if k != 0 and k < f-1 and fita[k] == 1 and contador == 0:
            if fita[k-1] == 0 or fita[k+1] == 0:
                fita[k-1] = 1
                fita[k+1] = 1
                contador = 1
        elif k == f-1 and fita[k] == 1:
            if fita[k-1] == 0:
                fita[k-1] = 1
        else:
            contador = 0 
    if 0 in fita:
        dias +=1
        return quantos_dias(fita, f, dias)
    else:      
        dias+=1
        return dias


f, r = map(int, input().split())

gotas = list(map(int, input().split()))
gotas = verifica_entrada(gotas, r)

fita = []

#Gotas na fita 
for valor in range(f):
    contador = 0
    for gota in gotas:
        if gota == valor+1:
            fita.append(1)
            contador = 1
    if contador == 0:
        fita.append(0)

#fita após dias
dias = 0
fitadias = quantos_dias(fita, f, dias)
print(fitadias)

