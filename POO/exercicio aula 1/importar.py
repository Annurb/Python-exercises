from funcionario import Funcionario

f1 = Funcionario("Ana", 2000)
f2 = Funcionario("Carlos", 5000)
f3 = Funcionario("Livia", 10000)

f1.altera_salario(2000)
f2.altera_salario(5000)
f3.altera_salario(10000)

print(f1.nome, ":" , f1.novosalario)
print(f2.nome, ":" , f2.novosalario)
print(f3.nome, ":" , f3.novosalario)