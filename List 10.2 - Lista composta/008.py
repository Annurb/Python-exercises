escolha = [] 
aleatorio = []
soma = 0
escolha = list(map(int, input().split()))
aleatorio = list(map(int, input().split()))
for c in range(6):
    for d in range(6):
        if escolha[c] == aleatorio[d]:
            soma+=1
match(soma):
    case 3:
        print("terno")
    case 4:
        print("quadra")
    case 5:
        print("quina")
    case 6:
        print("sena")
if soma <3:
    print("azar")