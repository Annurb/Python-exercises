from veiculo import Veiculo

class Caminhao(Veiculo):
    def __init__(self, marca, modelo, ano, carga):
        super().__init__(marca, modelo, ano)
        self.carga = carga

    def capacidade_carga(self, carga):
        self.carga = carga
    def verificar_carga(self, verifica):
        if verifica <= self.carga:
            print(f"A capacidade da carga é {self.carga}, portanto, a carga pode ser transportada")
        else:
            print(f"A capacidade é {self.carga}, portanto, a carga não pode ser transportada")
    def exibir_dados(self):
        super().exibir_dados()
        print(f"Carga máxima: {self.carga}")