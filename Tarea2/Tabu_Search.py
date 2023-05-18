from typing import List, Tuple, Literal
from Hill_Climbing import hill_climbing_mejor
import copy
import random

VALOR_INFACTIBLE = 100

def tabu_search(num_uavs: int, uavs: List[Tuple[int, int, int]], t_espera: List[List[int]], costo_actual: int, solucion_anterior: List[int], orden: List[int], costos: List[int]) -> Tuple[int, List[int], List[int], Literal['Factible', 'Infactible']]:
    soluciones = []
    soluciones.append((costo_actual, solucion_anterior, costos, orden))
    boolean = True
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
        for n, i in enumerate(nuevo_orden):
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


"""def tabu_search(num_uavs: int, uavs: List[Tuple[int, int, int]], t_espera: List[List[int]], costo_actual: int, solucion_anterior: List[int], orden: List[int], costos: List[int]) -> Tuple[int, List[int], List[int], Literal['Factible', 'Infactible']]:
    Funcion que optimiza la solucion actual utilizando la metaheuristica Tabu Search

    Args:
        num_uavs (int): Numero de UAVs
        uavs (List[Tuple[int, int, int]]): Lista de tuplas con las coordenadas de los UAVs
        t_espera (List[List[int]]): Matriz de tiempos de espera entre los UAVs
        costo_actual ([int]): Costo actual de la solucion
        solucion_anterior (List[int]): Solucion anterior
        orden (List[int]): Lista con el orden de los UAVs
        costos (List[int]): Lista de costos de los UAVs

    Returns:
        Tuple[int, List[int], List[int], Literal['Factible', 'Infactible']]: Tupla con el costo de la solucion, la solucion, la lista de costos y si es factible o no
    
    # Se inicializa la solucion actual, la solucion anterior y el costo de la solucion
    solucion_actual = copy.deepcopy(orden)
    solucion_anterior = copy.deepcopy(solucion_anterior)
    costo_actual = copy.deepcopy(costo_actual)
    # Se inicializa la lista tabu con una lista vacia
    tabu = []
    # Se inicializa el numero de iteraciones en 0
    num_iteraciones = 0
    # Se inicializa la variable de parada en False
    parada = False
    # Se inicializa la variable de factibilidad en 'Factible'
    factibilidad = 'Factible'
    # Se inicializa la variable de mejor solucion en la solucion actual
    mejor_solucion = solucion_actual
    # Se inicializa la variable de mejor costo en el costo actual
    mejor_costo = costo_actual
    # Se inicializa la variable de mejor numero de iteraciones en 0
    mejor_num_iteraciones = num_iteraciones
    # Se inicializa la variable de mejor factibilidad en 'Factible'
    mejor_factibilidad = factibilidad
    # Se itera mientras no se alcance la condicion de parada
    while not parada:
        # Se inicializa el costo minimo en un valor muy grande
        costo_minimo = 99999
        # Se inicializa el indice del UAV con el costo minimo en -1
        indice_uav_minimo = -1
        # Se itera sobre los UAVs
        for i in range(num_uavs):
            # Si el UAV no esta en la lista tabu
            if i not in tabu:
                # Se calcula el costo del UAV
                costo_uav = costos[i]
                # Se itera sobre los UAVs
                for j in range(num_uavs):
                    # Si el UAV no es el mismo y no esta en la lista tabu
                    if i != j and j not in tabu:
                        # Se calcula el costo del UAV
                        costo_uav += t_espera[i][j]
                # Si el costo del UAV es menor al costo minimo
                if costo_uav < costo_minimo:
                    # Se actualiza el costo minimo
                    costo_minimo = costo_uav
                    # Se actualiza el indice del UAV con el costo minimo
                    indice_uav_minimo = i
        # Se agrega el UAV con el costo minimo a la lista tabu
        tabu.append(indice_uav_minimo)
        # Se actualiza el costo actual
        costo_actual += costo_minimo
        # Se actualiza la solucion actual
        solucion_actual[indice_uav_minimo] = num_iteraciones
        # Se actualiza el numero de iteraciones
        num_iteraciones += 1
        # Si el costo actual es menor al mejor costo
        if costo_actual < mejor_costo:
            # Se actualiza la mejor solucion
            mejor_solucion = copy.deepcopy(solucion_actual)
            # Se actualiza el mejor costo
            mejor_costo = costo_actual
            # Se actualiza el mejor numero de iteraciones
            mejor_num_iteraciones = num_iteraciones
            # Se actualiza la mejor factibilidad
            mejor_factibilidad = factibilidad
        # Si el numero de iteraciones es igual a 100
        if num_iteraciones == 100:
            # Se actualiza la variable de parada
            parada = True
        # Si el costo actual es mayor al mejor costo
        if costo_actual > mejor_costo:
            # Se actualiza la variable de parada
            parada = True
            # Se actualiza la variable de factibilidad
            factibilidad = 'Infactible'
    # Se retorna la mejor solucion, el mejor costo, la mejor factibilidad y el mejor numero de iteraciones
    return mejor_costo, mejor_solucion, mejor_num_iteraciones, mejor_factibilidad"""