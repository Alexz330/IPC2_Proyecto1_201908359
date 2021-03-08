
from xml.dom import minidom
import xml.etree.ElementTree as ET
from matriz import *
from ListaGeneral import *
from ReducirMatriz import *


def Menusito(ruta):
    print("######MENU BIEN PERRON###########")
    print("1. Cargar archivo")
    print("2. Procesar archivo")
    print("3. Escribir archivo salida")
    print("4. Mostrar datos del estudiate")
    print("5. Generar gráfica")
    print("6. Salida")
    opselect = input()
    if opselect == "1":
        print("Guardando datos...")
        print("")
        Lectura()
    elif opselect == "2":
        procesar_archivo(ruta)
    elif opselect == "3":
        archivo(ruta)
    elif opselect == "4":
        Opcion4()
    elif opselect == "5":
        graficar(ruta)
    else:
        print("Opcion inexistente")
        Menusito(ruta)



listaCircular = ListaGeneral()
listaBinaria = ListaGeneral()



def Lectura():
    
    ruta = input("Escriba la ruta del archivo: ")
    
    tree = ET.parse(ruta)
    
    
    root = tree.getroot()

    for valores in root:
        listaDatos= Matriz()
        for datos in valores:
            listaDatos.AppendS(datos.attrib['x'], datos.attrib['y'], datos.text)
        listaCircular.Append(valores.attrib['nombre'], valores.attrib['n'], valores.attrib['m'], listaDatos)
    listaCircular.Listar()

    


    print('****Matriz binaria*****')
    
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



    
    Menusito(ruta)
    
    

def procesar_archivo(ruta):
   
    tree = ET.parse(ruta)
    root = tree.getroot()
    
    for valores in root:
        listaDatos= Matriz()
        for datos in valores:

            listaDatos.AppendS(datos.attrib['x'], datos.attrib['y'], datos.text)
        print(valores.attrib['nombre'])
        matriz_reducida = devolverMatrizReducidaFinal(listaDatos,valores.attrib['n'], valores.attrib['m'] ) 
        matriz_reducida.ListarS()
        listaCircular.Append(valores.attrib['nombre'], valores.attrib['n'], valores.attrib['m'], listaDatos)
            

def archivo(ruta):
   
    tree = ET.parse(ruta)
    root = tree.getroot()
    txt = "<matrices>\n"

    for valores in root:
        listaDatos= Matriz()
        for datos in valores:
            listaDatos.AppendS(datos.attrib['x'], datos.attrib['y'], datos.text)
        listaCircular.Append(valores.attrib['nombre'], valores.attrib['n'], valores.attrib['m'], listaDatos)
        matriz_reducida = devolverMatrizReducidaFinal(listaDatos,listaCircular.first.n,listaCircular.first.m)
        txt = txt + '   <matriz nombre="'+valores.attrib['nombre']+"_Reducida"'" n="'+str(matriz_reducida.ObtenerN())+'" m="'+str(matriz_reducida.ObtenerM())+'">\n'
        txt = txt + matriz_reducida.ListarDatosXML()
        txt = txt + "   </matriz>\n"
    txt = txt + "</matrices>\n"
    with open("reporte.xml", mode='w') as f:
        f.write(txt) 

    Menusito(None)


def graficar(ruta):

    
    tree = ET.parse(ruta)
    root = tree.getroot()
   

    numero_grafo = 1
    for grafos in root: 
        
        print(str(numero_grafo)+". "+grafos.attrib['nombre'])
        numero_grafo+=1  

    g_elejido= input("selecciona la matriz a graficar: ")

    for grafos in root:    
        if g_elejido == grafos.attrib['nombre']:
            with open("Grafica.dot", mode='w') as f:
                f.write("digraph Figura {\n")
                f.write("rankdir=UD\n")
                f.write("Matriz[shape=circle color=red label=\"Matrices\"]\n")
                f.write("Matriz -> Nombre\n")
                f.write("Nombre -> "+grafos.attrib['nombre']+"[shape=circle color=red label=\"\"]\n")
                f.write("Fila[shape = doublecircle color=red label=\"n = "+grafos.attrib['n']+"\"]\n")
                f.write("Columna[shape = doublecircle color=red label=\"m = "+grafos.attrib['m']+"\"]\n")
                f.write(grafos.attrib['nombre']+"-> Fila\n")
                f.write(grafos.attrib['nombre']+"-> Columna\n") 
                for valores in grafos:
                    
                    f.write(grafos.attrib['nombre']+"->"+valores.text+"\n")
                   

                f.write("}\n")

    Menusito(None)    


Menusito(None)