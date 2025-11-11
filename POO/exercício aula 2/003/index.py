from animal import Animal
from ave import Ave

lista = []

while True:
    continuar = input("Deseja continuar? ")
    if continuar[0] == "N":
        break

    nome, especie, idade = input("Digite o nome, espécie e idade: ").split()

    nome = str(nome)
    especie = str(especie)
    idade = int(idade)

    isave = input("É ave? ").upper()
    if isave[0] == "S":
        envergadura = float(input("Envergadura: "))
        animal = Ave(nome, especie, idade, envergadura)

        if animal.pode_voar(especie):
            print("Ela pode voar")
        else:
            print("Não pode voar")
    else:
        animal = Animal(nome, especie, idade)

    lista.append(animal)

    info = str(input("Deseja exibir a informação de qual animal? "))
    for c in range(len(lista)):
        if lista[c].getNome() == info:
            lista[c].exibir_informacoes()
            
