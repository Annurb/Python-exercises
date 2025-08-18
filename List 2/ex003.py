#Questao 3
peso = float(input("Peso da pessoa: "))
altura = float(input("Altura da pessoa:"))

IMC = (peso)/(altura**2)

if IMC < 18.5:
    print("Abaixo do peso")
elif IMC <= 25:
    print("Peso ideal")
elif IMC <= 30:
    print("Sobrepeso")
elif IMC <= 40:
    print("Obesidade")
else:
    print("Obesidade Mórbita")
