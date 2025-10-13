par = []
impar = []
numeros = []
for c in range(10):
    num = int(input())
    if num%2 == 0:
        par.append(num)
    else:
        impar.append(num)
par.sort()
impar.sort()
numeros.append(par)
numeros.append(impar)

print(f"Números pares: {numeros[0]}")
print(f"Números ímpares: {numeros[1]}")