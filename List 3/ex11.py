#Questao 11
n = int(input("Quantas vezes: "))
controle1 = 0
controle2 = 0
controle3 = 0
for c in range(0, n):
    num = int(input("Digite um número: "))
    controle2 += num
    if c == 0:
        controle3 = num
    if num >controle1:
        controle1 = num
    if num < controle3:
        controle3 = num
media = controle2/n
print(f"Média: {media:.2f}")
print(f"Maior número: {controle1}")
print(f"Menor número: {controle3}")