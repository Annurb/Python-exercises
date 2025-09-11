#Questão 5
def verifica_entrada(i, m, f):
    while not(i<=m<=f):
        m = int(input("Digite novamente: "))
    return m

def verifica_dig(m, n):
    p = str(m)
    l1 = p.strip()
    while len(l1) != n:
        m = int(input("Digite novamente o valor M: "))
        p = str(m)
        l1 = p.strip()
    return m 

def sim_ou_nao(m):
    p = str(m)
    l1 = p.strip()
    soma = 0
    for c in range(len(l1)):
        soma += int(l1[c])
    if soma%3 == 0:
        return True
    else:
        return False

while True:
    n1, m1 = map(int, input().split())
    n = verifica_entrada(1, n1, 10)
    m = verifica_entrada(1, m1, 100000)
    m = verifica_dig(m, n)
    SouN = sim_ou_nao(m)

    if SouN:
        print("Sim")
    else:
        print("Não")

    continua = str(input("Deseja continuar? ")).upper()
    if continua == "N":
        break

