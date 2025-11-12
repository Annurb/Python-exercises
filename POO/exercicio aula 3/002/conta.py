class Conta:
    def __init__(self, nome, saldo, limite, tempo):
        self.nome = nome
        self.saldo = saldo
        self.limite = limite
        self.tempo = tempo

    def getNome(self):
        return self.nome
    
    def imprimir_informacao(self):
        print(f"\nNome: {self.nome} \nSaldo: {self.saldo}\nLimite: {self.limite}\nTempo: {self.tempo}")

    def emprestimo(self, dinheiro, mes):
        if self.tempo >= 10:
            parcela = (dinheiro/mes)*1.10
            print(f"Emprestimo aceito! Suas parcelas por mês serão de R${parcela:.2f} ")
        else:
            print(f"o cliente {self.nome} não está habilitado pra isso")

    def sacar(self, sacado):
        if sacado <= self.saldo and sacado <= self.limite:
            self.saldo = self.saldo - sacado
            print(f"Dinheiro transferido, seu saldo é de R$ {self.saldo:.2f}")
        else:
            print("Saldo ou limite insuficiente.")
    
    def depositar(self, deposito):
        self.saldo = self.saldo + deposito
        print(f"Dinheiro depositado, seu novo saldo é de R$ {self.saldo:.2f}")
    
    def consultar_saldo(self):
        print(f"Seu saldo é de R${self.saldo:.2f}")


    