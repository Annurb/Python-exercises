questao = ["A", "B", "C", "D", "E"]
while True:
    n = int(input())
    if n == 0:
        break
    for c in range(n):
        lista = list(map(int, input().split()))
        preto = 0
        for d in range(5):
            if lista[d] <= 127:
                preto +=1
                alternativa = questao[d]
        if preto >1 or preto == 0:
            print("*")
        else:
            print(alternativa)
                
