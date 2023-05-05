

class Tarefas():
    def __init__(self):
        self.lista_tarefas = []
    
    def adicionar(self, add):
       
            print("tarefa adicionada com sucesso!")
            return self.lista_tarefas.append(add)
        
    def listar(self):
        print(self.lista_tarefas)
    
    def remover(self,remover):
        print("tarefa removida com sucesso!")
        self.lista_tarefas.pop(remover)
        return self.listar()
    
    def modificar_acao(self,index, elemento):
        self.listar()
        self.lista_tarefas.insert([index][1], elemento)
        return print("Ação modificada com sucesso!")
    
    def verificarChoqueHorario(self):

        self.lista_tarefas.sort()
        for i in range(len(self.lista_tarefas)):
            if self.lista_tarefas[-1+i][0] == self.lista_tarefas[i][0]:
                print("choque de hórario!")
                return False 
            else:
                return True
        


    def modificar_horario(self,index, horario):
       
        if self.verificarChoqueHorario == True:
            self.listar()
            self.lista_tarefas[index][0] = horario
            return print("Horário modificado com sucesso!")
        else:
            return print("Choque de horário!")

