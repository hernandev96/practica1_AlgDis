# Programa que simula el envio de peticiones en una estructura de estrella

import sys
from nodo_hijo import Nodo_hijo
from nodo_padre import padre
import random


def solicitud():
    sol = random.randint(0, 1)
    if sol == 1:
        return True
    return False


def crear_nodos(filename):
    aux = list()
    archivo = open(filename, "r")
    for line in archivo:
        arrAux = line.split(" ")
        newNodo = Nodo_hijo(arrAux[1], arrAux[0], solicitud())
        aux.append(newNodo)
    return aux


def main():
    nodo_central = padre()
    print("Recursos disponibles: ", nodo_central.recursos)
    if len(sys.argv) != 2:
        print("No recibi ningun archivo!!!")

    else:
        print("recibi el archivo\nvamos a crear los nodos de la periferia ")
        nodos = crear_nodos(sys.argv[1])
        for nodo in nodos:
            if nodo.solicitud:
                print("Soy el nodo ", nodo.nodo_num,
                      " Y voy a enviarr una solicitud TRIS al nodo 1")
                nodo_central.solicitar2()
            else:
                print("Soy el nodo ", nodo.nodo_num,
                      "No voy a solicitar recursos")

        print("Soy el nodo central y atendi en total: \n",
              nodo_central.msg, " mensajes")
        print("Solicitudes atendidas favorablemente: ",
              nodo_central.atendidos, "\n")
        print("Total de recursos restantes: ", nodo_central.recursos)


main()
