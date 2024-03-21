class Fila:
    def __init__(self, tamanho_máximo):
        self.tamanho_maximo = tamanho_máximo
        self.itens = []
        
#inclusao

    def inserir_na_fila(self, item):
        if len(self.itens) == self.tamanho_maximo:
            print('A lista está cheia')
        else:
            self.itens += [item]
            return self.itens

#exclusao

    def excluir_item_da_fila(self):
        if len(self.itens) == 0:
            print('A lista está vazia')
            
        else:
            self.itens.pop(0)

            
            
#mostrar fila

    def mostrar_fila(self):
        if len(self.itens) == 0:
            print('A fila está vazia')
        else:
            print("Elementos da fila:")
            for item in self.itens:
                print(item)

tamanho_fila = 8
fila = Fila(tamanho_fila)

