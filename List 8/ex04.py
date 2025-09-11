#Questão 4
def verifica_quantia(q):
    q = int(q)
    while not(1<=q<=15):
        q = int(input("Digite a quantia novamente:"))
    return q

def verifica_tipo(t):
    t = str(t).upper()
    while not(t == "C" or t == "R" or t == "S"):
        t = str(input("Digite novamente o tipo: "))
    return t

total = 0
coelho = 0 
rato = 0 
sapo = 0 

n = int(input())

for c in range(n):
    quantia, tipo = input().split()
    quantia = verifica_quantia(quantia)
    tipo = verifica_tipo(tipo)

    total +=quantia
    match(tipo):
        case "C":
            coelho+=quantia
        case "R":
            rato +=quantia
        case "S":
            sapo += quantia
    percentC = (coelho/total)*100
    percentR = (rato/total)*100
    percentS = (sapo/total)*100

print(f"""Total: {total} cobaias
Total de coelhos: {coelho}
Total de ratos: {rato}
Total de sapos: {sapo}
Porcentagem de coelhos: {percentC:.2f} %
Porcentagem de coelhos: {percentR:.2f} %
Porcentagem de coelhos: {percentS:.2f} %
""")