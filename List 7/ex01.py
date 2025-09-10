#Questão 1
def verifica_entrada(valor):
    while not(0<=valor<=1):
        valor = int(input("digite novamente um valor entre 0 e 1: "))
    return valor
def ganhou(a, b, c):
        if a == b and b ==c:
            if a == 0:
                return False
            else:
                return "*"
        elif a != b and b == c:
            return "A"
        elif b != a and a == c:
            return "B"
        else: 
            return "C"

while True:
    ai, bi, ci = map(int, input().split())

    a = verifica_entrada(ai)
    b = verifica_entrada(bi)
    c = verifica_entrada(ci)

    ganhador = ganhou(a, b, c)

    if ganhador == False:
        break
    else:
        print(ganhador)