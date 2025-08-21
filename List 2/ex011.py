#Questão 11
cv, ce, cs, fv, fe, fs = input().split()
cv= int(cv)
ce = int(ce)
cs = int(cs)
fv = int(fv)
fe = int(fe)
fs = int(fs)

cv = cv*3
fv = fv*3

if(cv + ce > fv+fe):
    print("C")
elif(cv+ce<fv+fe):
    print("F")
else:
    if(cs> fs):
        print("C")
    elif(cs<fs):
        print("F")
    else:
        print("=")