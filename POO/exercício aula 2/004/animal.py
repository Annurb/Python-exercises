class Animal:
    def __init__(self, nome, idade, peso, dono, raca, pelo):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.dono = dono
        self.raca = raca
        self.pelo = pelo

    def getNome(self):
        return self.nome
    
    def restricao_alimentar(self):
        print("Este cão não possui restrição alimentar")

    def imprimir_informacao(self):
        print(f"\nNome do cão: {self.nome}\nIdade do cão: {self.idade}")
        print(f"Peso: {self.peso}\nDono: {self.dono}\nRaça: {self.raca}")
        print(f"Pelo: {self.peso}")

    def cachorro_idoso(self):
        idade = []
        nome = []
        print("Cachorro mais idoso: ")
        self.idade = str(self.idade)
        for item in self.idade:
            idade.append(item)
            nome.append(self.nome)
        for c in range(len(self.idade)):
            if max(idade) == self.idade[c]:
                print(nome[c])
        self.idade = int(self.idade)

