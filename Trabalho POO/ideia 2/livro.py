import datetime
class Livro:
    def __init__(self, id, titulo, autor, genero, preco, quantidadeEstoque):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.preco = preco
        self.quantidadeEstoque = quantidadeEstoque


    def adicionarEstoque(self, quantidade):
        self.quantidadeEstoque += quantidade
    
    def removerEstoque(self, quantidade):
        self.quantidadeEstoque -= quantidade

    def exibirDetalhes(self):
        print(f"Id: {self.id}\nTítulo: {self.titulo}\nAutor: {self.autor}\nGênero: {self.genero}\nPreço: R${self.preco}\nQuantidade em estoque: {self.quantidadeEstoque}")

    def getPreco(self):
        return self.preco
    
    def getTipo(self):
        return "Livro físico"
    
class LivroFisicoLuxo(Livro):
    def getTipo(self):
        return "Livro físico edição de luxo"

class Ebook(Livro):
    def getTipo(self):
        return "Livro digital"

#Venda
class Venda:
    def __init__(self, id, cliente, formaDePagamento):
        self.id = id
        self.cliente = cliente
        self.listaDeLivros = Carrinho()
        self.dataVenda = datetime.datetime.today()
        self.formaDePagamento = formaDePagamento
        self.valorTotal = Carrinho.calcularTotal()
    
    def calcularTotal(self):
        return self.carrinho.calcularTotal()
    
class Carrinho:
    def __init__(self):
        self.livros =[]
    
    def adicionar(self, livro):
        self.livros.append(livro)

    def remover(self, livro):
        self.livros.remove(livro)
    
    def calcularTotal(self):
        total = 0
        for c in range(len(self.livros)):
            total += self.livros[c].getPreco()
        return total
    