#Questao 16 
diametro = int(input())
a, l, p = input().split()
a = int(a)
l= int(l)
p = int(p)

if(diametro <= a) and  (diametro <= l) and (diametro <= p):
    print("S")
else:
    print("N")