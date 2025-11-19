from datetime import date
class Usuario:
    def __init__(self, nome, celular, gmail, senha):
        self.nome = nome
        self.celular = celular
        self.gmail = gmail
        self.senha = senha
    
    def imprimir_informacao(self):
        print(f"Nome: {self.nome}\nCelular: {self.celular}\nGmail: {self.gmail}\nSenha: {self.senha}")

class Assinatura_mensal(Usuario):
    def __init__(self, nome, celular, gmail, senha):
        super().__init__(nome, celular, gmail, senha)
        self.data = date.today
    
class Assinatura_anual(Usuario):
    def __init__(self, nome, celular, gmail, senha):
        super().__init__(nome, celular, gmail, senha)
        self.data = date.today

class Empresa(Usuario):
    def __init__(self, nome, celular, gmail, senha):
        super().__init__(nome, celular, gmail, senha)





    

