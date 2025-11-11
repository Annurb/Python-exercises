from animal import Animal

class Ave(Animal):
    def __init__(self, nome, especie, idade, envergadura_asas):
        super().__init__(nome, especie, idade)
        self.envergadura_asas = envergadura_asas

    def pode_voar(self, especie):
        if especie == "pinguim" or especie == "avestruz":
            return False
        else: 
            return True   

    def getNome(self):
        return self.nome   

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Envergadura das asas: {self.envergadura_asas}")

