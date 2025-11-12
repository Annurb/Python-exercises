from animal import Animal
from vip import Vip

lista = [] 

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
        
        isvip = str(input("O cliente é VIP? ").lower())
        if isvip[0] == "s":
            alimentacao = bool(input("Restrição alimentar"))
            banho = int(input("Periodicidade do banho: "))
            animal = Vip(nome, idade, peso, dono, raca, pelo, alimentacao, banho)
        else:
            animal = Animal(nome, idade, peso, dono, raca, pelo)

        lista.append(animal)

        animal.imprimir_informacao()

    elif cadastro == 2:
        print("Escolha uma opção:")
        imprimir = int(input("1- Imprimir um cliente específico\n2 - Imprimir todos os clientes\n"))
        if imprimir == 1:
            clientespecifico = input("Digite o nome do cliente: ").upper()
            for classe in lista:
                if classe.getNome() == clientespecifico:
                    classe.imprimir_informacao()
        
        else:
            for classe in lista:
                classe.imprimir_informacao()

    elif cadastro == 3:
        nomedocao = input("Digite o nome do cliente: ").upper()
        for classe1 in lista:
            if classe1.getNome() == nomedocao:
                classe1.restricao_alimentar()
    else: 
        animal.cachorro_idoso()
            


