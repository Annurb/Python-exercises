#Gasto de combustível ex013
#entrada de dados
tempo = float(input("Tempo gasto em horas: "))
velocidade = float(input("Velocidade média: "))

#Processamento
distancia = velocidade*tempo
litro = distancia/12

#saida de dados
print("{:.3f}".format(litro))