#Questão 4
def soma(inicio, fim):
    valorF = 0
    for c in range(inicio, fim+1):
        valorF +=c
    return valorF

def subtração(minuendo, subtraendo):
    valorS =0
    if minuendo > subtraendo:
        valorS = minuendo - subtraendo
        return valorS
    else:
        valorS = subtraendo - minuendo
        return valorS

while True:
    n1, n2 = map(int, input("Digite o intervalo: ").split())
    n3, n4 = map(int, input("Digite 2 valores: ").split())

    num  = soma(n1, n2)
    num2 = subtração(n3, n4)

    print(f"Soma do intervalo = {num}")
    print(f"Diferença = {num2}")

    continua = input("Deseja continuar? ").upper()
    if continua == "N":
        break
