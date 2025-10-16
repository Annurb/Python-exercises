matriz = []
aluno = []
boletim = []
while True:
    menu = int(input("""
1. Cadastrar
2. Boletim Geral
3. Consulta por aluno
4. Sair 
"""))
    if menu == 1: 
        info = []
        nota = []
        nome = input("Nome do aluno: ")
        aluno.append(nome)
        n1, n2, n3 = map(int, input().split())
        info.append(n1)
        info.append(n2)
        info.append(n3)
        media = (info[0]+info[1]+info[2])/3
        nota.append(nome)
        nota.append(media)
        boletim.append(nota[:])
        info.append(media)
        matriz.append(info[:])
    if menu == 2:
        print(boletim)
    if menu == 3:
        pessoa = str(input("Digite o nome do aluno: ").lower())
        i = aluno.index(pessoa)
        print(matriz[i])
    if menu == 4:
        break