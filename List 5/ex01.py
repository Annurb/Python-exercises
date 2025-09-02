#Questao 1
import random
parada = 0
while parada == 0:
    escolhapc = random.choice(["pedra", "papel", "tesoura"])
    escolha = input("Escolha pedra, papel ou tesoura: ").lower()
    if escolhapc == escolha:
        print(f"O computador escolheu {escolhapc}, o jogo deu EMPATE")
    elif escolhapc == "pedra" and escolha == "tesoura" or escolhapc == "tesoura" and escolha =="papel" or escolhapc == "papel" and escolha == "pedra":
        print(f"O computador escolheu {escolhapc}, você PERDEU")
    else:
        print(f"O computador escolheu {escolhapc}, você GANHOU")
    sn = str(input("Deseja continuar jogando? [S/N]")).upper()
    if sn == "N":
        parada = 1 