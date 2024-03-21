class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        
class Fila:
    def __init__(self, tamanho_maximo):
        self.tamanho_maximo = tamanho_maximo
        self.cabeca = None
        self.cauda = None
        self.itens = []
        
    def inserir(self,valor):
        
        if len(self.itens) == self.tamanho_maximo:
            print('A fila está cheia')
        else:
            novo_valor = No(valor)
            if self.cabeca is None:
                self.cabeca = novo_valor
                self.cauda = novo_valor
                self.itens += [valor]
            else:
                self.cauda.proximo = novo_valor
                self.cauda = novo_valor
                self.itens += [valor]
        
    def mostrar(self):
        if len(self.itens) == 0:
            print('Fila vazia')
        else:
            print('Elementos da fila')
            for item in self.itens:
                print(item)
    
    def remover(self):
        if self.cabeca is None:
            print('Fila vazia')
        else:
            self.cabeca = self.cabeca.proximo
            return f'o elemento {self.itens.pop(0)} foi removido'

    
    
    
    
tamanho_fila = 2
fila = Fila(tamanho_fila)

fila.inserir(8)
fila.inserir(6)
print(fila.remover())
fila.mostrar()
