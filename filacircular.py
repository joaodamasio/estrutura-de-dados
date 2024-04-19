class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def enqueue(self, item):
        if (self.rear + 1) % self.size == self.front:
            print("A fila está cheia!")
            return

        elif self.front == -1:
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = item
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = item

    def dequeue(self):
        if self.front == -1:
            print("A fila está vazia!")
            return None, -1 

        temp = self.queue[self.front]
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return temp, self.front

    def display(self):
        if self.front == -1:
            print("A fila está vazia!")
            return
        elif self.rear >= self.front:
            print("Elementos na fila: ", end=" ")
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
            print()
        else:
            print("Elementos na fila: ", end=" ")
            for i in range(self.front, self.size):
                print(self.queue[i], end=" ")
            for i in range(0, self.rear + 1):
                print(self.queue[i], end=" ")
            print()


def main():
    size = int(input("Digite o tamanho da fila circular: "))
    queue = CircularQueue(size)

    while True:
        print("\nEscolha uma operação:")
        print("1. Adicionar à fila")
        print("2. Remover da fila")
        print("3. Mostrar fila")
        print("4. Sair")

        choice = input("Opção: ")

        if choice == "1":
            item = input("Digite o item a ser adicionado: ")
            queue.enqueue(item)
        elif choice == "2":
            item, new_front = queue.dequeue()
            if new_front != -1:
                print(f"Item removido: {item}")
        elif choice == "3":
            queue.display()
        elif choice == "4":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()


