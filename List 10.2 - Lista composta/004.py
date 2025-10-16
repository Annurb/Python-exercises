import random
print("""----------------------------
    JOGA NA MEGA SENA
----------------------------""")
n = int(input("Quantos jogos quer que eu sorteie? "))
print("-=-=-= SORTEANDO 4 JOGOS -=-=-=")
for c in range(n):
    lista = []
    for d in range(6):
        lista.append(random.randint(1, 60))
    print(f"Jogo {c+1}: {lista}")
print("-=-=-=-=-= < BOA SORTE! > -=-=-=-=-=")