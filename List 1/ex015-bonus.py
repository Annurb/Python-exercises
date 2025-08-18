#salário com bonus ex015
#entrada de dados
nome = str(input("Nome do vendedor: "))
salario = float(input("Salário fixo: "))
vendas = float(input("Total de vendas: "))

#Processamento
total = salario + (vendas*0.15)

#saida de dados
print("TOTAL = R$ {:.2f}".format(total))