from cao import Cao

class Vip(Cao):
    def __init__(self, nome, peso, raca, banho):
        super().__init__(nome, peso, raca, banho)
    def restricao_alimentar(self):
        print(f"Possui restrição: {self.restricao}")
    def restricao(self, restricao):
        if restricao:
            self.restricao = "Sim"
        else:
            self.restricao = "Não"
    def imprimir_informacao(self):
        super().imprimir_informacao()
        print(f"Possui restrição alimentar: {self.restricao}")
        print("Possui 20% de desconto no pacote banho e tosa")

    def mensalidade(self):
        super().mensalidade()
        novamensalidade = self.mensalidade*0.8
        print(f"Com os descontos, a nova mensalidade fica R${novamensalidade}")
