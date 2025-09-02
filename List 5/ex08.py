#Questão 8
#Criaçao das variaveis iniciais
n = -1
s = 1001
#Variáveis de controle
soma = 0
menor = 0
#Controle pra nao sair do escopo
while not(1<=n<-30 or -10**3<= s <=10**3):
    n, s = input().split()
    n = int(n)
    s = int(s)
#Número de colunas
for c in range(n):
    #Número que vai somar
    num = int(input())
    #colocar o menor como o inicial e a soma como o valor inicial mais o numero acrescido
    if c == 0:
        soma = s + num
        menor = s   
    else:
        #Desenvolver a soma
        soma += num
        #Colocar o menor valor
        if soma<menor:
            menor = soma
print(menor)