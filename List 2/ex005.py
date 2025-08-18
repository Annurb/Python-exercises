#Questao 5
renda = float(input("Renda: R$ "))

if renda < 2000:
    imposto = "Isento"
    print(imposto)
elif renda <= 3000:
    imposto = (renda-2000)*0.08
    print(f"R$ {imposto:.2f}")
elif renda <= 4500:
    imposto = (renda - 3000)*0.18 +(1000)*0.08
    print(f"R$ {imposto:.2f}")
else:
    imposto = (renda - 4500)*0.28 + (1500)*0.18 +(1000)*0.08
    print(f"R$ {imposto:.2f}")