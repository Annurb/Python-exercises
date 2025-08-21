#Questao 17
salario = float(input())

if salario<= 400:
    nsalario = 1.15*salario
    reajuste = 0.15*salario
    percentual = 15
elif salario <= 800:
    nsalario = 1.12*salario
    reajuste = 0.12*salario
    percentual = 12
elif salario <= 1200:
    nsalario = 1.10*salario
    reajuste = 0.10*salario
    percentual = 10
elif salario <= 2000:
    nsalario = 1.07*salario
    reajuste = 0.07*salario
    percentual = 7
else: 
    salario = 1.04*salario
    reajuste = 0.04*salario
    pencentual = 4
print(f"""Novo salario: {nsalario:.2f}
Reajuste ganho: {reajuste:.2f}
Em percentual: {percentual} %""")