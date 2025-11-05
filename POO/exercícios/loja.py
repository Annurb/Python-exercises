class Loja_de_roupas:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def consulta_preco(self):
        return self.preco
    
    def consulta_quantidade(self):
        return self.quantidade

