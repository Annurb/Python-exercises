dicionario = {'W': 1, 'H': 1/2, 'Q':1/4, 'E':1/8, 'S':1/16, 'T':1/32, 'X':1/64}
while True:
    palavra = input().split('/')
    certo = 0
    if palavra[0] == '*':
        break
    for c in palavra:
        soma = 0
        for d in range(len(c)):
            soma+=dicionario.get(c[d])
        if soma == 1:
            certo+=1
    print(certo)
