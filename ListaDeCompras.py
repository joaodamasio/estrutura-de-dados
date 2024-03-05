class ListaDeCompras:
    
    def __init__(self):
        self.itens = []
        self.quantidade = []
        
    def __str__(self) -> str:
        return f'{self.itens} | {self.quantidade}'

    def adicionar_itens(self, nome_produto, quantidade):
        self.itens += [nome_produto]
        self.quantidade += [quantidade]
        
    def remover_itens(self, nome_produto):
        if nome_produto in self.itens:
            index = self.itens.index(nome_produto)
            del self.itens[index]
            del self.quantidade[index]
            print(f"O produto '{nome_produto}' foi removido do carrinho.")
        else:
            print(f"O produto '{nome_produto}' não está no carrinho.")
            
        
    def listar_item(self):
        print('Lista de itens no carrinho:')
        for i in range(len(self.itens)):
            print(f'{self.quantidade[i]} x {self.itens[i]}')
        
        
carrinho = ListaDeCompras()
carrinho.adicionar_itens('Maçã', 3)
carrinho.adicionar_itens('Beringela', 1)
carrinho.adicionar_itens('Mamão', 1)
carrinho.adicionar_itens('Leite', 2)
carrinho.remover_itens('Maçã')
carrinho.listar_item()