#Questao 24
a = int(input())

if a>0:
    print("Positivo")
    if a%2 == 0:
        print("Par")
elif a<0:
    print("Negativo")
    if a%2 == 0:
        print("Par")
else:
    print("Zero")