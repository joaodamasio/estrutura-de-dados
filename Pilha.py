class Livro:
    def __init__(self, titulo, qtd_paginas):
        self.titulo = titulo
        self.qtd_paginas = qtd_paginas
        
class PilhaDeLivros:
    def __init__(self):
        self.pilhaLivros = []
        
    def adiconar_livro(self, titulo, qtd_paginas):
        novo_livro = Livro(titulo, qtd_paginas)
        return self.pilhaLivros.append(novo_livro)
    
    def remover_livro(self):
        if self.pilhaLivros is None:
            return 
        else:
            return self.pilhaLivros.pop()
            
    def listar_livros(self):
        if self.pilhaLivros is None:
            print("Não há livros nesta lista")
            return
        else:
            for livro in self.pilhaLivros:
                print(f"Livro: {livro.titulo}, Número de Páginas: {livro.qtd_paginas}")
                
                
                
pilhaLivro = PilhaDeLivros()
pilhaLivro.adiconar_livro("Sim", 123)
pilhaLivro.adiconar_livro("Não", 124)
pilhaLivro.adiconar_livro("Talvez", 125)
pilhaLivro.adiconar_livro("Com certeza", 126)

pilhaLivro.listar_livros()

pilhaLivro.remover_livro()
pilhaLivro.listar_livros()