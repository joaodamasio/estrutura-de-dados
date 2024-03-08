class Pedido:
    def __init__(self, nmr_pedido, nome_cliente, itens_pedido, valor_total):
        self.nmr_pedido = nmr_pedido
        self.nome_cliente = nome_cliente
        self.itens_pedido = itens_pedido
        self.valor_total = valor_total
        
    def __str__(self):

        return f"Número do Pedido: {self.nmr_pedido}, Cliente: {self.nome_cliente}, Itens: {self.itens_pedido}, Valor Total: {self.valor_total}"
class FilaDePedidos:
    def __init__(self):
        self.lista_pedidos = []
        
    def adicionar_pedido(self, nmr_pedido, nome_cliente, itens_pedido, valor_total):
        novo_pedido = Pedido(nmr_pedido, nome_cliente, itens_pedido, valor_total)
        self.lista_pedidos.append(novo_pedido)
        

    def remover_pedido(self,nmr_pedido):
        for pedido in self.lista_pedidos:
            if pedido.nmr_pedido == nmr_pedido:
                self.lista_pedidos.remove(pedido)
                return
            print("O pedido não está na lista")

    def listar_pedidos(self):
        print("Lista de pedidos:")
        for pedido in self.lista_pedidos:
            print(pedido)









pedido = FilaDePedidos()
pedido.adicionar_pedido(1,"Roberto", "Bolonhesam, Bife, Frango", "R$18")
pedido.adicionar_pedido(2,"Roberto", "Bolonhesam, Bife, Frango", "R$18")
pedido.adicionar_pedido(3,"Roberto", "Bolonhesam, Bife, Frango", "R$18")
pedido.adicionar_pedido(4,"Roberto", "Bolonhesam, Bife, Frango", "R$18")
pedido.adicionar_pedido(5,"Roberto", "Bolonhesam, Bife, Frango", "R$18")

pedido.listar_pedidos()
