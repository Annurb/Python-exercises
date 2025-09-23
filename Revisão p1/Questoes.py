
#Questão 11 lista 4
n = int(input())
c = 0
res = 0
f1 = 0
f2= 1
while c< n:
    print(res, end = " - ")    
    if c == 1:
        res = 1
        f1 = 0
        f2 = 1 
    res = f1+f2
    f1 = f2
    f2 = res
    c+=1

#Questão 5 lista 7
def multiplicaPrimos(p1, p2):
    res = p1*p2
    return res
def verifica_entrada(n, m):
    while not(2<=n<=100 and 2<=m<=100):
        n, m = map(int, input("Digite novamente: ").split())
    return n, m
def encontra_primo(m):
    if m == 2:#Caso o primo seja 2
        return m
    for d in range(m, 2, -1):#Primeiro pegamos os números do maior para o menor
        primo = 1#Variável de controle
        for i in range(2, d):#Vemos se ele é primo
            if d%i == 0:#Caso seja divisível, então nao e primo
                primo = 0
                break#Sai do loop se não for primo
        if primo == 1:#Caso o primo continue 1, quer dizer que d é primo, assim ele retorna
            return d
x = int(input("Número de verificações: "))
for c in range(x):
    n1, m1 = map(int, input("Digite os valores de N e M: ").split())
    n, m = verifica_entrada(n1, m1)
    p1 = encontra_primo(n)
    p2 = encontra_primo(m)
    res = multiplicaPrimos(p1, p2)
    print(res)
print("Fim")


#Questão 7 lista 6
def verifica_entrada(i, m, f):
    while not(i<=m<=f):
        m = int(input("Digite novamente: "))
    return m
def calcula_distancia(t, v):
    d = v*t
    return d

n1 = int(input())
n = verifica_entrada(1, n1, 10)
dtotal = 0
for c in  range(n):
    t1, v1 = map(int, input().split())
    t = verifica_entrada(0, t1, 1000)
    v = verifica_entrada(0, v1, 1000)
    distancia = calcula_distancia(t, v)
    dtotal +=distancia
print(f"Distância total percorrida: {dtotal} km considerando os {n} trechos. ")

#Questão 5 lista 8
def verifica_entrada( m, n):
    while not(1<=m<=10 and 1<=m<=100000):
        m, n = map(int, input("Digite novamente: ").split())
    return m , n

def verifica_algarismo(n, m):
    m = str(m)
    while not(len(m) == n):
        m = input("Digite M novamente: ")
    m = int(m)
    return m

while True:
    n1, m1 = map(int, input().split())
    n, m = verifica_entrada(n1, m1)
    m = verifica_algarismo(n, m)
    m = str(m)
    soma = 0
    for d in m:
        d = int(d)
        soma +=d
    print(soma, end = " ")
    if soma%3 == 0:
        print("Sim")
    else:
        print("Não")
    continua = input("Deseja continuar? ").upper()
    if continua[0] == "N":
        break
    