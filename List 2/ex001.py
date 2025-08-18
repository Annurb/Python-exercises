#Questão 1
valor = float(input("Valor da casa: "))
salario = float(input("Salário do comprador: "))
ano = int(input("Anos de pagamento: "))

prestacao = valor/(ano*12)

if (prestacao>0.3*salario):
    print("Empréstimo negado")
else:
    print(f"Empréstimo concedido! A prestação mensal será de R$ {prestacao:.2f}")