#Livro

class Livro:
    def __init__(self, titulo, autor, total_pag, pag_lidas = 0):
        self.titulo = titulo
        self.autor = autor
        self.total_pag = total_pag
        self.pag_lidas = pag_lidas

    def ler(self):
        if self.pag_lidas <= self.total_pag:
            print("Total de paginas lidas: ", self.pag_lidas , " páginas")
        else:
            print("Valor incorreto, páginas lidas não pode ultrapassar a quantidade de páginas do livro")

    def porcentagem_lida(self):
        porcentagem = (self.pag_lidas / self.total_pag) * 100
        return f"Porcentagem de leitura: {round(porcentagem)}%"

    def paginas_restantes(self):
        resto = self.total_pag - self.pag_lidas
        return f"Páginas restantes: {resto}"

    def terminou(self):
        if self.pag_lidas == self.total_pag:
            return True
        else:
            return False

livro1 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1000)
livro2 = Livro("O Hobbit", "J.R.R. Tolkien", 450, 380)


livro1.ler()
print(livro1.porcentagem_lida())
print(livro1.paginas_restantes())
print("Terminou? " , livro1.terminou())
print("\n")
livro2.ler()
print(livro2.porcentagem_lida())
print(livro2.paginas_restantes())
print("Terminou? " , livro2.terminou())

