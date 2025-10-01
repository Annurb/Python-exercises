'''#Questao 1
l, n = map(int, input().split())
msoma = (n-1)+(l-(n-1))**2
print(msoma)

#1165
def primo(x):
    for c in range(2, int(x**1/2 +1)):
        if x%c == 0:
            return False
    return True

n = int(input())
for c in range(n):
    x = int(input())
    prim = primo(x)
    if prim:
        print(f"{x} eh primo")
    else:
        print(f"{x} nao eh primo")
#1071
def somaImpar(x, y):
    soma = 0
    if y>x:
        for c in range(x+1, y):
            if c%2 !=0:
                soma+=c
    else:
        for d in range(y+1,x):
            if d%2 !=0:
                soma+=d
    return soma
x = int(input())
y = int(input())
soma = somaImpar(x, y)
print(soma)

#1234
while True:
    try:
        frase = str(input())
        frase2 = ""
        i = 0
        for c in range(0, len(frase)):
            if frase[c].isalpha():
                if (c-i)%2 == 0:
                    frase2 += frase[c].upper() 
                else:
                    frase2 += frase[c].lower()
            else:
                i += 1
                frase2 += frase[c]
        print(frase2)
    except EOFError:
        break

#1555
def ganhou(x,y):
    r = (3*x)**2 + y**2
    b = 2*(x**2)+(5*y)**2
    c = -100*x +y**3
    if r> b and r>c:
        return "Rafael ganhou"
    elif b>c and b>r:
        return "Beto ganhou"
    else:
        return "Carlos ganhou"

n = int(input())
for c in range(n):
    x, y = map(int, input().split())
    g = ganhou(x, y)
    print(g)

#1221
import math
def primo(num):
    for d in range(2, int(math.sqrt(num)+1)):
        if num%d == 0:
            return "Not Prime"
    return "Prime"           

n = int(input())
for c in range(n):
    num = int(input())
    p = primo(num)
    print(p)

#1079
def ponderada(a, b, c):
    mp = (2*a+3*b+5*c)/10
    return mp

n = int(input())
for c in range(n):
    a, b, c = map(float, input().split())
    media = ponderada(a, b, c)
    print(f"{media:.1f}")

#1235
n = int(input())
for c in range(n):
    frase = ""
    linha = str(input())
    num = len(linha)
    for c in range((num//2)-1, -1, -1):
        frase += linha[c]
    for d in range(num-1, (num//2)-1, -1):
        frase += linha[d]
    print(frase)

#1865
n = int(input())
for c in range(n):
    nome, forca = input().split()
    nome = str(nome)
    forca =int(forca)

    if nome == "Thor":
        print("Y")
    else:
        print("N")

#1436
t = int(input())
for c in range(t):
    n = int(input())
    for d in range(n):
        num = input()
        if d == n//2:
            a = num
    print(f"Case {c}: {a}")
    
#1116
n = int(input())
for c in range(n):
    x, y = map(int, input().split())
    if y == 0:
        print("divisao impossivel")
    else:
        d = x/y
        print(f'{d:.1f}')

#1241
n = int(input())
for c in range(n):
    a, b = map(str, input().split())
    num = len(b)
    i = 1
    indiceb = 0
    if int(a)<int(b):
        print("nao encaixa")
    else:
        for d in range(len(a)-num, len(a)):
            if b[indiceb] != a[d]:
                print("nao encaixa")
                i = 0
                break
            indiceb+=1
        if i == 1:
            print("encaixa")

#1985
def verifica_entrada(i, m, f):
    while not(i<=m<=f):
        m = int(input("Digite novamente: "))
    return m

p = int(input())
p = verifica_entrada(1, p, 5)
res = 0
for c in range(p):
    t, q = map(int, input().split())
    q = verifica_entrada(1, q, 500)
    if t == 1001:
        v = 1.50
    elif t == 1002:
        v = 2.50
    elif t == 1003:
        v = 3.50
    elif t == 1004:
        v = 4.50
    elif t == 1005:
        v = 5.50
    res = res + v*q
print(f"{res:.2f}")'''

#


