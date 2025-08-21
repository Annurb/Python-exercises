#Questão 12
int(input())
d2 = int(input())
d3, d4, d5, d6 = input().split()
d3 = int(d3)
d4 = int(d4)
d5 = int(d5)
d6 = int(d6)
d7 = int(input())
if(d3+d5 == 7 and d2+d7 == 7 and d4+d6 == 7):
    print("SIM")
else:
    print("NAO")

#Questão 14
hi, hf = input().split()
hi = int(hi)
hf = int(hf)
if(hf> hi):
    duracao = hf-hi
elif(hf == hi):
    duracao = 24
else: 
    duracao = 24 - hi +hf
print(f"O JOGO DUROU {duracao} HORA(S)")