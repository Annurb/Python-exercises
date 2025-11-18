class Conta:
    def __init__(self, numero, nome, saldo, limite):
        print("Inicializando uma conta...")
        self.numero = numero
        self.nome = nome
        self.saldo = saldo
        self.limite = limite
        print("Conta criada com sucesso!!")
        
    def deposita(self, valor):
        self.saldo += valor
        
    def retira(self,valor):
        if self.saldo < valor:
            print("Saldo insuficiente! Saque cancelado!")
        else:    
            self.saldo -= valor
            
    def extrato(self):
        print(f"Conta: {self.numero}  -  Saldo: {self.saldo}")
        
    def transfere(self, destino, valor):
        if self.saldo > valor:
            self.saldo -= valor
            destino.saldo += valor
            