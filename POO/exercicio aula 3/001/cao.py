class Cao:
    def __init__(self, nome, peso, raca, banho):
        self.nome = nome
        self.peso = peso
        self.raca = raca
        self.banho = banho


    def getNome(self):
        return self.nome
    
    def getPeso(self):
        return self.peso

    def imprimir_informacao(self):
        print(f"\nNomme do animal: {self.nome}\nPeso: {self.peso}\nRaça: {self.raca}\nBanho: {self.banho}")

    def restricao_alimentar(self):
        print("Este cão não possui restrição alimentar")

    def mensalidade(self):
        self.mensalidade = self.banho*25
        if self.raca == "pitbull" or self.raca == "pincher":
            self.mensalidade =self.mensalidade*1.15
        if self.peso >20:
            self.mensalidade = self.mensalidade*1.10
        print(f"Mensalidade: R${self.mensalidade:.2f}")

            
        

