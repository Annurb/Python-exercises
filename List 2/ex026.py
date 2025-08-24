#Questao 26
a = float(input())
b = float(input())

if a>b:
    quantia = a-b
    print(f"Quantia faltante: R${quantia:.2f}")
elif a<b:
    troco = b-a
    print(f"Troco: R$ {troco:.2f}")