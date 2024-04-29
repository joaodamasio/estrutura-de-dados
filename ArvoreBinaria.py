class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self._inserir_recursivamente(self.raiz, valor)

    def _inserir_recursivamente(self, no, valor):
        if valor < no.valor:
            if no.esquerda is None:
                no.esquerda = No(valor)
            else:
                self._inserir_recursivamente(no.esquerda, valor)
        else:
            if no.direita is None:
                no.direita = No(valor)
            else:
                self._inserir_recursivamente(no.direita, valor)

    def imprimir_pre_ordem(self, no):
        if no is not None:
            print(no.valor, end=" ")
            self.imprimir_pre_ordem(no.esquerda)
            self.imprimir_pre_ordem(no.direita)

    def imprimir_em_ordem(self, no):
        if no is not None:
            self.imprimir_em_ordem(no.esquerda)
            print(no.valor, end=" ")
            self.imprimir_em_ordem(no.direita)

    def imprimir_pos_ordem(self, no):
        if no is not None:
            self.imprimir_pos_ordem(no.esquerda)
            self.imprimir_pos_ordem(no.direita)
            print(no.valor, end=" ")


def interacao_usuario():
    arvore = ArvoreBinaria()
    
    while True:
        print("\n1. Inserir valor na árvore")
        print("2. Imprimir árvore em pré-ordem")
        print("3. Imprimir árvore em ordem")
        print("4. Imprimir árvore em pós-ordem")
        print("5. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            valor = int(input("Digite o valor que deseja inserir na árvore: "))
            arvore.inserir(valor)
            print("Valor inserido com sucesso!")
        elif escolha == "2":
            print("Imprimir em pré-ordem:")
            arvore.imprimir_pre_ordem(arvore.raiz)
        elif escolha == "3":
            print("Imprimir em ordem:")
            arvore.imprimir_em_ordem(arvore.raiz)
        elif escolha == "4":
            print("Imprimir em pós-ordem:")
            arvore.imprimir_pos_ordem(arvore.raiz)
        elif escolha == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha novamente.")

interacao_usuario()
