#Questão 5
continua = "S"
while continua == "S":
    n = int(input())
    c = 0
    while c < 10:
        c+=1
        print(f"{c} x {n} = {c*n}")
    continua = str(input("Deseja continuar? [S/N] ")).upper()
