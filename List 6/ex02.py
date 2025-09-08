#Questão 2(aumento do salário)
def calcula_aumento(salario):
    if salario<=400:
        p = 15
    elif salario<= 800:
        p = 12
    elif salario <=1200:
        p = 10
    elif salario <=2000:
        p = 7
    else:
        p = 4
    novoSalario = salario * ((100+ p)/100)
    reajuste = novoSalario - salario
    print(f"Novo salário: {novoSalario:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: {p} %")
#main
salario = calcula_aumento(float(input()))