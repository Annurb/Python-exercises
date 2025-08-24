#Questão 23
a = int(input("Valor1: "))

if a<0 or a>1000:
    print("Valor fora do intervalo.")
    print("Digite novamente")
    a = int(input("Valor1: "))

b = int(input("Valor2: "))
if b<0 or b>1000:
    print("Valor fora do intervalo.")
    print("Digite novamente:")
    b = int(input("Valor2: "))

if a==b:
    print("Valor1 = Valor2")
    print("Digite novamente:")
    b = int(input("Valor2: "))

if a>b:
    print(f"Saída: {a*3}")
else:
    print(f"Saída: {b*3}")
print("Fim do programa")
#nd 0<= b <= 1000 and a != b: