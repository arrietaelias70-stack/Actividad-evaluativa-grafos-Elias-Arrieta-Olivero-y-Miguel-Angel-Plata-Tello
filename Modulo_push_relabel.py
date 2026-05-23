# Modulo: push_relabel.py
import time, numpy as np
from grafo_general import Grafo, construir_escenario_A, construir_escenario_B


class PushRelabel:
    def __init__(self, grafo: Grafo, fuente: int, sumidero: int):
        self.grafo=grafo
        self.fuente=fuente
        self.sumidero=sumidero
        self.tamaño= len(grafo.nodos)
        self.capacidad_disponible =np.zeros((self.tamaño, self.tamaño), dtype=int)
        self.altura= [0] * self.tamaño
        self.exceso= [0] * self.tamaño

        # Métricas de rendimiento
        self.operaciones_push= 0
        self.operaciones_relabel= 0
        self.tiempo_ejecucion= 0.0
        self.iteraciones_totales= 0      
        self.saturacion_red= 0.0     

        self._construir_matriz_capacidad_disponible()

    # Construcción de la matriz de capacidades disponibles a partir del grafo
    def _construir_matriz_capacidad_disponible(self):
        for arista in self.grafo.aristas:
            u= arista.origen
            v= arista.destino
            self.capacidad_disponible[u][v]+= arista.capacidad

    def _push(self, u: int, v: int):
        flujo_enviado= min(self.exceso[u], self.capacidad_disponible[u][v])
        self.capacidad_disponible[u][v]-= flujo_enviado
        self.capacidad_disponible[v][u]+= flujo_enviado
        self.exceso[u]-= flujo_enviado
        self.exceso[v]+= flujo_enviado
        self.operaciones_push+= 1

    def _relabel(self, u: int):
        min_altura_vecino= float('inf')
        for v in range(self.tamaño):
            if self.capacidad_disponible[u][v] > 0:
                min_altura_vecino= min(min_altura_vecino, self.altura[v])
        self.altura[u]= 1 + min_altura_vecino
        self.operaciones_relabel+= 1

    def _inicializar_preflujo(self):
        self.altura[self.fuente]= self.tamaño
        for v in range(self.tamaño):
            if self.capacidad_disponible[self.fuente][v] > 0:
                self.exceso[v]+= self.capacidad_disponible[self.fuente][v]
                self.capacidad_disponible[v][self.fuente]+=self.capacidad_disponible[self.fuente][v]
                self.exceso[self.fuente]-=self.capacidad_disponible[self.fuente][v]
                self.capacidad_disponible[self.fuente][v]= 0

    def calcular_flujo_maximo(self):
        inicio = time.perf_counter()
        self._inicializar_preflujo()

        # Lista de nodos activos
        activos = [u for u in range(self.tamaño) if u != self.fuente and u != self.sumidero and self.exceso[u] > 0]
        while activos:
            u = activos[0]
            empujado = False
            self.iteraciones_totales += 1

            for v in range(self.tamaño):
                if (self.capacidad_disponible[u][v] > 0 and self.altura[u] == self.altura[v] + 1):
                    self._push(u,v)
                    empujado = True
                    # Tambien agregamos al nodo v a activos si cumple las condiciones
                    if (v!=self.fuente and v!= self.sumidero and self.exceso[v] > 0 and v not in activos):
                        activos.append(v)
                    break

            if not empujado:
                self._relabel(u)
            # Esta partecita es para retirar al nodo u si ya no tiene exceso
            if self.exceso[u] == 0:
                activos.pop(0)

        self.tiempo_ejecucion = time.perf_counter() - inicio

        capacidad_fuente = 0
        for a in self.grafo.aristas:
            if a.origen==self.fuente:
                capacidad_fuente += a.capacidad
        if capacidad_fuente > 0:
            self.saturacion_red = (self.exceso[self.sumidero] / capacidad_fuente)*100
        return self.exceso[self.sumidero]

    
    def mostrar_resultados(self, flujo_maximo: int):
        nombre_fuente=self.grafo.nodos[self.fuente].nombre
        nombre_sumidero=self.grafo.nodos[self.sumidero].nombre

        print("  Algoritmo push-relabel para el flujo máximo")
    
        print(f"grafo: {self.grafo.nombre}")
        print(f"fuente: nodo {self.fuente} ({nombre_fuente})")
        print(f"sumidero: nodo {self.sumidero} ({nombre_sumidero})")
        print(f"flujo maximo encontrado: {flujo_maximo} gbps")
        print(f"operaciones Push: {self.operaciones_push}")
        print(f"operaciones Relabel: {self.operaciones_relabel}")
        print(f"iteraciones totales: {self.iteraciones_totales}")
        print(f"saturación de la red: {self.saturacion_red:.1f}%")
        print(f"tiempo de ejecución: {self.tiempo_ejecucion * 1000:.4f} ms")


def ejecutar_push_relabel(grafo: Grafo, fuente: int, sumidero: int):
    algoritmo=PushRelabel(grafo, fuente, sumidero)
    flujo_max=algoritmo.calcular_flujo_maximo()
    algoritmo.mostrar_resultados(flujo_max)
    return flujo_max, algoritmo

if __name__ == "__main__":
    print("\n-Prueba con push relabel\n")

    grafo_A = construir_escenario_A()
    ejecutar_push_relabel(grafo_A, fuente=0,sumidero=9)

    print()
    grafo_B = construir_escenario_B()
    ejecutar_push_relabel(grafo_B, fuente=0,sumidero=5)
