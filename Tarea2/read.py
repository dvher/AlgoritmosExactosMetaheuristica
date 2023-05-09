from typing import List, Tuple
import random

VALOR_INFACTIBLE = 100

def read_file(file_name: str) -> Tuple[int, List[List[int]], List[List[int]]]:
    tiempos_aterrizaje = []
    tiempos_requeridos = []

    with open(file_name, 'r') as f:
        lines = [line.strip() for line in f.readlines()]

    num_uavs = int(lines.pop(0))

    while len(lines) != 0:
        tiempos_aterrizaje.append(tuple(map(int, lines.pop(0).split())))

        tiempos_requeridos_i = []
        while len(tiempos_requeridos_i) < num_uavs:
            tiempos_requeridos_i.extend(list(map(int, lines.pop(0).split())))

        tiempos_requeridos.append(tiempos_requeridos_i)

    return num_uavs, tiempos_aterrizaje, tiempos_requeridos

def ordenar_tiempos_preferentes(num_uavs: int, uavs: List[List[int]]) -> List[int]:
    return sorted(range(num_uavs), key=lambda i: uavs[i][1])


def greedy_determinista(num_uavs: int, uavs: List[List[int]], t_espera: List[List[int]]) -> Tuple[int, List[int]]:
    orden = ordenar_tiempos_preferentes(num_uavs, uavs)  # Ordena los UAV por tiempo preferente
    tiempos_aterrizaje = [0] * num_uavs # Hace un arreglo de 0ros de tamaño num_uavs
    costo = 0

    for ord_actual, i in enumerate(orden):
        tiempo_aterrizaje = max(uavs[i][0], tiempos_aterrizaje[orden[ord_actual - 1]] + t_espera[orden[ord_actual - 1]][i] if i > 0 else 0)
        tiempos_aterrizaje[i] = tiempo_aterrizaje
        if tiempo_aterrizaje < uavs[i][1]:
            costo += (uavs[i][1] - tiempo_aterrizaje) * 2  # Costo adicional por estar por debajo del tiempo preferente
        elif tiempo_aterrizaje > uavs[i][2]:
            costo += (tiempo_aterrizaje - uavs[i][2]) * VALOR_INFACTIBLE # Muy costoso solucion pasa a ser infactible
        else:
            costo += abs(tiempo_aterrizaje - uavs[i][1])


    return costo, tiempos_aterrizaje

def greedy_estocastico(num_uavs: int, uavs: List[List[int]], t_espera: List[List[int]], seed: int) -> Tuple[int, List[int]]:

    random.seed(seed)

    orden = ordenar_tiempos_preferentes(num_uavs, uavs)  # Ordena los UAV por tiempo preferente
    tiempos_aterrizaje = [0] * num_uavs # Hace un arreglo de 0ros de tamaño num_uavs
    costo = 0

    for ord_actual, i in enumerate(orden):
        t_sig_aterrizaje = max(uavs[i][0], tiempos_aterrizaje[orden[ord_actual - 1]] + t_espera[orden[ord_actual - 1]][i] if i > 0 else 0)
        rango_tiempo = list(range(t_sig_aterrizaje, t_sig_aterrizaje + 50)) # Aca para hacerlo estocastico que elija entre un rango de tiempos desde el que puede aterrizar
        tiempo_aterrizaje = random.choice(rango_tiempo)
        tiempos_aterrizaje[i] = tiempo_aterrizaje
        if tiempo_aterrizaje < uavs[i][1]:
            costo += (uavs[i][1] - tiempo_aterrizaje) * 2  # Costo adicional por estar por debajo del tiempo preferente
        elif tiempo_aterrizaje > uavs[i][2]:
            costo += (tiempo_aterrizaje - uavs[i][2]) * VALOR_INFACTIBLE # Muy costoso solucion pasa a ser infactible
        else:
            costo += abs(tiempo_aterrizaje - uavs[i][1])


    return costo, tiempos_aterrizaje



archivo = 'C:/Users/Ketbome/Desktop/AlgoritmosExactosMetaheuristica/Tarea2/t2_Titan.txt'

num_uavs, uavs, t_espera = read_file(archivo)
costo_determinista, tiempos_aterrizaje_determinista = greedy_determinista(num_uavs, uavs, t_espera)
print(f"Archivo: {archivo}")
print(f"Greedy Determinista - Costo: {costo_determinista}")
print(f"Tiempos de aterrizaje: {tiempos_aterrizaje_determinista}")
print("Greedy Estocástico:")
for seed in range(5):
    costo_estocastico, tiempos_aterrizaje_estocastico = greedy_estocastico(num_uavs, uavs, t_espera, seed)
    print(f"  Seed {seed} - Costo: {costo_estocastico}")
    print(f"  Tiempos de aterrizaje: {tiempos_aterrizaje_estocastico}")
print()
