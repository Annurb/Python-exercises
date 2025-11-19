class Noticias:
    def __init__(self, titulo,autor, linhafina, texto):
        self.titulo = titulo
        self.linhafina = linhafina
        self.texto = texto
        self.autor = autor

    def getTitulo(self):
        return self.titulo    

    def imprimir_noticia(self):
        print(f"\n{self.titulo}\nAutor{self.autor}\n{self.linhafina}\n{self.texto}")

