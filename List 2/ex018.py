#Questao 18
a, b, c = input().split()
h, l = input().split()

a = int(a)
b = int(b)
c = int(c)

h = int(h)
l = int(l)

if(a<=h or a<=l) and (b<=h or b<=l):
    print("S")
elif(b<=h or b<=l) and (c<=h or c<=l):
    print("S")
elif(a<=h or a<=l) and (c<=h or c<=l):
    print("S")
else:
    print("N")