class Paciente:
    def __init__(self, nome_paciente, id, estado_saude) -> None:
        self.nome_paciente = nome_paciente
        self.id = id
        self.estado_saude = estado_saude
        self.proximo = None
        
class ListaDePaciente:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        
    def adicionar_paciente(self, nome, id, estado):
        novo_paciente = Paciente(nome, id, estado)
        
        if self.head is None:
            self.head = novo_paciente
            self.tail = novo_paciente
            
        else:
            self.tail.proximo = novo_paciente
            self.tail = novo_paciente
            
    def remover_paciente(self, id):
        if self.head is None:
            return
        elif self.head.id == id:
            self.head = self.head.proximo
            if self.head is None:
                self.tail = None
            return
        else:
            paciente_atual = self.head
            while paciente_atual.proximo is not None:
                if paciente_atual.proximo.id == id:
                    paciente_atual.proximo = paciente_atual.proximo.proximo
                    if paciente_atual.proximo is None:
                        self.tail = paciente_atual
                        return
                    paciente_atual = paciente_atual.proximo
    
    def listar_pacientes(self):
        if self.head is None:
            print('Não há pacientes nesta lista')
        else:
            paciente_atual = self.head
            while paciente_atual is not None:
                print(f'Nome: {paciente_atual.nome_paciente}, ID: {paciente_atual.id}, Estado de saúde: {paciente_atual.estado_saude}')
                paciente_atual = paciente_atual.proximo
            
            

lista_pacientes = ListaDePaciente()

lista_pacientes.adicionar_paciente('Joao', 101,'estavel')
lista_pacientes.adicionar_paciente('Maria', 123, 'tratamento')

lista_pacientes.listar_pacientes()