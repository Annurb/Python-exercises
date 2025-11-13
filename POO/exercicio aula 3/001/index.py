from cao import Cao
from vip import Vip
lista = [] 
c1 = Cao("tommy", 4, "viralata", 2)
c2 = Cao("anny", 5, "viralata", 3)
lista.append(c1)
lista.append(c2)


while True:
    continua = input("Deseja continuar? ").upper()
    if continua[0] == "N":
        break
    menu = int(input("""Escolha uma opção:
1 - Cadastrar conta
2 - Imprimir informações
3 - Restrição alimentar
4 - Mensalidade
5 - Cachorro mais pesado
""" ))
    if menu == 1:
        raca = str(input("Raça do cachorro: ")).lower()
        peso = float(input("Peso do animal: "))
        nome = str(input("Nome do animal: ")).lower()
        banho = int(input("Quantos banhos/mes: "))

        isvip = str(input("O cliente é Vip?")).upper()
        if isvip[0] == "S":
            print("entrou")
            restricao = bool(input("O cão possui restrição alimentar? "))
            animal = Vip(nome, peso, raca, banho)
            animal.restricao(restricao)
        else:
            animal = Cao(nome, peso, raca, banho)
        animal.imprimir_informacao()
        lista.append(animal)
    
    if menu == 2:
        cliente = str(input("Nome do cliente: ")).lower()
        for c in lista:
            if c.getNome() == cliente:
                c.imprimir_informacao()
    if menu == 3:
        cliente1 = str(input("Nome do cliente: ")).lower()
        for d in lista:
            if d.getNome() == cliente1:
                d.restricao_alimentar()

    if menu == 4:
        cliente2 = str(input("Nome do cliente: ")).lower()
        for e in lista:
            if e.getNome() == cliente2:
                e.mensalidade()
    if menu == 5:
        pesos = []
        for g in range(len(lista)):
            pesos.append(lista[g].getPeso())
        for s in range(len(lista)):
            if max(pesos) == lista[s].getPeso():
                print(f"O cachorro mais pesado é {lista[s].getNome()}")
                break

        
    


