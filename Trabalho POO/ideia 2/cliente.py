
class Cliente:
    def __init__(self, id, nome, endereco, telefone):
        self.id = id
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone

    def atualizar(self, id, nome, endereco, telefone):
        self.id = id
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone

    def exibirInformacoes(self):
        print(f"id: {self.id}\nNome: {self.nome}\nEndereço: {self.endereco}\nTelefone: {self.telefone}")
    

    
