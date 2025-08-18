#area ex009
#entrada de dados
a = float(input("Valor a: "))
b = float(input("Valor b: "))
c = float(input("Valor c: "))

#processamento
triangulo = (a*c)/2
circulo = 3.14159*(c**2)
trapezio = ((a+b)*c)/2
quadrado = b**2
retangulo = a*b

#saida de dados
print("""TRIANGULO: {:.3f}
CIRCULO: {:.3f}
TRAPEZIO: {:.3f}
QUADRADO: {:.3f}
RETANGULO: {:.3f}""".format(triangulo, circulo, trapezio, quadrado, retangulo))