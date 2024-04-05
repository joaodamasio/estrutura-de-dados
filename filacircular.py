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


# Criando uma fila circular de tamanho 5
cq = CircularQueue(5)
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
cq.enqueue(4)
cq.enqueue(5)
cq.enqueue(6)
cq.display()



print("Removendo um elemento da fila: ")
removed_value, next_front = cq.dequeue()
if removed_value is not None:
    print("Valor removido:", removed_value)
    print("Nova posição de front:", next_front)
cq.display()


