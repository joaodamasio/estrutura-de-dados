class Produto:
    def __init__(self, id, nome, qtd_estoque):
        self.id = id
        self.nome = nome
        self.qtd_estoque = qtd_estoque

class Node:
    def __init__(self, produto):
        self.esquerda = None
        self.direita = None
        self.produto = produto

class ArvoreProduto:
    def __init__(self):
        self.raiz = None
        
    def inserir(self, id, nome, qtd):
        produto = Produto(id, nome, qtd)
        if self.raiz is None:
            self.raiz = Node(produto)
        else:
            self._inserir(produto, self.raiz)
    
    def _inserir(self, produto, node):
        if produto.id < node.produto.id:
            if node.esquerda is None:
                node.esquerda = Node(produto)
            else:
                self._inserir(produto, node.esquerda)
        elif produto.id > node.produto.id:
            if node.direita is None:
                node.direita = Node(produto)
            else:
                self._inserir(produto, node.direita)
        else:
            node.produto = produto
    
    def buscar(self, id):
        return self._buscar(id, self.raiz)
    
    def _buscar(self, id, node):
        if node is None or node.produto.id == id:
            return node
        elif id < node.produto.id:
            return self._buscar(id, node.esquerda)
        else:
            return self._buscar(id, node.direita)

def interacao_usuario():
    arvore = ArvoreProduto()
    
    while True:
        print("\n1. Inserir produto")
        print("2. Buscar produto por ID")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            id = int(input("Digite o ID do produto: "))
            nome = input("Digite o nome do produto: ")
            qtd = int(input("Digite a quantidade em estoque: "))
            arvore.inserir(id, nome, qtd)
            print("Produto inserido com sucesso!")
        elif escolha == "2":
            id = int(input("Digite o ID do produto que deseja buscar: "))
            produto_encontrado = arvore.buscar(id)
            if produto_encontrado:
                print(f"Produto encontrado - Nome: {produto_encontrado.produto.nome}, Quantidade em Estoque: {produto_encontrado.produto.qtd_estoque}")
            else:
                print("Produto não encontrado.")
        elif escolha == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha novamente.")

interacao_usuario()
