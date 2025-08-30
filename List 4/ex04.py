#Questão 4
n = int(input("Digite um número:"))
c = 1
while c<=10000:
    if c%n == 2:
        print(c)
    c+=1