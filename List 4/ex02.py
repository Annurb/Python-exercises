#Questão 2
import random
num = int(input("Adivinhe o número do computador(0 a 10): "))
while num > 10 or num <0:
    num = int(input("Número inválido. Digite novamente: "))
r = random.randint(0,10)
while num != r:
    num = int(input("Errou! Digite outra vez:"))
print("Paranbens! Você acertou")