
from matriz import *

def devolverMatrizReducida(matrizNormal, matrizBinaria, m, n):
    cont = 0
    existeIgual = False
    y1igual = 0
    y2igual = 0
    
    for y1 in range(int(n)):
        for y2 in range(int(n)):
            if(y1 < y2):
                cont = 0
                for x in range(int(m)):
                    #print("x:"+str(x+1) +" y1:"+ str(y1+1) +" y2:"+ str(y2+1) )
                    #print(str(matrizBinaria.ObtenerPorCoordenada(x+1,y1+1))+" "+str(matrizBinaria.ObtenerPorCoordenada(x+1,y2+1)))
                    if(matrizBinaria.ObtenerPorCoordenada(x+1,y1+1) == matrizBinaria.ObtenerPorCoordenada(x+1,y2+1)):
                        cont = cont +1
                if(cont == int(m)):
                    y1igual = y1+1
                    y2igual = y2+1
                    existeIgual = True
                    break
        if(existeIgual):
            break
    #print("y1igual: " + str(y1igual))
    #print("y2igual: " + str(y2igual))
    if(y1igual == 0 and y2igual == 0):
        return None
    else:
        return unirFilas(matrizNormal,y1igual,y2igual,m,n)

def pasarAMatrizBinaria(matrizNormal):
    temporal = matrizNormal.first
    nuevaMatriz = Matriz()
    while temporal is not None:
        if(temporal.dato == '0'):
            nuevaMatriz.AppendS(temporal.x,temporal.y,0)
        else:
            nuevaMatriz.AppendS(temporal.x,temporal.y,1)
        temporal = temporal.next
    return nuevaMatriz

def devolverMatrizReducidaFinal(matrizNormal, m, n):
    matrizTemporal = matrizNormal
    cont = 0
    while matrizTemporal is not None:
        matrizNormal = matrizTemporal
        nuevaBinaria = pasarAMatrizBinaria(matrizNormal)
        matrizTemporal = devolverMatrizReducida(matrizNormal,nuevaBinaria, m, str(int(n) - cont))
        cont = cont + 1
    return matrizNormal

def unirFilas(matrizNormal, y1, y2, m, n):
    alcanzoY2 = False
    nuevaMatrizSumada = Matriz()
    for yy in range(int(n)):
        for xx in range(int(m)):
            #print("yy+1: " + str(yy+1))
            #print("y1: " + str(y1))
            #print(yy+1 != y1)
            if(yy+1==y1):
                nuevaMatrizSumada.AppendS(xx+1,yy+1,str(matrizNormal.ObtenerPorCoordenada(xx+1,y1)+matrizNormal.ObtenerPorCoordenada(xx+1,y2)))
            elif(yy+1==y2):
                alcanzoY2 = True
            else:
                if(alcanzoY2):
                    nuevaMatrizSumada.AppendS(xx+1,yy,str(matrizNormal.ObtenerPorCoordenada(xx+1,yy+1)))
                else:
                    nuevaMatrizSumada.AppendS(xx+1,yy+1,str(matrizNormal.ObtenerPorCoordenada(xx+1,yy+1)))
    return nuevaMatrizSumada


