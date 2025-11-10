#Herança funcionário

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
        print("Criou um objeto")

    def getNome(self):
        return self.nome
    
    def getSalario(self):
        return self.salario
    
    def setNome(self, nome):
        self.nome = nome

    def setSalario(self, salario):
        self.salario = salario
    
    def __str__(self):
        print(f"\nNome do funcionário: {self.nome}\nSalário: {self.salario}")
    

