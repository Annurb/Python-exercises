while True:
    continua = input("Deseja continuar? ").upper()
    if continua[0] == "N":
        break

    #Cadastro
    cadastro = int(input("""Escolha uma opção:
1 - Cadastrar cliente
2 - Imprimir informações
3 - Restrição alimentar
4 - Cachorro mais idoso
"""))
    
    if cadastro == 1:
        nome = str(input("Digite o nome do animal: ")).upper()
        idade = int(input("Digite a idade: "))
        peso = float(input("Insira o peso do animal: "))
        dono = str(input("Digite o nome do dono: ")).upper()
        raca = str(input("Insira a raça: ")).upper()
        pelo = str(input("Insira a cor do pelo: "))
        
        isvip = input("O cliente é VIP? ").lower()
        if isvip == "s":
            alimentacao = str("Insira a restrição alimentar: ")
            banho = int("Periodicidade do banho: ")
            animal = Vip(nome, idade, peso, dono, raca, pelo, alimentacao, banho)
        
