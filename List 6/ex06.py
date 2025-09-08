#Questão 6
def verifica(num):
    if num%2 == 0:
        return "Par"
    else:
        return "Ímpar"

i = 0
c = 0

for a in range(10):

    numi = int(input())
    num = verifica(numi)

    if num == "Par":
        i+=1
    else:
        c+=1
    print(num)
print(f"Ao todo, foram digitados {i} números pares e {c} númweros ímpares")