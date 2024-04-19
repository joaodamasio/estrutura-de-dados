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

def main():
    tamanho_maximo = int(input('Digite o tamanho máximo da fila: '))
    fila = Fila(tamanho_maximo)

    while True:
        print('\nEscolha uma operação:')
        print('1. Inserir na fila')
        print('2. Remover da fila')
        print('3. Mostrar fila')
        print('4. Sair')

        opcao = input('Opção: ')

        if opcao == '1':
            item = input('Digite o item a ser inserido na fila: ')
            fila.inserir_na_fila(item)
        elif opcao == '2':
            fila.excluir_item_da_fila()
        elif opcao == '3':
            fila.mostrar_fila()
        elif opcao == '4':
            print('Encerrando o programa...')
            break
        else:
            print('Opção inválida. Tente novamente.')

if __name__ == '__main__':
    main()

