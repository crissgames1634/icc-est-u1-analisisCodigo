import bechmarking as bm
#from bechmarking import Benchmarking
from metodo_ordenamiento import MetodoOrdenamiento
# Archivo pricipal
if __name__ == "__main__":
    print("Funciona")
    bench = bm.Benchmarking()
    metodosO = MetodoOrdenamiento()

    ##tam = 10000
    tamanios = [5000, 10000, 1500]
    resulatdos = []
    arreglo_base = bench.build_arreglo(tamanios)

    key = "burbuja",
    value = metodosO.sort_bubble

    metodos_dic ={
        "burbuja": metodosO.sort_bubble,
        "inserccion" : metodosO.sort_burbuja_mejorado_optimizado,
        "seleccion" :metodosO.sort_seleccion,
        "shell": metodosO.sort_shell
    }
    resultados =[]

    for nombre, fun_metodo in metodos_dic.items():
        tiempo_resultado = bench.contar_con_nanosegundos(fun_metodo, arreglo_base)
        tupla_resultado = (tamanios, nombre, tiempo_resultado)
        resultados.append(tupla_resultado)
    
    for tamanios, nombre, tiempo in resultados:
        print(f'Tamaño:{tamanios}, nombre metodo: {nombre}, tiempo {tiempo:.6f},segundos')


    