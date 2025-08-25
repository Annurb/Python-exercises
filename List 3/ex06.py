#Questão 6
i = 0
num = int(input("Digite um inteiro: "))
for c in range(2, num ):
    if num%c == 0:
        print("Não é primo")
        for a in range(2, num):
            if num%a == 0:
                print(a, end=" ")            
        break
    else:
        print('É primo')
        break
