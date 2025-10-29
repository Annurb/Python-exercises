x = int(input())
dicionario = {}
lista = []
for c in range(x):
    chave = input()
    valores = list(input().split())
    dicionario[chave] = valores

print("Consulta:")
while True:
    nome, livro = input().split()
    pegarlista = dicionario.get(nome)
    sim = nome in dicionario
    if sim:
        c = 0
        for d in pegarlista:
            if d == livro:
                print("Livro Encontrado")
                c +=1
        if c == 0:
            print("Tente Novamente! Continue procurando com outro primo.... ")
    else:
        print("Essa pessoa não está cadastrada")

    continua = input("Deseja continuar? (S/N)").upper()
    if continua == "N":
        break
