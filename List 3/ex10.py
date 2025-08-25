#Questão 10
mnome = ""
mnota = 0
snota = 0
for c in range(1, 6):
    nome = input("Nome do aluno:")
    nota = float(input("Nota do aluno: "))
    snota +=nota

    if nota > mnota:
        mnome = nome
        mnota = nota
media = snota/5
print(f"Média da turma: {media:.2f}")
print(f"Melhor aluno: {mnome}")
print(f"Melhor nota:{mnota:.2f}")
if mnota<2.75:
    print("Reprovado")
elif mnota< 5.75:
    print("Em Recuperação")
else:
    print("Aprovado")