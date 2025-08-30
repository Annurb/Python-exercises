#Questao 8
m = 1
n = 1
while m != 0 or n != 0:
    m, n =input().split()
    m = int(m)
    n = int(n)
    soma = 0
    if n ==0 or n ==0:
        break
    if m>n:
        while n != m+1:
            print(n, end = " ")
            soma +=n
            n+=1
    else:
        while m !=n+1:
            print(m, end=" ")
            soma +=m
            m+=1
    print(f"Sum= {soma}")