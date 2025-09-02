#Questão 9
r = 0
i = 1

while True:
    r = int(input())
    if r == 0:
        break
    somaa = 0
    somab = 0
     
    for c in range(r):
        a, b = map(int, input().split())
        somaa += a
        somab +=b

        if somaa>somab:
            ganhador = "Aldo"
        else:
            ganhador = "Beto"

    print(f"Teste {i}\n{ganhador}\n")
    i+=1

