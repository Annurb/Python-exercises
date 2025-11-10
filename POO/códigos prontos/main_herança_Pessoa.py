'''
Implementar um algoritmo que defina a classe Pessoa,
com 3 propriedades: nome, idade, identificação
(considerando que uma pessoa pode ser
Pessoa Física (possui cpf) ou Pessoa Jurídica (possui cnpj)
'''

from herança_PessoaFisica import PessoaFisica
from herança_PessoaJuridica import PessoaJuridica


#main
p1 = PessoaFisica("Ana Maria", 30, "927.715.678-09")
pf1 = PessoaFisica("JOao",45, "123.456.789-09")
p2 = PessoaJuridica("Angeloni", 50, "11.222.333/0001-99")


print(p1.getNome())
print(p1.getCpf())
print(p2.getNome())


p1.__str__()
p2.__str__()

