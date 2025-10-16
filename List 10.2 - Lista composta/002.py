def verifica_num(x):
    lista = []
    soma = 0
    for d in range (1, (x//2)+1):
        if x%d == 0:
            lista.append(d)
    for s in range( len(lista)):
        soma += lista[s]
    if soma == x:
        return True
    else:
        return False
    
n = int(input())
for c in range(n):
    x = int(input())
    perfeito = verifica_num(x)
    if perfeito: 
        print(f"{x} eh perfeito")
    else:
        print(f"{x} nao eh perfeito")