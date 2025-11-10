from funcionario import Funcionario
from gerente import Gerente

while True:
    lista = [] 
    menu = int(input("""Escolha uma opção:
1 - Cadastrar funcionário
2 - Exibir dados
"""))
    if menu == 1:
        nome, salario = input("Digite o nome e o salário: ").split()
        gerente = input("É gerente? [S/N]").upper()
        if gerente[0] == "S":
            departamento = input("Insira o departamento: ")
            pessoa = Gerente(nome, salario, departamento)
        else: 
            pessoa = Funcionario(nome, salario)
        lista.append(pessoa)
    elif menu == 2:
        pessoa.__str__()



        