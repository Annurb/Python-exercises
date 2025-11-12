from conta import Conta
from vip import Vip

lista = []
p1 = Conta("Lisa", 12, 20, 10)
lista.append(p1)
p2 = Vip("Flavio", 300, 200, 1)
lista.append(p2)

while True:
    continua = input("Deseja continuar? ").upper()
    if continua[0] == "N":
        break
    menu = int(input("""Escolha uma opção:
1 - Cadastrar conta
2 - Sacar dinheiro
3 - Depositar dinheiro
4 - Solicitar empréstimo
5 - Consultar saldo
""" ))
    if menu == 1:
        isvip = input("A conta é VIP? ").upper()
        nome = str(input("Nome do cliente: ")).title()
        saldo = float(input("Digite o saldo: "))
        limite = float(input("Digite o limite da conta: "))
        tempo = int(input("Quantos anos tem a conta: "))

        if isvip == "S":
            cliente = Vip(nome, saldo, limite, tempo)
        else:
            cliente = Conta(nome, saldo, limite, tempo)
    
        lista.append(cliente)

        cliente.imprimir_informacao()

    if menu == 4:
        client = input("Digite o nome do cliente: ").title()
        dinheiro = int(input("Emprestimo necessário: "))
        mes = int(input("Quantos meses (maximo de 12 meses) : "))

        for c in lista:
            if c.getNome() == client:
                c.emprestimo(dinheiro, mes)

    if menu == 2:
        client1 = input("Digite o nome do cliente: ").title()
        sacado = float(input("Quanto sacar: "))
        for d in lista:
            if d.getNome() == client1:
                d.sacar(sacado)

    if menu == 3:
        client2 = input("Digite o nome do cliente: ").title()
        deposito = float(input("Depósito: "))
        for d in lista:
            if d.getNome() == client2:
                d.depositar(deposito)

    if menu == 5:
        client3 = input("Digite o nome do cliente: ").title()
        for f in lista:
            if f.getNome() == client3:
                f.consultar_saldo()






