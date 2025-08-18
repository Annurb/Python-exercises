#salario ex006
#entrada de dados
numero = int(input("Numero do funcionário:"))
trabalho = int(input("Horas trabalhadas:"))
valor = float(input("Valor recebido por hora:"))

#processamento
salario = trabalho*valor

#saida de dados
print("""NUMBER = {}
SALARY = U$ {}""".format(numero, salario))