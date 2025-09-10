#Questão 2
def verifica_entrada(inicio, x, y, fim):
    while not(inicio<=x<=fim and inicio<=y<=fim):
        x, y = map(int, input("Digite x e y novamente: ").split())
    return x, y

def calcule(x, y):
    area = (x*y)/2
    print(f"Área: {area:.0f} cm2")
    
quant = int(input("Digite a quantidade de pipas: "))
for c in range(quant):
    xi, yi = map(int, input("Digite x e y: ").split())
    x, y = verifica_entrada(1, xi, yi, 100)

    calcule(x, y) 
