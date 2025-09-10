#Questão 3
def verifica_entrada(inicio, meio, fim):
    while not(inicio<=meio<=fim):
        meio = int(input("Digite novamente: "))
    return meio

def calcule(num):
    for c in range(2, int(num**0.5) + 1):
        if num % c == 0:
            return False
    return True

i = 0

for c in range(10):
    n1 = int(input("Digite um número: "))
    n = verifica_entrada(2, n1, 300)

    primo = calcule(n)

    if primo == False:
        print(f"O número {n} não é primo")
    else:
        print(f"O numero {n} é primo")
        i+=1
print(f"O total de primos foi {i}")
  