#Questão 5
def verifica_entrada(inicio, meio, fim):
    while not(inicio<=meio<=fim):
        meio = int(input("Digite novamente um valor entre {inico} e {fim}: "))
    return meio
 
def escolha(a, b, c, h, l):
    if (a<=h) and (b<=l or c<= l):
        return True
    elif (b<=h) and(c<=l or a<=l):
        return True
    elif (c<=h) and (b<=l or a<=l):
        return True
    else: 
        return False

ai, bi, ci = map(int, input().split())

a = verifica_entrada(1, ai, 300)
b = verifica_entrada(1, bi, 300)
c = verifica_entrada(1, ci, 300)

hi, li = map(int, input().split())

h = verifica_entrada(1, hi, 250)
l = verifica_entrada(1, li, 250)

saida = escolha(a, b, c, h, l)

if saida: 
    print("Você escolheu o tamanho adequado. Parabens pela compra! ")
else: 
    print("Sinto muito, acho que você deve procurar outro colchão!")
