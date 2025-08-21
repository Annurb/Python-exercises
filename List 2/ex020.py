#Questao 20
c, q = input().split()
c = float(c)
q = float(q)

if c == 1:
    valor = 4*q
elif c == 2:
    valor = 4.5*q
elif c == 3:
    valor = 5*q
elif c == 4:
    valor = 2*q
else:
    valor = 1.5*q
print(f"Total: R$ {valor:.2f}")