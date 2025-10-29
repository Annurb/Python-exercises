def funcao(base, n):
    proximalinha = []
    for c in range(n):
        if c == 0:
            pass
        else:
            if base[c] == base[c-1]:
                proximalinha.append(1)
            else:
                proximalinha.append(-1)
    n = n-1
    base = proximalinha
    if n!= 1:
        return funcao(base, n)
    else:
        return(base[0])

n = int(input())
base = list(map(int, input().split()))
proximalinha = []

ultimo = funcao(base, n)
if ultimo == -1:
    print("branca")
else:
    print("preta")



