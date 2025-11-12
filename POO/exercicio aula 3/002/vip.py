from conta import Conta

class Vip(Conta):
    def __init__(self, nome, saldo, limite, tempo ):
        super().__init__(nome, saldo, limite, tempo)

    def getNome(self):
        return self.nome    
    
    def emprestimo(self, dinheiro, mes):
        if self.tempo >= 10:
            parcela = (dinheiro/mes)*1.03
            print(f"Emprestimo aceito! Suas parcelas por mês serão de R${parcela:.2f} ")
        else:
            parcela = (dinheiro/mes)*1.05
            print(f"Emprestimo aceito! Suas parcelas por mês serão de R${parcela:.2f} ")