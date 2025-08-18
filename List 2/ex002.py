#Questao 2
valor = float(input("Valor do produto: R$ "))
pagamento = str(input(""" Condição de pagamento:
a. à vista (dinheiro ou cheque) – 10% de desconto 
b. 1x no cartão – 5% de desconto 
c. 2x cartão – preço normal 
d. 3x ou mais no cartão - 20% de juros
"""))

if pagamento == "a":
    nvalor = valor*0.9
elif pagamento =="b":
    nvalor = valor*0.95
elif pagamento == "c":
    nvalor = valor
else:
    nvalor = valor*1.2
    
print(f" o valor a ser pago vai ser: R$ {nvalor:.2f}")