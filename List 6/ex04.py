#Questão 4
def verifica_entrada(inicio, meio, fim):
    while not(inicio<=meio<= fim):
        meio = int(input(f"Digite novamente (valor entre {inicio} e {fim}): "))
    return meio

def fuso(s, t, f):
    fusoH = s + t + f
    if fusoH >= 24:
        fusoH -= 24
    elif fusoH < 0:
        fusoH = 24 + fusoH
    print(fusoH)

#main
si, ti, fi = map(int, input().split())

s = verifica_entrada(0, si, 23 )
t = verifica_entrada(1, ti, 12 )
f = verifica_entrada(-5, fi, 5 )

fuso(s, t, f)