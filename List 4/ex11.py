#Questão 11
n = int(input("Digite um número inteiro: "))

a = 0
b = 1
c = 0

while c < n:
    print(a, end=" ")
    
    d= a + b  # soma dos dois últimos
    a = b            # o "segundo" vira o primeiro
    b = d     # e o próximo vira o "segundo"
    
    c += 1