class Paciente:
    def __init__(self, nome_paciente, id_paciente, estado_saude) -> None:
        self.nome_paciente = nome_paciente
        self.id_paciente = id_paciente
        self.estado_saude = estado_saude
        self.proximo = None
        
class ListaDePaciente:
    def __init__(self) -> None:
        self.primeiro = None
        
    def adicionar_paciente(self, nome, id, estado):
        novo_paciente = Paciente(nome, id, estado)
        
        if self.primeiro is None:
            self.primeiro = novo_paciente
            
        else:
            atual = self.primeiro
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_paciente
            
    def remover_paciente(self, id):
        atual = self.primeiro
        anterior = None
        while atual:
            if atual.id_paciente == id:
                if anterior:
                    anterior.proximo = atual.proximo
                else:
                    self.primero = atual.proximo
                    
                return True
            anterior = atual
            atual = atual.proximo
        return False
    
    def listar_pacientes(self):
        atual = self.primeiro
        print('Lista de pacientes:')
        while atual:
            print('Nome:', atual.nome_paciente)
            print('Id:', atual.id_paciente)
            print('Estado de saúde:', atual.estado_saude)
            print('---------------------------------')
            atual = atual.proximo
            
            

lista_pacientes = ListaDePaciente()

lista_pacientes.adicionar_paciente('Joao', 101,'estavel')
lista_pacientes.adicionar_paciente('Maria', 123, 'tratamento')

lista_pacientes.listar_pacientes()