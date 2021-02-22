from xml.dom import minidom


def lectura():
    ruta = input("Escriba la ruta del archivo: ")
    doc =  minidom.parse(ruta)
    