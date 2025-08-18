#Consumo ex014
#entrada de dados
x = float(input("Distância total percorrida: "))
y = float(input("Total de combustível gasto: "))

#Processamento
consumo = x/y

#saída de dados
print("{:.3f} km/l".format(consumo))
