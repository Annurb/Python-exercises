#Questao 15
hi, mi, hf, mf = input().split()
hi = int(hi)
mi = int(mi)
hf = int(hf)
mf = int(mf)

if(hf>hi) and (mf>mi):
    hora = hf - hi
    if(mf>=mi):
        minuto = mf-mi
    else:
        minuto = 60 +(mf-mi)
elif(hf< hi) and (mf> mi):
    hora = 24 - hi + hf
    if(mf>=mi):
        minuto = mf-mi
    else:
        minuto = 60 +(mf-mi)
else:
    hora = 24
    if(mf>=mi):
        minuto = mf-mi
    else:
        minuto = 60 +(mf-mi)
print(f"O JOGO DUROU {hora} HORA(S) E {minuto} MINUTO(S)")