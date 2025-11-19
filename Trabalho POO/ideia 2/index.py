import livro
import cliente

while True:
    print("1 - Cadastrar Livro\n2 - Cadastrar Cliente\n3 - Vender Livro\n4 - Sair")
    menu = int(input("Escolha uma opção: "))

    if menu == 1:

        id = int(input("Id do livro: "))
        titulo = str(input("Título do livro: "))
        autor = str(input("Digite o autor: ")).title()
        genero = str(input("Digite o gênero: "))
        preco = float(input("Preço: R$ "))
        quantidadeEstoque = int(input("Quantidade no estoque: "))

        l1 = livro.Livro(id, titulo, autor, genero, preco, quantidadeEstoque)

        l1.exibirDetalhes()

    elif menu == 2:
        
        idCliente = int(input("Id do cliente: "))
        nome = str(input("Nome do cliente: "))
        endereco = str(input("Endereço: "))
        telefone = int(input("Telefone(apenas números): "))
        
        c1 = cliente.Cliente(idCliente, nome, endereco, telefone)

        c1.exibirInformacoes()
    
    elif menu == 3:


    else:
        break
