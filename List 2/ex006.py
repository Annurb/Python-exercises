#Questão 6 
dia1 = int(input("Dia "))
hora1, minuto1, segundo1 = input().split(" : ")
hora1 = int(hora1)
minuto1 = int(minuto1)
segundo1 = int(segundo1)
dia2 = int(input("Dia "))
hora2, minuto2, segundo2 = input().split(" : ")
hora2 = int(hora2)
minuto2 = int(minuto2)
segundo2 = int(segundo2)
if (hora1 <= hora2):
    ddia = dia2 - dia1
    dhora = hora1 - hora2
    if(segundo1<=segundo2):
        dsegundo = segundo2 - segundo1
    else:
        dsegundo = 60 -(segundo1 - segundo2)
    if(minuto1<=minuto2):
        dminuto = minuto2 - minuto1
    else:
        dminuto =  60 - (minuto1 - minuto2) 
else:
    ddia = dia2 - dia1 - 1
    dhora = 24 - (hora1 - hora2)
    if(segundo1<=segundo2):
        dsegundo = segundo2 - segundo1
    else:
        dsegundo = 60 -(segundo1 - segundo2)
    if(minuto1<=minuto2):
        dminuto = minuto2 - minuto1
    else:
        dminuto = 60 - (minuto1 - minuto2) 
print(f"{ddia} dia(s)")
print(f"{dhora} hora(s)")
print(f"{dminuto} minuto(s)")
print(f"{dsegundo} segundo(s)")