class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_dados(self):
        print(f"\nMarca: {self.marca} \nModelo: {self.modelo}\nAno: {self.ano}")
