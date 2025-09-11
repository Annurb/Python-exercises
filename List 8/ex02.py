#Questão 2 
n = int(input())
for c in range(n):
    dignum = str(input())
    while not(len(dignum) == 3):
        dignum = str(input("Digite novamente:"))
    separa = dignum.strip()
    letra = separa[1]
    if int(separa[2]) == int(separa[0]):
        res = int(separa[2]) * int(separa[0])
    elif letra.upper() == letra:
        res = int(separa[2]) - int(separa[0])
    else:
        res = int(separa[2]) + int(separa[0])
    print(res)