import time
import random
from metodo_ordenamiento import MetodoOrdenamiento

class Benchmarking:
    
    def __init__(self):
        print("Benchmarking instanciado")
        self.mO = MetodoOrdenamiento()  # instanciamos una sola vez

    def medir_tiempo(self, funcion, arreglo):
        inicio = time.perf_counter()
        funcion(arreglo)
        fin = time.perf_counter()
        return fin - inicio

    def build_arreglo(self, tamanio):
        arreglo = [random.randint( ) for i in range(tamanio)]
        return arreglo

    def contar_con_milisegundos(self, tarea):
        inicio = time.time()
        tarea()
        fin = time.time()
        return fin - inicio

    def contar_con_nanosegundos(self, tarea):
        inicio = time.time_ns()
        tarea()
        fin = time.time_ns()
        return (fin - inicio) / 1_000_000_000.0

    def correr_benchmark(self):
        arreglo = self.build_arreglo(10000)

        # copias para que no se altere el arreglo original entre métodos
        arreglo_bubble = arreglo.copy()
        arreglo_optimizado = arreglo.copy()
        arreglo_seleccion = arreglo.copy()

        tarea_bubble = lambda: self.mO.sort_bubble(arreglo_bubble)
        tarea_optimizado = lambda: self.mO.sort_burbuja_mejorado_optimizado(arreglo_optimizado)
        tarea_seleccion = lambda: self.mO.sort_seleccion(arreglo_seleccion)

        tiempo_bubble_ms = self.contar_con_milisegundos(tarea_bubble)
        tiempo_optimizado_ms = self.contar_con_milisegundos(tarea_optimizado)
        tiempo_seleccion_ms = self.contar_con_milisegundos(tarea_seleccion)

        print(f"Bubble Sort: {tiempo_bubble_ms * 1000:.3f} ms")
        print(f"Bubble Sort Optimizado: {tiempo_optimizado_ms * 1000:.3f} ms")
        print(f"Selección: {tiempo_seleccion_ms * 1000:.3f} ms")


        