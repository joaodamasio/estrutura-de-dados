def busca_binaria(array, alvo):
    inicio = 0
    fim = len(array) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if array[meio] == alvo:
            return meio
        elif array[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1

    return -1

def ler_array():
    array = input("Digite os elementos do array separados por espaço: ").split()
    return [int(x) for x in array]

def ler_alvo():
    return int(input("Digite o elemento que deseja buscar: "))

def main():
    array = ler_array()
    alvo = ler_alvo()
    resultado = busca_binaria(array, alvo)
    if resultado != -1:
        print(f'O elemento {alvo} foi encontrado no índice {resultado}.')
    else:
        print(f'O elemento {alvo} não foi encontrado no array.')

if __name__ == "__main__":
    main()
