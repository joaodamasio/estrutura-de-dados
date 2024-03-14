class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class PilhaEncadeada:
    def __init__(self, tamanho_maximo):
        self.topo = None
        self.tamanho_maximo = tamanho_maximo
        self.tamanho_atual = 0

    def esta_vazia(self):
        return self.topo is None

    def esta_cheia(self):
        return self.tamanho_atual == self.tamanho_maximo

    def empilhar(self, valor):
        if self.esta_cheia():
            print("A pilha está cheia, não é possível adicionar mais elementos.")
            return
        novo_no = No(valor)
        novo_no.proximo = self.topo
        self.topo = novo_no
        self.tamanho_atual += 1

    def desempilhar(self):
        if self.esta_vazia():
            print("A pilha está vazia, não é possível desempilhar.")
            return None
        valor_desempilhado = self.topo.valor
        self.topo = self.topo.proximo
        self.tamanho_atual -= 1
        return valor_desempilhado

    def topo_pilha(self):
        if self.esta_vazia():
            print("A pilha está vazia.")
            return None
        return self.topo.valor

    def imprimir_pilha(self):
        if self.esta_vazia():
            print("A pilha está vazia.")
            return
        temp = self.topo
        while temp:
            print(temp.valor, end=" -> ")
            temp = temp.proximo
        print("None")

# Exemplo de uso:
tamanho_maximo = int(input("Digite o tamanho máximo da pilha: "))
pilha = PilhaEncadeada(tamanho_maximo)

while True:
    print("\nOpções:")
    print("1 - Empilhar")
    print("2 - Desempilhar")
    print("3 - Mostrar o topo da pilha")
    print("4 - Imprimir a pilha")
    print("0 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        valor = input("Digite o valor a ser empilhado: ")
        pilha.empilhar(valor)
    elif opcao == 2:
        valor_desempilhado = pilha.desempilhar()
        if valor_desempilhado is not None:
            print("Valor desempilhado:", valor_desempilhado)
    elif opcao == 3:
        topo = pilha.topo_pilha()
        if topo is not None:
            print("Topo da pilha:", topo)
    elif opcao == 4:
        print("Conteúdo da pilha:")
        pilha.imprimir_pilha()
    elif opcao == 0:
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
