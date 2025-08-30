#Questão 10
n = int(input())
for c in range(0, n):
    x, y =map(int, input().split())
    soma = 0
    if x>y:
        y+=1
        while y<x:
            if y%2 == 1:
                soma +=y
            y+=1
        print(soma)
    else:
        x+=1
        while x<y:
            if x%2 == 1:
                soma +=x
            x+=1
        print(soma)