dicionario = {}
x = int(input())
for c in range(x):
    lista = []            
    chave, valor1, valor2, valor3 = input().split()
    lista.append(valor1)
    lista.append(valor2)
    lista.append(valor3)
    dicionario[chave] = lista

while True:
    try:
        nome, presente = input().split()
        presentes = dicionario.get(nome)
        if nome in dicionario:
            for c in range(3):
                acertou = 0
                if presente == presentes[c]:
                    acertou = 1
                    break
            if acertou == 1:
                print("Uhul! Seu amigo secreto vai adorar o/")
            else:
                print("Tente Novamente!")

    except EOFError:
        break