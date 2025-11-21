
class Cliente:
    def __init__(self, nome, cpf, telefone):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone

    def getNome(self):
        return self.nome

    def atualizar(self, nome, cpf, telefone):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone

    def getCPF(self):
        return self.cpf

    def exibirInformacoes(self):
        print(f"\nNome: {self.nome}\nCPF: {self.cpf}\nTelefone: {self.telefone}")

    def isVip(self):
        return "Não"
    
class ClienteVip(Cliente):
    def __init__(self, nome, cpf, telefone):
        super().__init__(nome, cpf, telefone)

    def isVip(self):
        return "Sim"