import livro
import cliente
import random
import labels

#livros
listaDeLivros = []
l1 = livro.Livro( "O Ceifador (Físico)", "Neil Shursterman", "Distopia", 50, 3)
base = livro.Livro("A empregada", "Freida McFadden", "Suspense", 30, 0)
l2 = livro.LivroFisicoLuxo("A empregada (Luxo)", base, 40, 1)
l3 = livro.Ebook("A empregada (Ebook)", base, 12)

listaDeLivros.append(l1)
listaDeLivros.append(l2)
listaDeLivros.append(base)
listaDeLivros.append(l3)

#Clientes
listaDeClientes = []
c1 = cliente.ClienteVip("Vitoria", 787924948, 63987652334)
listaDeClientes.append(c1)

#Menu
while True:
    print("1 - Cadastrar Livro\n2 - Buscar livro\n3 - Cadastrar Cliente\n4 - Deletar livro\n5 - Vender Livro\n6 - Sair")
    menu = int(input("Escolha uma opção: "))

    if menu == 1:

        titulo = str(input("Título do livro: "))
        autor = str(input("Digite o autor: ")).title()
        genero = str(input("Digite o gênero: "))
        preco = float(input("Preço: R$ "))
        quantidadeEstoque = int(input("Quantidade no estoque: "))

        luxo = int(input("Existem edições de luxo (Caso não, digite 0 para passar)? "))

        l = livro.Livro( titulo, autor, genero, preco, quantidadeEstoque)
        l.titulo += " (Físico)"

        #Livro de luxo
        if luxo != 0:
            precoLuxo = float(input("Qual o valor da edição de luxo? R$ "))
            lx = livro.LivroFisicoLuxo(titulo, l, precoLuxo, luxo)
            lx.titulo += " (Luxo)"
            listaDeLivros.append(lx)

        #Ebook
        ebook = float(input("Preço do Ebook: "))
        le = livro.Ebook(titulo, l, ebook)
        le.titulo += " (Ebook)"

        listaDeLivros.append(l)
        listaDeLivros.append(le)

        l.exibirDetalhes()
        if luxo != 0:
            lx.exibirDetalhes()
        le.exibirDetalhes()
    
    elif menu == 2: 

        livro = str(input("Nome do livro: "))

        indice = 0
        for d in range(len(listaDeLivros)):
            if livro == listaDeLivros[d].getNome():
                indice = 1
                listaDeLivros[d].exibirDetalhes()
                break
        if indice == 0:
            print("Livro não encontrado")

    elif menu == 3:
        cadouatu = str(input("Deseja cadastrar ou atualizar informações? ")).lower()

        nome = str(input("Nome do cliente: "))
        cpf = int(input("CPF: "))
        telefone = int(input("Telefone(apenas números): "))

        if cadouatu == "atualizar":
            for f in range(len(listaDeClientes)):
                if listaDeClientes[f].getNome().lower() == nome.lower():
                    listaDeClientes[f].atualizar( nome, cpf, telefone)
                    break

            print("Cliente atualizado")
            listaDeClientes[f].exibirInformacoes()
        else:
            print("Clientes VIP possuem frete GRATIS")
            vip = str(input("Deseja ser VIP? ")).upper()
            
            if vip[0] == "S":
                c = cliente.ClienteVip(nome, cpf, telefone)
            else:
                c = cliente.Cliente( nome, cpf, telefone)

            listaDeClientes.append(c)

            c.exibirInformacoes()
    
    elif menu == 4:

        livro = str(input("Livro desejado: ")).title()

        for c in range(len(listaDeLivros)):
            if livro == listaDeLivros[c].getNome():
                del listaDeLivros[c]
                break
    
    elif menu == 5:
        carrinho = livro.Carrinho()

        while True:

            nome = input("Digite o nome do livro com seu tipo(ou Enter para finalizar): ")

            if nome == "":
                break

            encontrado = 0
            for f in range(len(listaDeLivros)):
                if listaDeLivros[f].getNome().lower() == nome.lower():

                    estoque = listaDeLivros[f].removerEstoque(1)

                    if estoque != 0:
                        carrinho.adicionar(listaDeLivros[f])
                        encontrado = 1
                        print("Livro adicionado ao carrinho")
                    break
            if encontrado == 0:
                print("Livro não encontrado")


            remover = input(("Deseja remover algum livro do carrinho? (Nome do livro ou Enter caso não)"))

            if remover != "":
                encontrado = 0
                for f in range(len(listaDeLivros)):
                    if listaDeLivros[f].getNome().lower() == remover.lower():
                        carrinho.remover(listaDeLivros[f])
                        encontrado = 1

                        listaDeLivros[f].adicionarEstoque(1)

                        print("Livro removido carrinho")
                        break
                
                if encontrado == 0:
                    print("Livro não encontrado")
            
        print(f"Total da compra: R$ {carrinho.calcularTotal()}")

        if carrinho.calcularTotal() > 0:

            #Simulação da venda
            nome = str(input("Digite o nome completo: "))
            cpf = int(input("Digite o CPF: "))

            print("\nEndereço:")
            estado = str(input("Digite o estado (ex:SC): ")).upper()
            endereco = str(input("Digite o endereço: "))

            pagamento = livro.Venda(cpf, nome, carrinho)

            #Vendo se o cliente é vip
            for f in range(len(listaDeClientes)):
                if listaDeClientes[f].getNome().lower() == nome.lower():
                    if listaDeClientes[f].isVip() != "Sim" and listaDeClientes[f].getCPF() != cpf:
                        pagamento.calcularFrete(estado)

            print(f"Valor total da compra: R$ {pagamento.calculaTotal():.2f}")

            print("\nEscolha a forma de pagamento:\n1 - Pix\n2 - Cartão de credito(até 3x sem juros)\n3 - Cartão de débito")

            formaDePagamento = int(input())

            if formaDePagamento == 1:
                labels.formaPix()
                escolha_possivel = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
                chave_pix = ''

                pagamento.formaDePagar("Pix")

                for c in range(12):
                    chave_pix += random.choice(escolha_possivel)
                copia = input(f"Copie e cole a chave pix: {chave_pix}(Digite Enter)")

                if copia == "":
                    print("\nPagamento aprovado")
            
            elif formaDePagamento == 2:
                pagamento.formaDePagar("Crédito")
                parcelas = int(input("Parcelas [1, 2 ou 3]: "))
                if parcelas == 2:
                    parcela = (pagamento.calculaTotal()/2)
                elif parcelas == 3:
                    parcela = (pagamento.calculaTotal()/3)
                else:
                    parcela = (pagamento.calculaTotal())
                print(f"Cada parcela ficou: R${parcela:.2f}")
                print("Pagamento aprovado")
            else:
                pagamento.formaDePagar("Débito")
                print("Pagamento aprovado")
   
            pagamento.imprimirVenda()
    else:
        break
