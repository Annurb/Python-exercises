class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def altera_salario(self, salario):
        if salario <= 2000:
            novosalario = salario*1.15
        elif salario <= 3000:
            novosalario = salario*1.10
        else:
            novosalario = salario*1.05
        self.novosalario = novosalario

