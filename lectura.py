from xml.dom import minidom
import xml.etree.ElementTree as ET
from lista import *


def lectura():

    ruta = input("Escriba la ruta del archivo: ")
    tree = ET.parse(ruta)
    
    root = tree.getroot()
    
    matriz = listaCircular()

    for elemento in root:
        if elemento.attrib['nombre']== 'matriz_n_1':
            for subelemento in elemento:
                matriz.insertar(subelemento.text, "")
        else: 
            return False


    listaMatriz = listaCircular()
    #Clases = etree.xpath('//clase')
    for clase in root:
        listaMatriz.insertar(matriz.attrib['nombre'], matriz.attrib['n'], matriz.atrib['m'])
    print("@@@@@@@@@@@@@@@@@@@@@")
    listaMatriz.imprimir()