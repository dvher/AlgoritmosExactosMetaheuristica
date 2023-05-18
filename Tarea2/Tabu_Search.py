from typing import List, Tuple, Literal
from Hill_Climbing import hill_climbing_mejor
import copy
import random

VALOR_INFACTIBLE = 100

def tabu_search(num_uavs: int, uavs: List[List[int]], t_espera: List[List[int]], costo_actual: int, solucion_anterior: List[int], orden: List[int], costos: List[int]) -> Tuple[int, List[int], List[int], Literal['Factible', 'Infactible']]:
    soluciones = []
    soluciones.append((costo_actual, solucion_anterior, costos, orden))
    fact = "Factible"
    # Se comienza con un cambio de orden para probar soluciones Exploración
    swaps = int(num_uavs * 0.20) # Un 20% del valor de los números de UAVs harán swaps
    # Se harán 5 soluciones como espacio del tabu search
    for i in range(swaps):
        costo_total = 0
        tiempos_aterrizaje_actual = copy.deepcopy(solucion_anterior)
        costo_orden = copy.deepcopy(costos)
        nuevo_orden = copy.deepcopy(orden)
        nuevo_orden = random_swaps(nuevo_orden, swaps) # Se le pasa un orden el cual va a cambiarlo a sectores vecinos
        tiempos_aterrizaje_actual = random_swaps(tiempos_aterrizaje_actual, swaps)
        for _, i in enumerate(nuevo_orden):
            #Calcular nuevo costo
            if tiempos_aterrizaje_actual[i] < uavs[i][0]: #Infactible
                costo_total += abs(tiempos_aterrizaje_actual[i] - uavs[i][0]) * VALOR_INFACTIBLE
                costo_orden[i] = abs(tiempos_aterrizaje_actual[i] - uavs[i][0]) * VALOR_INFACTIBLE
            elif tiempos_aterrizaje_actual[i] > uavs[i][2]: #Infactible
                costo_total += abs(tiempos_aterrizaje_actual[i] - uavs[i][0]) * VALOR_INFACTIBLE
                costo_orden[i] = abs(tiempos_aterrizaje_actual[i] - uavs[i][0]) * VALOR_INFACTIBLE
            elif tiempos_aterrizaje_actual[i] == uavs[i][1]:
                costo_orden[i] = 0
            else: #Factible
                costo_total += abs(tiempos_aterrizaje_actual[i] - uavs[i][0])
                costo_orden[i] = abs(tiempos_aterrizaje_actual[i] - uavs[i][0])

        # Se aplican las condiciones
        costo_hill_climbing, tiempos_aterrizaje_hill_climbing, orden_costos_hill, fact = hill_climbing_mejor(num_uavs, uavs, t_espera, costo_total, tiempos_aterrizaje_actual, nuevo_orden, costo_orden)
        soluciones.append((costo_hill_climbing, tiempos_aterrizaje_hill_climbing, orden_costos_hill, nuevo_orden))


    #Se evalúa manda la mejor solucion encontrada
    min_value = 999999
    min_index = 0
    for i in range(len(soluciones)):
        if i != 0:
            if soluciones[i][0] < min_value:
                min_value = soluciones[i][0]
                min_index = i
            #print(soluciones[i][0])
    for n, i in enumerate(soluciones[min_index][3]):
        if soluciones[min_index][1][i] > uavs[i][2] or soluciones[min_index][1][i] < uavs[i][0]:
            fact = "Infactible"

    return soluciones[min_index][0], soluciones[min_index][1], soluciones[min_index][2], fact

def random_swaps(arr, n):
    swapped_indices = set()

    for _ in range(n):
        i = random.randint(0, len(arr) - 2)
        if i not in swapped_indices and i + 1 not in swapped_indices:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            swapped_indices.add(i)
            swapped_indices.add(i + 1)

    return arr
