while True:
    continua = input("Deseja continuar? ").upper()
    if continua[0] == "N":
        break
    menu = int(input("""Escolha uma opção:
1 - Cadastrar conta
""" ))
    if menu == 1:
        raca = str(input("Raça do cachorro: ")).title()
        peso = float("Peso do animal: ")
        
