#Questão 5
n = int(input("Número de bandejas:"))
quebrado = 0
while not(1<n<100):
    n = int(input("Número fora do escopo, digite outro número:"))
for c in range(n):
    l = c = -1
    while not(0<=l<=100 and 0<=c<=100):
        l, c = input().split()
        l = int(l)
        c = int(c)
    if l>c:
        quebrado = quebrado + c
print(quebrado)
