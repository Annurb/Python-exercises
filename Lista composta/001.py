principal = []
num = 0
while True:
    cadastro = []
    nome = str(input("Digite o nome da pessoa: "))
    idade = int(input("Digite a idade: "))
    peso = float(input("Digite o peso: "))
    cadastro.append(nome)
    cadastro.append(idade)
    cadastro.append(peso)

    if len(principal) == 0:
        maior = menor = cadastro[2]
    else:
        if maior<cadastro[2]:
            maior = cadastro[2]
        if menor>cadastro[2]:
            menor = cadastro[2]
    if cadastro[1] > 20:
        num +=1
    
    principal.append(cadastro[:])


    parada = str(input("Deseja continuar o casastro? S/N:")).upper()
    if parada[0] == "N":
        break
maisleve = []
maispesado = []
maiores = []
print(f"Número de pessoas cadastradas: {len(principal)}")
for cadastro in principal:
    if cadastro[2] == maior:
        maispesado.append(cadastro[0])
    if cadastro[2] == menor:
        maisleve.append(cadastro[0])
    if cadastro[1] > 20:
        maiores.append(cadastro[0])
print(f"Pessoas mais pesadas: {maispesado}")
print(f"Pessoas mais leves: {maisleve}")
print(f"Há {num} pessoas maiores de 20 anos")
print(f"Essas pessoas são: {maiores}")

    
        

