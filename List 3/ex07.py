#Questao 7
idadesoma = 0
n = int(input("Número de pessoas: "))
for c in range(0, n):
    idade = int(input(f"Idade da pessoa {c+1}: "))
    idadesoma +=idade
media = idadesoma/n
if media <=25:
    print("Turma jovem")
elif media < 60: 
    print("Turma adulta")
else:
    print("Turma idosa")