# implementando herança

class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
        print("criou um objeto")
        
    def getNome(self):
        return self.nome
    
    def getIdade(self):
        return self.idade
    
    def setNome(self,nome):
        self.nome = nome
        
    def setIdade(self,idade):
        self.idade = idade

    def __str__(self):
        print(f"\nNome: {self.nome}  \nIdade: {self.idade}")
        
        
#