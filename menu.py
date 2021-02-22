from lectura import lectura

def PantallaInicial():
    print("IPC2, Seccion #, 201908389")
    input("Presiona cualquier boton para continuar: ")
    MenuPrincipal()

def MenuPrincipal():
    print("--------------Bienvenido al menu, ingresa la opcion que desees--------------")
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
        lectura()
    elif opselect == "2":
        Opcion2()
    elif opselect == "3":
        Opcion3()
    elif opselect == "4":
        Opcion4()
    else:
        print("Opcion inexistente")
        MenuPrincipal()
PantallaInicial()