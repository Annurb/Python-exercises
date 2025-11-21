import datetime

#Livro
class Livro:
    def __init__(self, titulo, autor, genero, preco, quantidadeEstoque):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.preco = preco
        self.quantidadeEstoque = quantidadeEstoque


    def adicionarEstoque(self, quantidade):
        self.quantidadeEstoque += quantidade

    
    def removerEstoque(self, quantidade):
        if self.quantidadeEstoque>0:
            self.quantidadeEstoque -= quantidade
            return 1
        else:
            print("Este livro não tem mais no estoque")
            return 0 

    def exibirDetalhes(self):
        print(f"\nTítulo: {self.titulo}\nAutor: {self.autor}\nGênero: {self.genero}\nPreço: R${self.preco}\nQuantidade em estoque: {self.quantidadeEstoque}")

    def getPreco(self):
        return self.preco
    
    def getNome(self):
        return self.titulo

#Composição
class LivroFisicoLuxo:
    def __init__(self, titulo, livroBase: Livro, precoLuxo, luxo):
        self.titulo = titulo
        self.autor = livroBase.autor
        self.genero = livroBase.genero
        self.preco = precoLuxo
        self.quantidadeEstoque = luxo
    
    def exibirDetalhes(self):
        print(f"\nTítulo: {self.titulo}\nTipo: edição de luxo\nAutor: {self.autor}\nGênero: {self.genero}\nPreço: R${self.preco}\nQuantidade em estoque: {self.quantidadeEstoque}")

class Ebook:
    def __init__(self,titulo, livroBase: Livro, precoEbook):
        self.titulo = titulo
        self.autor = livroBase.autor
        self.genero = livroBase.genero
        self.preco = precoEbook
    
    def exibirDetalhes(self):
        print(f"\nTítulo: {self.titulo}\nTipo: ebook\nAutor: {self.autor}\nGênero: {self.genero}\nPreço: R${self.preco}")

#Venda
class Venda:
    def __init__(self, cpf, cliente, carrinho):
        self.cpf = cpf
        self.cliente = cliente
        self.listaDeLivros = carrinho
        self.dataVenda = datetime.datetime.today()
        self.formaDePagamento = ""
        self.valorTotal = 0
        self.frete = 0

    def calcularFrete(self, estado):
        regiao = regioes.get(estado.upper())
        self.regiao = regiao

        if self.regiao == "Norte":
            self.frete = 5
        elif self.regiao == "Nordeste":
            self.frete = 10
        elif self.regiao == "Centro-Oeste":
            self.frete = 10
        elif self.regiao == "Sudeste":
            self.frete = 15
        else: 
            self.frete = 20
        print(f"Valor do frete: R$ {self.frete:.2f}")

    def formaDePagar(self, formaDePagamento):
        self.formaDePagamento = formaDePagamento

    def calculaTotal(self):
        self.valorTotal = self.listaDeLivros.calcularTotal() + self.frete
        return self.valorTotal
    
    def imprimirVenda(self):
        print(f"\nNome do cliente: {self.cliente}\nCPF: {self.cpf}\nData Da venda: {self.dataVenda}\nForma de pagamento: {self.formaDePagamento}\nValor total da compra: R${self.valorTotal}")
        print("\nLivros comprados:")

        for livro in self.listaDeLivros.livros:
            print(f"- {livro.titulo} (R${livro.preco})\n")
    
class Carrinho:
    def __init__(self):
        self.livros = []
    
    def adicionar(self, livro):
        self.livros.append(livro)

    def remover(self, livro):
        self.livros.remove(livro)
    
    def calcularTotal(self):
        total = 0
        for c in range(len(self.livros)):
            total += self.livros[c].getPreco()
        return total

#Regioes
regioes = {"AC": "Norte", "AL": "Nordeste", "AP": "Norte","AM": "Norte",
"BA": "Nordeste","CE": "Nordeste","DF": "Centro-Oeste","ES": "Sudeste", "GO": "Centro-Oeste","MA": "Nordeste","MT": "Centro-Oeste","MS": "Centro-Oeste","MG": "Sudeste","PA": "Norte","PB": "Nordeste","PR": "Sul","PE": "Nordeste","PI": "Nordeste","RJ": "Sudeste","RN": "Nordeste","RS": "Sul","RO": "Norte","RR": "Norte","SC": "Sul","SP": "Sudeste","SE": "Nordeste","TO": "Norte" }