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
    # Ordena los UAV por tiempo preferente
    orden = ordenar_tiempos_preferentes(num_uavs, uavs)
    # Hace un arreglo de 0ros de tamaño num_uavs
    tiempos_aterrizaje = [0] * num_uavs
    orden_costos = [0] * num_uavs
    costo = 0

    for ord_actual, i in enumerate(orden):
        tiempo_aterrizaje = max(uavs[i][1], tiempos_aterrizaje[orden[ord_actual - 1]
                                                               ] + t_espera[orden[ord_actual - 1]][i] if i > 0 else 0)
        tiempos_aterrizaje[i] = tiempo_aterrizaje
        if tiempo_aterrizaje < uavs[i][1]:
            # Costo adicional por estar por debajo del tiempo preferente
            costo += uavs[i][1] - tiempo_aterrizaje + 1
            orden_costos[i] = uavs[i][1] - tiempo_aterrizaje + 1
        elif tiempo_aterrizaje > uavs[i][1]:
            # Costo adicional por estar por arriba del tiempo preferente mientras mas lejos mas costo
            costo += tiempo_aterrizaje - uavs[i][1] + 1
            orden_costos[i] = tiempo_aterrizaje - uavs[i][1] + 1
        elif tiempo_aterrizaje > uavs[i][2]:
            # Muy costoso solucion pasa a ser infactible
            costo += (tiempo_aterrizaje - uavs[i][2]) * VALOR_INFACTIBLE
            orden_costos[i] = (tiempo_aterrizaje - uavs[i][2]) * VALOR_INFACTIBLE
        else:
            costo += 0 #Está en el tiempo preferente
            orden_costos[i] = 0

    return costo, tiempos_aterrizaje, orden, orden_costos


def greedy_estocastico(num_uavs: int, uavs: List[List[int]], t_espera: List[List[int]], seed: int) -> Tuple[int, List[int]]:
    random.seed(seed)

    # Ordena los UAV por tiempo preferente
    orden = ordenar_tiempos_preferentes(num_uavs, uavs)
    # Hace un arreglo de 0ros de tamaño num_uavs
    tiempos_aterrizaje = [0] * num_uavs
    orden_costos = [0] * num_uavs
    costo = 0

    for ord_actual, i in enumerate(orden):
        t_sig_aterrizaje = max(uavs[i][0], tiempos_aterrizaje[orden[ord_actual - 1]
                                                              ] + t_espera[orden[ord_actual - 1]][i] if i > 0 else 0)
        # Aca para hacerlo estocastico que elija entre un rango de tiempos desde el que puede aterrizar
        rango_tiempo = list(range(t_sig_aterrizaje, t_sig_aterrizaje + 20))
        tiempo_aterrizaje = random.choice(rango_tiempo)
        tiempos_aterrizaje[i] = tiempo_aterrizaje
        if tiempo_aterrizaje < uavs[i][1]:
            # Costo adicional por estar por debajo del tiempo preferente
            costo += uavs[i][1] - tiempo_aterrizaje + 1
            orden_costos[i] = uavs[i][1] - tiempo_aterrizaje + 1
        elif tiempo_aterrizaje > uavs[i][1]:
            # Costo adicional por estar por arriba del tiempo preferente mientras mas lejos mas costo
            costo += tiempo_aterrizaje - uavs[i][1] + 1
            orden_costos[i] = tiempo_aterrizaje - uavs[i][1] + 1
        elif tiempo_aterrizaje > uavs[i][2]:
            # Muy costoso solucion pasa a ser infactible
            costo += (tiempo_aterrizaje - uavs[i][2]) * VALOR_INFACTIBLE
            orden_costos[i] = (tiempo_aterrizaje - uavs[i][2]) * VALOR_INFACTIBLE
        else:
            costo += 0 #Está en el tiempo preferente
            orden_costos[i] = 0

    return costo, tiempos_aterrizaje, orden, orden_costos


#def hill_climbing(num_uavs: int, uavs: List[List[int]], t_espera: List[List[int]], costo_actual, tiempos_aterrizaje_actual, orden) -> Tuple[int, List[int]]:
    

    return costo_actual, tiempos_aterrizaje_actual


archivo = 'C:/Users/Ketbome/Desktop/AlgoritmosExactosMetaheuristica/Tarea2/t2_Titan.txt'

num_uavs, uavs, t_espera = read_file(archivo)
costo_determinista, tiempos_aterrizaje_determinista, orden, orden_costos = greedy_determinista(
    num_uavs, uavs, t_espera)
print(f"Archivo: {archivo}")
print(f"Greedy Determinista - Costo: {costo_determinista}, {orden_costos}")
print(f"Tiempos de aterrizaje: {tiempos_aterrizaje_determinista}")
#print("Hill Climbing - Greedy determinista:")
#costo_hill_climbing, tiempos_aterrizaje_hill_climbing = hill_climbing(
#    num_uavs, uavs, t_espera, costo_determinista, tiempos_aterrizaje_determinista, orden)
#print(f"  Seed {0} - Costo: {costo_hill_climbing}, {orden_costos}")
#print(f"  Tiempos de aterrizaje: {tiempos_aterrizaje_hill_climbing}")
print()
for seed in range(5):
    print(f"Greedy Estocástico seed {seed}:")
    costo_estocastico, tiempos_aterrizaje_estocastico, orden, orden_costos = greedy_estocastico(
        num_uavs, uavs, t_espera, seed)
    print(f"  Seed {seed} - Costo: {costo_estocastico}")
    print(f"  Tiempos de aterrizaje: {tiempos_aterrizaje_estocastico}")
#    print(f"  Hill Climbing - Greedy estocastico:")
#    costo_hill_climbing, tiempos_aterrizaje_hill_climbing = hill_climbing(
#        num_uavs, uavs, t_espera, seed, 1000, costo_estocastico, tiempos_aterrizaje_estocastico, orden)
#    print(f"     Seed {seed} - Costo: {costo_hill_climbing}")
#    print(f"     Tiempos de aterrizaje: {tiempos_aterrizaje_hill_climbing}")
    print()
print()
