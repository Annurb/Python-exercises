def verifica_entrada(l, n):
    while len(l) != n:
        l = list(map(int, input("Digite novamente: ").split()))
    return l

def verifica_multiplos(l):
    contador = 0
    for d in range(len(l)):
        if l[d]%2 == 0:
            contador += 1
        elif l[d]%3 == 0:
            contador += 1
        elif l[d]%5 == 0:
            contador += 1
    return contador

n = int(input())
l = list(map(int, input().split()))
l = verifica_entrada(l, n)
multiplos = verifica_multiplos(l)
print(multiplos)