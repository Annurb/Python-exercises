#conta_historico.py
import datetime
class Historico():
    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes=[]    
    def imprime(self):
        print("data abertura: {}".format(self.data_abertura))
        print("transações: ")
        for t in self.transacoes:
            print("-", t)
            
class Conta():
    def __init__(self, numero, cliente, saldo, limite):
        self.numero = numero
        self.cliente = cliente
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()
    
    def deposita(self, valor):
        self.saldo += valor
        self.historico.transacoes.append("depósito de {}".format(valor))
        
    def retira(self,valor):
        if self.saldo < valor:
            print("Saldo insuficiente! Saque cancelado!")
        else:    
            self.saldo -= valor
            self.historico.transacoes.append("saque de {}".format(valor))
            
    def extrato(self):
        print(f"Conta: {self.numero}  -  Saldo: {self.saldo}")
        self.historico.transacoes.append(f"tirou extrato - saldo de {self.saldo}")
        
    def transfere(self, destino, valor):
        if self.saldo > valor:
            self.saldo -= valor
            destino.saldo += valor
            self.historico.transacoes.append(f"transferencia de {valor} para conta {destino.numero}")
            