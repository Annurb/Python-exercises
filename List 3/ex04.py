#Questao 4
np = 0
ni = 0
for c in range(0, 10):
    num = int(input("Digite um número: "))
    if num%2 == 0:
        np +=1
    else:
        ni+=1
print(f"Números pares: {np}")
print(f"Numeros ímpares: {ni}")
