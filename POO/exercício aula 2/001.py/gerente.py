from funcionario import Funcionario

class Gerente(Funcionario):
    def __init__(self, nome, salario, departamento):
        super().__init__(nome, salario)
        self.departamento = departamento

    def getDepartamento(self):
        return self.departamento
    
    def setDepartamento(self, departamento ):
        self.departamento = departamento
    
    def __str__(self):
        super().__str__()
        print(f"Departamento: {self.departamento}")
        