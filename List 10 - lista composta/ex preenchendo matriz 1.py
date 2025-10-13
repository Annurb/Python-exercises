#preechendo uma matriz
#crie um programa que crie uma matriz 3x3 e preencha seus valores

matriz=[[0,0,0],[0,0,0],[0,0,0]]   #para não usar append

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c]= int(input(f'Digite um valor para posição [{l},{c}]: '))

print(matriz)

for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end=" ")
    print()

