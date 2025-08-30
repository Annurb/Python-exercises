#Questão 3
continua = "S"
while continua == "S":
    sal = float(input("Digite o salário: "))
    desc = sal - 0.11*sal
    if 0.11*sal >320:
        desc = sal-320
        porcent = 100-desc/sal*100
        print(f"Novo desconto aplicado. Porcentagem: {porcent:.2f} %")
    print(f"Valor com desconto: {desc:.2f}")
    continua = str(input("Deseja continuar? [S/N]")).upper()