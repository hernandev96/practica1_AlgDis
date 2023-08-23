# Clase de nodo padre para atender las peticiones de sus hijos
import random


class padre:
    def __init__(self):
        self.recursos = random.randint(1, 5)
        self.disponibles = True
        self.msg = 0
        self.atendidos = 0

    def solicitar(self):
        print("Soy el nodo central y recibi un solicitud TRIS de recursos")
        self.msg = self.msg+1
        print("Enviando TRAS--------------")

    def solicitar2(self):
        print("Soy el nodo central y recibi un solicitud TRIS de recursos")
        if self.recursos > 0:
            self.msg = self.msg+1
            self.atendidos = self.atendidos+1
            self.recursos = self.recursos-1
            print("Enviando TRAS--------------")
        else:
            print("No hay recursos suficientes")
            print("Enviando TRUS--------------")
