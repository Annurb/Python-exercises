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