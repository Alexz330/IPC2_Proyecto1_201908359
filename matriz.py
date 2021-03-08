from NodoMatriz import *
from NodoGeneral import *
import os  

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
    

    def ObtenerPorCoordenada(self,x,y):
        temporal = self.first
        while temporal is not None:
            if(x==int(temporal.x) and int(temporal.y)==y):
                break
            temporal = temporal.next
        if(temporal is not None):
            return int(temporal.dato)
        else: 
            return None
    
    def ObtenerM(self):
        temporal = self.first
        final = None
        while temporal is not None:
            final = temporal
            temporal = temporal.next
        return final.y
    
    def ObtenerN(self):
        temporal = self.first
        final = None
        while temporal is not None:
            final = temporal
            temporal = temporal.next
        return final.x

    def ListarDatosXML(self):
        temporal = self.first
        txt = ""
        while temporal is not None:
            txt = txt + '       <dato x="'+str(temporal.x)+'" y="'+str(temporal.y)+'">'+str(temporal.dato)+'</dato>\n'
            temporal = temporal.next
        return txt
        
    
    