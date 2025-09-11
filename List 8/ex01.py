#Questão 1 
lista = ["N", "L", "S", "O"]
while True:
    num  = 0 
    n = int(input())
    
    while not(0<=n<=1000):
        n = int(input("Digite novamente: "))
        
    if n == 0:
        break
    
    name = str(input()).strip().upper()
    
    while not(len(name) == n):
        name = str(input("Digite novamente: ")).strip().upper()
        
    for m in name:
        if m == "D":
            num = num +1
            if num > 3:
                num = 0 
        else: 
            num = num-1
            if num < 0: 
                num = 3
    print(lista[num])