from NodoGeneral import *
from Matriz import *

class ListaGeneral:

    def __init__(self):
        self.first= None
        self.last = None
    
    def Append(self, nombre, n, m, matriz):
        nuevo = NodoGeneral(nombre, n, m, matriz)

        if self.first is None:
            self.first = self.last = nuevo
            self.last.next = self.first
        else:
            temporal = self.last
            self.last = temporal.next = nuevo
            self.last.next = self.first
  
    def Listar(self):
        temporal = self.first
        while temporal is not None:
            print(f'nombre: {str(temporal.nombre)} n: {str(temporal.n)}  m:{str(temporal.m)}  ' )
            if temporal.matriz is not None:
                print(f'{temporal.matriz.ListarS()}')
            temporal = temporal.next
            if temporal == self.first:
                break 
        