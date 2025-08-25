#Questao 8
controle1 = 0
controle2 = 1
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
for c in range(n1, n2+1):
    controle1 += c
    controle2 *= c
print(f"Soma entre eles: {controle1}")
print(f"Multiplicação entre eles: {controle2}")
