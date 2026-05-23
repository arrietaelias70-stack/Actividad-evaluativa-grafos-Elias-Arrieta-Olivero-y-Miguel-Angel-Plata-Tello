class Nodo:
    def __init__(self, identificador,nombre):
        self.identificador = identificador
        self.nombre=nombre
    def __str__(self):
        return f"nodo {self.identificador}: {self.nombre}"

class Arista:

    def __init__(self, origen, destino, capacidad):
        self.origen= origen
        self.destino=destino
        self.capacidad=capacidad

    def __str__(self):
        return (f"  Nodo {self.origen}, Nodo {self.destino}" f" Capacidad: {self.capacidad} Gbps")



class Grafo:

    def __init__(self, nombre):
        self.nombre= nombre
        self.nodos= {}
        self.aristas= []
        self.adyacencia= {}

    #Agregar un nodo al grafo
    def agregar_nodo(self, identificador, descripcion):
        nodo= Nodo(identificador, descripcion)
        self.nodos[identificador]= nodo
        self.adyacencia[identificador]= []

    # Agregar una arista dirigida al grafo 
    def agregar_arista(self, origen, destino, capacidad):
        arista= Arista(origen, destino, capacidad)
        self.aristas.append(arista)
        self.adyacencia[origen].append(arista)

    #vecinos de un nodo 
    def vecinos(self, id_nodo):
        return self.adyacencia[id_nodo]

    # Obtener la capacidad de una arista específica
    def capacidad_arista(self, origen, destino):
        for arista in self.adyacencia[origen]:
            if arista.destino==destino:
                return arista.capacidad
        return 0
    
    #Info del grafo
    def info_del_grafo(self):
     texto= f"Grafo: {self.nombre}\n"
     texto+= f"Nodos: {len(self.nodos)}\n"
     texto+= f"Aristas: {len(self.aristas)}\n"
     texto+= "\nNodos:\n"
     for nodo in self.nodos.values():
        entran= 0
        for a in self.aristas:
            if a.destino== nodo.identificador:
                entran+= 1
        salen = len(self.adyacencia[nodo.identificador])
        texto += f"{nodo} (entran: {entran}, salen: {salen})\n"
     texto += "\nAristas:\n"
     for arista in self.aristas:
        texto += str(arista) + "\n"
    
     return texto


def construir_escenario_A():

    grafo = Grafo("Escenario A red de 10 nodos")
    grafo.agregar_nodo(0, "Servidor central Bogotá")
    grafo.agregar_nodo(1, "Centro de Datos sucursal Bucaramanga")
    grafo.agregar_nodo(2, "Centro de Datos sucursal Cali")
    grafo.agregar_nodo(3, "Router Principal")
    grafo.agregar_nodo(4, "Switch 1")
    grafo.agregar_nodo(5, "Centro de Datos sucursal Medellín")
    grafo.agregar_nodo(6, "Router Secundario")
    grafo.agregar_nodo(7, "Centro de Datos sucursal Barranquilla")
    grafo.agregar_nodo(8, "Switch 2")
    grafo.agregar_nodo(9, "Terminal New York")

    #En esta parte agregamos las aristas con parametros (origen, destino, capacidad)
    grafo.agregar_arista(0, 1, 15)
    grafo.agregar_arista(0, 2, 10)
    grafo.agregar_arista(0, 3, 12)
    grafo.agregar_arista(1, 3,  8)
    grafo.agregar_arista(1, 4, 10)
    grafo.agregar_arista(2, 4,  7)
    grafo.agregar_arista(2, 5,  9)
    grafo.agregar_arista(3, 4,  6)
    grafo.agregar_arista(3, 6,  5)
    grafo.agregar_arista(4, 5,  4)
    grafo.agregar_arista(4, 6,  8)
    grafo.agregar_arista(4, 7,  7)
    grafo.agregar_arista(5, 7,  6)
    grafo.agregar_arista(5, 8,  5)
    grafo.agregar_arista(6, 7,  9)
    grafo.agregar_arista(6, 9,  4)
    grafo.agregar_arista(7, 8,  8)
    grafo.agregar_arista(7, 9,  6)
    grafo.agregar_arista(8, 9, 10)
    return grafo




def construir_escenario_B():
    grafo = Grafo("Escenario B red de 6 nodos")

    # Agregar los 6 nodos
    grafo.agregar_nodo(0, "Servidor central")
    grafo.agregar_nodo(1, "Nodo centro de datos norte")
    grafo.agregar_nodo(2, "Nodo centro de datos sur")
    grafo.agregar_nodo(3, "Nodo centro de datos noroeste")
    grafo.agregar_nodo(4, "Nodo centro de datos suroeste")
    grafo.agregar_nodo(5, "Terminal Salida")

    grafo.agregar_arista(0, 1, 12)
    grafo.agregar_arista(0, 2, 10)
    grafo.agregar_arista(0, 3,  8)
    grafo.agregar_arista(0, 4, 15)
    grafo.agregar_arista(0, 5,  6)
    grafo.agregar_arista(1, 0,  9)
    grafo.agregar_arista(1, 2, 14)
    grafo.agregar_arista(1, 3, 11)
    grafo.agregar_arista(1, 4,  7)
    grafo.agregar_arista(1, 5, 13)
    grafo.agregar_arista(2, 0,  5)
    grafo.agregar_arista(2, 1,  8)
    grafo.agregar_arista(2, 3, 10)
    grafo.agregar_arista(2, 4, 12)
    grafo.agregar_arista(2, 5,  9)
    grafo.agregar_arista(3, 0, 11)
    grafo.agregar_arista(3, 1,  6)
    grafo.agregar_arista(3, 2,  7)
    grafo.agregar_arista(3, 4, 14)
    grafo.agregar_arista(3, 5, 10)
    grafo.agregar_arista(4, 0,  8)
    grafo.agregar_arista(4, 1, 13)
    grafo.agregar_arista(4, 2,  9)
    grafo.agregar_arista(4, 3,  5)
    grafo.agregar_arista(4, 5, 16)
    grafo.agregar_arista(5, 0,  4)
    grafo.agregar_arista(5, 1,  7)
    grafo.agregar_arista(5, 2, 11)
    grafo.agregar_arista(5, 3,  8)
    grafo.agregar_arista(5, 4, 10)

    return grafo



if __name__ == "__main__":
    print("Grafo de la red interconexión S.A.")

    grafo_A = construir_escenario_A()
    grafo_A.info_del_grafo()
    grafo_B = construir_escenario_B()
    grafo_B.info_del_grafo()

