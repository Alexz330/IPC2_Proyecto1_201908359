  
from xml.dom import minidom
import xml.etree.ElementTree as ET
from matriz import *
from ListaGeneral import *

def lectura():

    ruta = input("Escriba la ruta del archivo: ")
    tree = ET.parse(ruta)
    
    root = tree.getroot()
    
    listaCircular = ListaGeneral()
    listaBinaria = ListaGeneral()
    

    #for valores in root:
        #listaDatos= Matriz()
        #for datos in valores:
            #listaDatos.AppendS(datos.attrib['x'], datos.attrib['y'], datos.text)
        #listaCircular.Append(valores.attrib['nombre'], valores.attrib['n'], valores.attrib['m'], listaDatos)
    #listaCircular.Listar()


    #matriz binaria 

    
    print('***********Matriz binaria************')
    
    lista=[1,2,3,4,5,6,7,8,9]
    for M_binaria in root:
        listaDato= Matriz()
        
        for datos in M_binaria:
            if int(datos.text) in lista:
                
                listaDato.AppendS(datos.attrib['x'], datos.attrib['y'], 1)
            else:
                listaDato.AppendS(datos.attrib['x'], datos.attrib['y'], 0)
        listaBinaria.Append(M_binaria.attrib['nombre'], M_binaria.attrib['n'], M_binaria.attrib['m'], listaDato)
    listaBinaria.Listar()


    print("*****Reduccion de matrices*****")


    for M_reducida in root:
        reducida = Matriz()
        for datos in M_reducida:
            if int(datos.text) in lista:
                listaDato.AppendS(datos.attrib['x'], datos.attrib['y'], 1)
            else:
                listaDato.AppendS(datos.attrib['x'], datos.attrib['y'], 0)
        listaBinaria.Append(M_reducida.attrib['nombre'], M_reducida.attrib['n'], M_reducida.attrib['m'], listaDato)
    listaBinaria.Listar()



    
    
        


