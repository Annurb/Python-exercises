class Animal:
    def __init__(self, nome, especie, idade):
        self.nome = nome
        self.especie = especie
        self.idade = idade

    def getNome(self):
        return self.nome
    
    def getEspecie(self):
        return self.especie
    
    def getIdade(self):
        return self.idade
    
    def exibir_informacoes(self):
        print(f"\nNome:{self.nome}\nEspecie: {self.especie}\nIdade: {self.idade}")
    
