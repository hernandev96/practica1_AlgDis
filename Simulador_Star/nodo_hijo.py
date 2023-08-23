class Nodo_hijo:

    def __init__(self, padre, nodo_num, solicitud):
        self.padre = padre
        self.nodo_num = nodo_num
        self.solicitud = solicitud

    def get_padre(self):
        return self.padre

    def getnum_nodo(self):
        return self.nodo_num

    def getSolicitud(self):
        return self.solicitud
