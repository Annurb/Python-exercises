#distancia entre 2 pontos ex011
#entrada de dados
x1 = float(input("Digite o valor 1 do eixo x:"))
y1 = float(input("Digite o valor 1 do eixo y:"))
x2 = float(input("Digite o valor 2 do eixo x:"))
y2 = float(input("Digite o valor 2 do eixo y: "))

distancia = ((x2 - x1)**2 + (y2-y1)**2)**(1/2)

print("{:.4f}".format(distancia))
