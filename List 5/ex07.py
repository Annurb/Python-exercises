#Questão 7
d = vf = vg = -1
limite = 12
while not(1 <= d<= 100 and 1<=vf<=100 and 1<= vg <=100):
    d, vf, vg = input().split()
    d = float(d)
    vf = float(vf)
    vg = float(vg)
if vg<=vf or d == 12:
    print("N")
else:
    tg = 12/vg
    tf = 12/vf 
    if tg <= tf:
        print("S")
    else:
        print("N")