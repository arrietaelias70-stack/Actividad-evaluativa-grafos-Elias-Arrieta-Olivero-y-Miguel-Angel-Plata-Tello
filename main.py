from grafo_general import construir_escenario_A, construir_escenario_B
from Modulo_push_relabel import ejecutar_push_relabel
from Modulo_Welsh_powell import ejecutar_welsh_powell


print("red interconexion S.A. analisis mediante Push-Relabel y Welsh-Powell")

# escenario A
print("\n Escenario A con 10 nodos")
grafo_A= construir_escenario_A()

print("\nPush-Relabel:")
flujo_A, push_relabel_A = ejecutar_push_relabel(grafo_A, fuente=0, sumidero=9)

print("\nWelsh-Powell:")
colores_A, welsh_powell_A = ejecutar_welsh_powell(grafo_A)

# escenario B
print("\nEscenario B con 6 nodos")
grafo_B= construir_escenario_B()

print("\nPush-Relabel:")
flujo_B, push_relabel_B= ejecutar_push_relabel(grafo_B, fuente=0, sumidero=5)

print("\nWelsh-Powell:")
colores_B, welsh_powell_B= ejecutar_welsh_powell(grafo_B)
print("\nComparacion de resultados")

print("\nPush-Relabel:")
print("En el escenario A el flujo maximo fue", flujo_A, "gbps y en el escenario B fue", flujo_B, "gbps")
print("El escenario A necesito", push_relabel_A.operaciones_push, "operaciones push y el B", push_relabel_B.operaciones_push)
print("En relabel, el escenario A tuvo", push_relabel_A.operaciones_relabel, "operaciones y el B tuvo", push_relabel_B.operaciones_relabel)
print("Las iteraciones totales del escenario A fueron", push_relabel_A.iteraciones_totales, "y del B fueron", push_relabel_B.iteraciones_totales)
print("La saturacion de la red fue de", round(push_relabel_A.saturacion_red, 1), "% en A y", round(push_relabel_B.saturacion_red, 1), "% en B")
print("En cuanto al tiempo el escenario A demoró", round(push_relabel_A.tiempo_ejecucion * 1000, 4), "ms y el B demoró", round(push_relabel_B.tiempo_ejecucion * 1000, 4), "ms")

print("\nWelsh-Powell:")
print("El escenario A necesito", colores_A, "colores y el B necesito", colores_B)
print("La densidad del grafo A es", round(welsh_powell_A.densidad_grafo, 2), "y la del B es", round(welsh_powell_B.densidad_grafo, 2))
print("La distribucion de nodos por color en A fue", welsh_powell_A.nodos_por_color, "y en B fue", welsh_powell_B.nodos_por_color)
print("El tiempo del escenario A fue", round(welsh_powell_A.tiempo_ejecucion * 1000, 4), "ms y el B fue", round(welsh_powell_B.tiempo_ejecucion * 1000, 4), "ms")
