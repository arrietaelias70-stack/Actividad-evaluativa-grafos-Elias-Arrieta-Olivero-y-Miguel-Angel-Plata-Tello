import time
from grafo_general import Grafo, construir_escenario_A, construir_escenario_B


class WelshPowell:
    def __init__(self, grafo: Grafo):
        self.grafo=grafo
        self.colores={}   
        self.num_colores=0
        self.tiempo_ejecucion=0.0
        self.orden_procesado=[]
        self.densidad_grafo=0.0
        self.nodos_por_color={}

    def calcular_grados(self):
        grados={}
        for nodo_id in self.grafo.nodos:
            grados[nodo_id] = 0
        for arista in self.grafo.aristas:
            grados[arista.origen] += 1
            grados[arista.destino] += 1
        return grados

    def obtener_vecinos(self, nodo_id):
        vecinos=[]
        for arista in self.grafo.aristas:
            if arista.origen==nodo_id:
                vecinos.append(arista.destino)
            if arista.destino==nodo_id:
                vecinos.append(arista.origen)
        return vecinos


    # de mayor a menor grado 
    def ordenar_nodos_por_grado(self, grados):
        nodos = list(self.grafo.nodos.keys())

        for i in range(len(nodos)):
            for j in range(i+1,len(nodos)):
                if grados[nodos[i]]< grados[nodos[j]]:
                    nodos[i],nodos[j]=nodos[j], nodos[i]
        return nodos


    # creamos esta función para verificar si un nodo vecino ya tiene el color que queremos asignar
    def hay_inconveniente(self,nodo_id,color):
        vecinos=self.obtener_vecinos(nodo_id)
        for vecino in vecinos:
            if vecino in self.colores:
                if self.colores[vecino]==color:
                    return True
        return False


    # Ejecutar el algoritmo de coloración Welsh-Powell
    def colorear(self):
        inicio = time.perf_counter()

        #Calcular grados y ordenar nodos
        grados= self.calcular_grados()
        nodos_ordenados= self.ordenar_nodos_por_grado(grados)
        self.orden_procesado= nodos_ordenados

        #asignar colores
        color_actual= 0
        for nodo_id in nodos_ordenados:
            if nodo_id in self.colores:
                continue                    

            # Asignar el color actual a este nodo
            self.colores[nodo_id]=color_actual

            # Intentar asignar el mismo color a otros nodos sin inconvenientes
            for otro_nodo in nodos_ordenados:
                if otro_nodo in self.colores:
                    continue                

                if not self.hay_inconveniente(otro_nodo, color_actual):
                    self.colores[otro_nodo]=color_actual
            color_actual+= 1

        self.num_colores=color_actual
        self.tiempo_ejecucion=time.perf_counter() - inicio


        n= len(self.grafo.nodos)
        max_aristas=n*(n-1)
        self.densidad_grafo=len(self.grafo.aristas)/max_aristas

        #cuántos nodos tiene cada color
        for nodo_id in self.colores:
            color=self.colores[nodo_id]
            if color not in self.nodos_por_color:
                self.nodos_por_color[color]=0
            self.nodos_por_color[color]+= 1

    def mostrar_resultados(self):
        grados= self.calcular_grados()
        # Agrupar nodos por color
        grupos= {}
        for nodo_id in self.colores:
            color=self.colores[nodo_id]
            if color not in grupos:
                grupos[color]= []
            grupos[color].append(nodo_id)

        nombres_colores= ["Rojo","Azul","Verde","Amarillo","Magenta","Cian","Naranja","Violeta","Rosa","Gris" ]

        print("Resultados Welsh-Powell")
        print("grafo:", self.grafo.nombre)
        print("colores usados:", self.num_colores)
        print("densidad del grafo:", self.densidad_grafo)
        print("nodos por color:", self.nodos_por_color)
        print("tiempo:", self.tiempo_ejecucion * 1000, "ms")

        print("\nOrden de nodos de mayor a menor grado:")
        for nodo_id in self.orden_procesado:
         nombre=self.grafo.nodos[nodo_id].nombre
         print(" nodo", nodo_id, "--", nombre, "-- grado:", grados[nodo_id])

        print("\ncolores asignados:")
        for color in grupos:
         if color<len(nombres_colores):
            etiqueta=nombres_colores[color]
         else:
            etiqueta= nombres_colores[0]
         print("\n", etiqueta)
         for nodo_id in grupos[color]:
            nombre= self.grafo.nodos[nodo_id].nombre
            print("nodo", nodo_id, "-", nombre)


def ejecutar_welsh_powell(grafo: Grafo):
    algoritmo=WelshPowell(grafo)
    algoritmo.colorear()
    algoritmo.mostrar_resultados()
    return algoritmo.num_colores, algoritmo


if __name__== "__main__":

    print("\nPrueba Welsh-Powell")

    grafo_A= construir_escenario_A()
    ejecutar_welsh_powell(grafo_A)

    grafo_B= construir_escenario_B()
    ejecutar_welsh_powell(grafo_B)
