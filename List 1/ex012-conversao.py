#Conversão de tempo ex012
#entrada de dados
segundos = int(input("Digite os segundos:"))

#processamento
horas = segundos //3600
minutos = (segundos%3600)//60
segundosres = segundos % 60

print("{} : {} : {}".format(horas, minutos, segundosres))
