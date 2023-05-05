from librays.tarefas import Tarefas

agenda = Tarefas()


def Workspace():
  print("Adicionando Tarefas!")
  agenda.adicionar(['8:00AM', 'Tomar Café!'])
  agenda.adicionar(['6:00AM', 'Orar!'])
  agenda.adicionar(['5:00AM', 'Acordar!'])
  agenda.adicionar(['12:00AM', 'Estudar!'])
  print('')

  print("listar todas as tarefas adicionadas!")
  agenda.listar()
  print("")
  print("Podemos remover umas das tarefas")
  agenda.remover(0)
  print('')
  

  print("Caso tenha choque de horário, o programa o alerta")
  agenda.modificar_horario(0,"6:00AM")
  
  

if __name__ == "__main__":
    Workspace()