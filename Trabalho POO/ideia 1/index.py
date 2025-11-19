from noticias import Noticias
import cadastro
import random

def classe_usuario(nome, celular, gmail, senha):
    usuario = cadastro.Usuario(nome, celular, gmail, senha)
    return usuario

def logado(lista_usuarios):
        sair = str(input("Deseja voltar? ")).upper()
        if sair[0] != "S":
            gmail = input("Digite o seu gmail: ")
            senha = input("Digite a senha: ")
            indice = 0
            for c in range(len(lista_usuarios)):
                if lista_usuarios[c].getGmail() == gmail and lista_usuarios[c].getSenha() == senha:
                    print("Você está logado! ")
                    indice = 1
            if indice == 0:
                print("Erro na senha ou gmail")
                return logado(lista_usuarios)
    

lista_usuarios = []

titulo = "Superlua poderá ser vista em todo o Brasil nesta semana"
autor = "Fulaninho de tal"
linhafina = "Lorem ipsum dolor sit amet. In quia labore et voluptas autem ut quaerat autem ut sunt architecto"
texto = "Lorem ipsum dolor sit amet. In quia labore et voluptas autem ut quaerat autem ut sunt architecto. Qui voluptatum molestiae ut illo odit qui galisum delectus. Hic reiciendis quibusdam ad omnis consequatur qui dolorem rerum aut veritatis voluptatem. Non quasi laudantium qui laudantium quia sed explicabo sint aut voluptas sunt cum Quis omnis aut totam laborum."


titulo2 = "Meteoro 'bola de fogo' surpreende ao iluminar o céu do Rio Grande do Sul"
autor2 = "Fulaninho de tal 2"
linhafina2 = "Lorem ipsum dolor sit amet. In quia labore et voluptas autem ut quaerat autem ut sunt architecto"
texto2 = "Lorem ipsum dolor sit amet. In quia labore et voluptas autem ut quaerat autem ut sunt architecto. Qui voluptatum molestiae ut illo odit qui galisum delectus. Hic reiciendis quibusdam ad omnis consequatur qui dolorem rerum aut veritatis voluptatem. Non quasi laudantium qui laudantium quia sed explicabo sint aut voluptas sunt cum Quis omnis aut totam laborum."

noticiatitulo = []
noticiatitulo.append(titulo)
noticiatitulo.append(titulo2)
noticiageral = []

sobrenos = "Somos uma equipe de notícias de astronomia"

infos = Noticias(titulo, autor, linhafina, texto)
noticiageral.append(infos)
infos = Noticias(titulo2,autor2, linhafina2, texto2)
noticiageral.append(infos)

while True:
    print("selecione uma opção:\n1 -Sobre nós\n2 - Notícias\n3 - Corpos Celestes\n4 - Cadastro\n5 - Login\n6 - Sair")
    menu = int(input())

    if menu  == 1:
        print(sobrenos)
    if menu == 2: 
        print(f"Selecione qual notícia você deseja: ")
        for c in range(len(noticiatitulo)):
            print(f"{c+1} - {noticiatitulo[c]}")
        opcao = int(input())
        for d in range(len(noticiatitulo)):
            if opcao == d+1:
                noticiageral[d].imprimir_noticia()

    elif menu == 4:
        nome = str(input("Digite o nome completo: "))
        celular = int(input("Digite o celular: "))
        gmail = str(input("Digite o email"))
        senha = input("Digite uma senha: ")
        assinar = str(input("Deseja assinatura? ")).upper()
        empresa = str(input("É da empresa? ")).upper()
        if assinar[0] == "S":
            print("1 - Assinatura mensal: R$ 13.90\n2 - Assinatura anual: 12xR$9.90\n3 - Voltar")
            escolha = int(input())
            escolha_possivel = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
            chave_pix = ''
            for c in range(12):
                chave_pix += random.choice(escolha_possivel)
            if escolha == 3:
                usuario = classe_usuario(nome, celular, gmail, senha)
            else:
                print(f"Copie e cola: {chave_pix}")
                if escolha == 1:
                    usuario = cadastro.Assinatura_mensal(nome, celular, gmail, senha)
                else:
                    usuario = cadastro.Assinatura_anual(nome, celular, gmail, senha)
        elif empresa[0] == "S":
            chave = int("Digite a chave: ")
            if chave == 123456:
                usuario = cadastro.Empresa(nome, celular, gmail, senha)
        else:
            usuario = classe_usuario(nome, celular, gmail, senha)

        lista_usuarios.append(usuario)
        usuario.imprimir_informacao()
    
    elif menu == 5:
        logado(lista_usuarios)

    if menu == 6:
        break

