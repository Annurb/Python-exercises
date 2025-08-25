#Questão 3
a = ""
b = 0
c = 0
n1 = 0
nome = ""
mens = 0
for c in range(0,5):
    a = str(input("Aluno: "))
    b = float(input("Média geral: "))
    c = float(input("Mensalidade: "))
    if b >n1:
        n1 = b
        nome = a
        mens = c

print(f"Melhor aluno(a): {nome}")
print(f"Melhor nota: {n1}")
print(f"Mensalidade: R$ {mens:.2f}")
print(f"Nova mensalidade: R$ {0.7*mens:.2f}")