class Produto:
    def __init__(self,nome_produto, codigo, preco, qtd_estoque):
        self.nome_produto = nome_produto
        self.codigo = codigo
        self.preco = preco 
        self.qtd_estoque = qtd_estoque
        self.proximo = None
        self.anterior = None
        
        
class ListaDeProdutos:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def adicionar_produto(self, nome, codigo, preco, quantidade):
        novo_produto = Produto(nome, codigo, preco, quantidade)
        
        if self.head is None:
            self.head = novo_produto
            self.tail = novo_produto
            
        else:
            novo_produto.anterior = self.tail
            self.tail.proximo = novo_produto
            self.tail = novo_produto
            
    def remover_produto(self, codigo):
        produto_atual = self.head
        while produto_atual:
            if produto_atual.codigo == codigo:
                if produto_atual.anterior:
                    produto_atual.anterior.proximo = produto_atual.proximo
                else:
                    self.head = produto_atual.proximo
                if produto_atual.proximo:
                    produto_atual.proximo.anterior = produto_atual.anterior
                else:
                    self.tail = produto_atual.anterior
                return True
            produto_atual = produto_atual.proximo
        return False
    
    def atualizar_quantidade(self, codigo, quantidade):
        produto_atual = self.head
        while produto_atual:
            if produto_atual.codigo == codigo:
                produto_atual.qtd_estoque = quantidade
                return True
            produto_atual = produto_atual.proximo
        return False
    
    def buscar_por_codigo(self, codigo):
        produto_atual = self.head
        while produto_atual:
            if produto_atual.codigo == codigo:
                return produto_atual
            produto_atual = produto_atual.proximo
        return None
    
    def busca_por_nome(self, nome):
        produto_atual = self.head
        while produto_atual:
            if produto_atual.nome_produto == nome:
                return produto_atual
            produto_atual = produto_atual.proximo
        return None
    
    def listar_produto(self):
        if self.head is None:
            print('Não ha produtos na lista')
        else:
            produto_atual = self.head
            while produto_atual is not None:
                print(f'Nome do produto: {produto_atual.nome_produto} | Código: {produto_atual.codigo} | Preço: {produto_atual.preco} | Quantidade: {produto_atual.qtd_estoque}')
                produto_atual = produto_atual.proximo
            
            
produto = ListaDeProdutos()
produto.adicionar_produto('Mamao', 12314, 'R$4', '4kg')
produto.adicionar_produto('limao', 34524, 'R$2', '9kg')
produto.adicionar_produto('laranja', 625624, 'R$5', '10kg')
produto.adicionar_produto('batata', 76452, 'R$1', '8kg')
produto.listar_produto()
        