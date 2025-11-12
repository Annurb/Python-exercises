from animal import Animal

class Vip(Animal):
    def __init__(self, nome, idade, peso, dono, raca, pelo, alimentacao, banho):
        super().__init__(nome, idade, peso, dono, raca, pelo )
        self.alimentacao = alimentacao 
        self.banho = banho

    def restricao_alimentar(self):
        if self.alimentacao:
            print("Este cão possui restrição alimentar")
        else:
            super().restricao_alimentar(self)
    
    def imprimir_informacao(self):
        super().imprimir_informacao()
        print(f"Possui restrição alimentar: {self.alimentacao}\nBanho:{self.banho}")
    
