#Questão 3
def verifica_entrada(inicio, b, fim):
    b = int(b)
    while not( inicio<=  b <= fim):
        b = int(input("Digite novamente: "))
    return b

def controle_capacidade(pessoas):
    if pessoas> c:
        return True
    
#main
pessoas = 0
n = verifica_entrada(1, input(), 1000)
c = verifica_entrada(1, input(), 1000)
i = 0

for d in range(n):
    s = verifica_entrada(0, input(), 1000)
    e = verifica_entrada(0, input(), 1000)
    s = int(s)
    e = int(e)

    pessoas = pessoas + e -s

    passou = controle_capacidade(pessoas)
    if passou:
        i = 1

if i == 1:
    print("S")
else:
    print("N")


