#Questão 5
def verifica_entrada(n, m):
    while not(2<=n<=100 and 2<=m<=100):
        n, m = map(int, input("Digite novamente: ").split())
    return n, m

def verifica_primo(x):
    if x == 2:
        return x
    for d in range(x, 2, -1):
        primo = 1
        for s in range(2, d):
            if d%s == 0:
                primo = 0
                break
        if primo == 1:
            return d

def multiplica_primo(p1, p2):
    r = p1*p2
    return r     

num = int(input("Número de verificações: "))

for c in range(num):
    n1, m1 = map(int, input("Digite os valores de N e M: ").split())
    n, m = verifica_entrada(n1, m1)

    p1 = verifica_primo(n)
    p2 = verifica_primo(m)

    res = multiplica_primo(p1, p2)

    print(res)
print("Fim")