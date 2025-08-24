#Questao 25
a = float(input())
if a>= 7000:
    n1 = 0.75*a
    d = 25
elif a >= 5000:
    n1 = 0.85*a
    d = 15
else:
    n1 = 0.95*a
    d = 5
print(f"""Valor da compra: R${a}
Desconto: {d}%
Valor com desconto: R${n1:.2f}
      """)
