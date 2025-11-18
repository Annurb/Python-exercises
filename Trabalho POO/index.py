from noticias import Noticias

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
    print("selecione uma opção:\n1 -Sobre nós\n2 - Notícias\n3 - Cadastro\n4 - Login\n5 - Sair")
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
    elif menu == 3:
        

    if menu == 5:
        break

