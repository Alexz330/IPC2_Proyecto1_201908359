  
from xml.dom import minidom
import xml.etree.ElementTree as ET
from Matriz import *
from ListaGeneral import *


def lectura():

    ruta = input("Escriba la ruta del archivo: ")
    tree = ET.parse(ruta)
    
    root = tree.getroot()
    
    matriz = ListaGeneral()
    datos = Matriz()

    for elementos in root:
        matriz.Append()
        


