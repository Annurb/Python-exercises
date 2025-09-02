#Questao 2
a, b, c = input("Digite trê números inteiros: ").split()
a = int(a)
b = int(b)
c = int(c)
if a>=b and a>=c:
    if b>=c:
        print(f"{a}>{b}>{c}")
    else:
        print(f"{a}>{b}>{c}")
elif b>=a and b>=c:
    if a>=c:
        print(f"{b}>{a}>{c}")
    else:
        print(f"{b}>{c}>{a}")
else:
    if b>=a:
        print(f"{c}>{b}>{a}")
    else:
        print(f"{c}>{a}>{b}")
