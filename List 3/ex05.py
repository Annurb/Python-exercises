#Questão 5
num = int(input("Digite um inteiro: "))
for c in range(2, num):
    if num%c == 0:
        print("Nâo é primo. ")
        break
    else:
        print("É primo.")
        break
        