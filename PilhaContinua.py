class Pilha:
    def __init__(self, tamanho_maximo):
        self.tamanho_maximo = tamanho_maximo
        self.itens = []

    def vazia(self):
        return len(self.itens) == 0

    def cheia(self):
        return len(self.itens) == self.tamanho_maximo

    def empilhar(self, item):
        if self.cheia():
            print("A pilha está cheia. Não é possível empilhar mais itens.")
        else:
            self.itens.append(item)

    def desempilhar(self):
        if self.vazia():
            print("A pilha está vazia. Não é possível desempilhar.")
        else:
            return self.itens.pop()

    def topo(self):
        if self.vazia():
            print("A pilha está vazia.")
            return None
        else:
            return self.itens[-1]

    def tamanho(self):
        return len(self.itens)
        
    def mostrar_pilha(self):
        if self.vazia:
            print("Está vazia")
        else:
            print("Elementos da pilha")
            for item in reversed(self.item):
                print(item)

# Exemplo de uso:
tamanho_pilha = int(input("Digite o tamanho da pilha: "))
pilha = Pilha(tamanho_pilha)

while True:
    print("\nEscolha uma opção:")
    print("1. Empilhar")
    print("2. Desempilhar")
    print("3. Verificar o topo")
    print("4. Verificar se a pilha está vazia")
    print("5. Verificar se a pilha está cheia")
    print("6. Tamanho da pilha")
    print("7. Mostrar elementos da pilha")
    print("8. Sair")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == '1':
        item = input("Digite o item que deseja empilhar: ")
        pilha.empilhar(item)
    elif opcao == '2':
        item_desempilhado = pilha.desempilhar()
        if item_desempilhado is not None:
            print("Item desempilhado:", item_desempilhado)
    elif opcao == '3':
        print("Topo da pilha:", pilha.topo())
    elif opcao == '4':
        print("A pilha está vazia?" if pilha.vazia() else "A pilha não está vazia.")
    elif opcao == '5':
        print("A pilha está cheia?" if pilha.cheia() else "A pilha não está cheia.")
    elif opcao == '6':
        print("Tamanho da pilha:", pilha.tamanho())
    elif opcao == '7':
        self.mostrar_pilha()
    elif opcao == '8':
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")
