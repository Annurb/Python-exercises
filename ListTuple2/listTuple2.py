#Questão 1
def verifica_entrada(n):
    while not(1<=n<=10**4):
        n = int(input("Digite novamente: "))
    return n
lista = []
nvoltaram = []
r1, n1 = map(int, input().split())
r = verifica_entrada(r1)
n = verifica_entrada(n1)
for c in range(r):
    lista.append(c+1)
voltaram = list(map(int, input().split()))
for d in range(len(lista)):
    if not lista[d] in voltaram:
        nvoltaram.append(lista[d])
if len(nvoltaram) == 0:
    print("*")
else:
    print(nvoltaram)

def verifica_entrada(i, m, f):
    m = int(m)
    while not(i<=m<=f):
        m = int(input())
    return m
go = 1   
p = verifica_entrada(1, input(), 5)
n = verifica_entrada(2, input(), 100)
lista = list(map(int, input().split()))
for c in range(len(lista)-1):
    diferenca = lista[c+1] - lista[c]
    if diferenca > p:
        go = 0
        break
if go == 0:
    print("GAME OVER")
else:
    print("YOU WIN")
    
#Questão 3
def verifica_entrada(n):
    n = int(n)
    while not(1<=n<= 50):
        n = int(input("Digite novamente: "))
    return n

lista = []
n = verifica_entrada(input())
bombas = []
for c in range(n):
    num = int(input())
    lista.append(num)
for d in range(n):
    if d == 0:
        bombas.append(lista[d] +lista[d+1])
    elif d == n-1:
        bombas.append(lista[d-1] +lista[d])
    else:
        bombas.append(lista[d-1] +lista[d] + lista[d+1])
print(bombas)

#Questão 4
def verifica_entrada(i, m, f):
    while not(i<=m<=f):
        m = int(input("Digite novamente: "))
    return m

posicao = 0
n = int(input())
for c in range(n):
    qt1, s1 = map(int, input().split())
    qt = verifica_entrada(4, qt1, 10)
    s = verifica_entrada(1, s1, 100)
    lista = list(map(int, input().split()))
    for c in range(len(lista)):
        if c == 0:
            posicao = 1
            indice = abs(s - lista[0])
        else:
            if abs(s-lista[c])<indice:
                    posicao = c+1
                    indice = abs(s-lista[c])
    print(posicao)
    
#Questao 5
x = list(map(int, input().split()))
y = list(map(int, input().split()))
i = 1
for c in range(len(x)):
    if x[c] == y[c]:
        print("N")
        i = 0
        break
if i != 0:
    print("Y")

#Questao 6
x = []
for c in range(10):
    y = int(input())
    if y <1:
        x.append(1)
    else:
        x.append(y)
    print(f"X[{c}] = {x[c]}")       

#Questão 7
def verifica_entrada(x, y, a):
    while not x == y:
        a = []
        a = list(map(int, input("Digite novamente os suspeitos: ").split()))
        x = len(a)
    return a

while True:
    suspeito = []
    n = int(input())
    if n == 0:
        break
    suspeito = list(map(int, input().split()))
    suspeito = verifica_entrada(len(suspeito), n, suspeito)
    nsuspeito = sorted(suspeito)
    segundo = nsuspeito[len(nsuspeito)-2]
    resposta = suspeito.index(segundo)
    print(resposta+1)

#Questão 8
inteiros = []
d2 = d3 = d4 = d5 = 0
n = int(input())
inteiros = list(map(int, input().split()))
for c in range(len(inteiros)):
    if inteiros[c]%2 == 0:
        d2 +=1
    if inteiros[c]%3 == 0:
        d3 +=1
    if inteiros[c]%4 == 0:
        d4 +=1
    if inteiros[c]%5 == 0:
        d5+=1
print(f"""{d2} Multiplo(s) de 2
{d3} Multiplo(s) de 3
{d4} Multiplo(s) de 4
{d5} Multiplo(s) de 5""")

#Questão 9
while True:
    rpm = []
    n = int(input())
    indice = 0
    if n == 0:
        break
    rpm = list(map(int, input().split()))
    for c in range(len(rpm)):
        if c == 0:
            pass
        elif rpm[c] < rpm[c-1]:
            indice = c+1
            break
    print(indice)

#Questão 10
produto = list(map(int, input().split()))
nlista = []
for c in range(len(produto)):
    if produto[c]< 150:
        nvalor = produto[c]*1.15
        nlista.append(nvalor)
    elif produto[c]> 650:
        nvalor = produto[c]*0.95
        nlista.append(nvalor)
for d in range(len(nlista)):
    print(f"{nlista[d]:.2f}", end = " ")

#Questão 11
palavra = str(input()).upper()
lista = []
soma = 0
for c in palavra:
    lista.append(c)
for d in range(len(lista)):
    num = 0
    if lista[d] == "Q" or lista[d] == "Z":
        num = 10
    elif lista[d] == "J" or lista[d] == "X":
        num = 8
    elif lista[d] == "K":
        num = 5
    elif lista[d] == "F" or lista[d] == "H" or lista[d] == "V" or lista[d] == "W" or lista[d] == "Y":
        num = 4
    elif lista[d] == "B" or lista[d] =="C" or lista[d] == "M" or lista[d] == "P":
        num = 3
    elif lista[d] == "D" or lista[d] == "G":
        num = 2
    soma+=num
    if d < (len(lista) - 1):
        print(f"{num} +", end = " ")
    else:
        print(f"{num} =", end = " ")
print(soma)

#Questao 12
aposta = list(map(int, input().split()))
sorteio = list(map(int, input().split()))
num = 0
for c in range(len(aposta)):
    for d in range(len(aposta)):
        if aposta[c] == sorteio[d]:
            num +=1
if num < 3:
    print("azar")
elif num == 3:
    print("terno")
elif num == 4:
    print("quadra")
elif num == 5:
    print("quina")
else:
    print("sena")

