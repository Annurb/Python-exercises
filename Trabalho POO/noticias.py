class Noticias:
    def __init__(self, titulo, linhafina, texto):
        self.titulo = titulo
        self.linhafina = linhafina
        self.texto = texto

    def getTitulo(self):
        return self.titulo    

    def imprimir_noticia(self):
        print(f"\n{self.titulo}\n{self.linhafina}\n{self.texto}")

