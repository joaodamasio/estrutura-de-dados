class No:
    def __init__(self, chave):
        self.chave = chave
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, chave):
        if self.raiz is None:
            self.raiz = No(chave)
        else:
            self._inserir_recursivo(chave, self.raiz)

    def _inserir_recursivo(self, chave, no_atual):
        if chave < no_atual.chave:
            if no_atual.esquerda is None:
                no_atual.esquerda = No(chave)
            else:
                self._inserir_recursivo(chave, no_atual.esquerda)
        elif chave > no_atual.chave:
            if no_atual.direita is None:
                no_atual.direita = No(chave)
            else:
                self._inserir_recursivo(chave, no_atual.direita)
        else:
            # Chave já existe na árvore
            pass

    def em_ordem(self):
        self._em_ordem_recursivo(self.raiz)

    def _em_ordem_recursivo(self, no_atual):
        if no_atual:
            self._em_ordem_recursivo(no_atual.esquerda)
            print(no_atual.chave)
            self._em_ordem_recursivo(no_atual.direita)

    def imprimir_arvore(self):
        self._imprimir_recursivo(self.raiz, 0)

    def _imprimir_recursivo(self, no_atual, nivel):
        if no_atual:
            self._imprimir_recursivo(no_atual.direita, nivel + 1)
            print("    " * nivel + str(no_atual.chave))
            self._imprimir_recursivo(no_atual.esquerda, nivel + 1)

# Exemplo de uso:
arvore = ArvoreBinaria()
arvore.inserir(5)
arvore.inserir(3)
arvore.inserir(7)
arvore.inserir(1)
arvore.inserir(4) 
arvore.inserir(2) 
arvore.inserir(7) 
arvore.inserir(8) 


print("Árvore binária:")
arvore.imprimir_arvore()
