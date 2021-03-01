from NodoMatriz import *

class Matriz:

    def __init__(self):
        self.first = None
    
    def AppendS(self, x, y, dato):
        nuevo = NodoMatriz(x, y, dato)

        if self.first is None:
            self.first = nuevo
        else:
            temporal = self.first
            while temporal.next is not None:
                temporal = temporal.next
            temporal.next = nuevo

    def ListarS(self):
        temporal = self.first
        while temporal is not None:
            print(f'posicion x:{str(temporal.x)} posicion y:{str(temporal.y)} valor: {str(temporal.dato)}')
            temporal = temporal.next
        
    
    