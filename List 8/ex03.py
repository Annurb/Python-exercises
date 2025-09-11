#Questão 3 
n = int(input())
while not(1<=n<=1000):
    n = int(input("Digite novamente: "))
for c in range(n):
    led = 0
    v = int(input())
    while not(1<=v<=10**100):
        v = int(input("Digite novamente: "))
    v = str(v)
    for m in v:
        match(m):
            case "1":
                led +=2 
            case "2":
                led+=5
            case "3":
                led+=5
            case "4":
                led+=4
            case "5":
                led+=5
            case "6":
                led+=6
            case "7":
                led+=3
            case "8":
                led+=7
            case "9":
                led+=6
            case "0":
                led+=6
    print(f"{led} leds")