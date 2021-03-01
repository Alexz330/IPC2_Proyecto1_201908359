  
from xml.dom import minidom
import xml.etree.ElementTree as ET
from Matriz import *
from ListaGeneral import *

def lectura():

    ruta = input("Escriba la ruta del archivo: ")
    tree = ET.parse(ruta)
    
    root = tree.getroot()
    
    listaCircular = ListaGeneral()
    

    for valores in root:
        listaDatos= Matriz()
        for datos in valores:
            listaDatos.AppendS(datos.attrib['x'], datos.attrib['y'], datos.text)
        listaCircular.Append(valores.attrib['nombre'], valores.attrib['n'], valores.attrib['m'], listaDatos)
    listaCircular.Listar()


    
    
        


