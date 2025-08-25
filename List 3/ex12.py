#Questao 12
n = int(input("Número de praias ara cadastrar: "))
mdistancia = 0
mnome = ""
i = 0
sdistancia = 0
for c in range(0, n):
    nome = str(input("Digite o nome: "))
    distancia = int(input("Digite a distância do centro: "))
    sdistancia +=distancia
    if distancia> mdistancia:
        mdistancia = distancia
        mnome = nome
    if 15<= distancia <=20:
        i +=1
media = sdistancia/n
print(f"Praia mais distante: {mnome}")
print(f"Maior distâcia do centro: {mdistancia}")
print(f"Quantidade de praias entre 15 e 20 km: {i}")
print(f"Distância média entre as praias: {media}")