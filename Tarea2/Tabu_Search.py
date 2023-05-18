from typing import List, Tuple, Literal
import copy

def tabu_search(num_uavs: int, uavs: List[Tuple[int, int, int]], t_espera: List[List[int]], costo_actual: int, solucion_anterior: List[int], orden: List[int], costos: List[int]) -> Tuple[int, List[int], List[int], Literal['Factible', 'Infactible']]:
    """Funcion que optimiza la solucion actual utilizando la metaheuristica Tabu Search

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
    """
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
    return mejor_costo, mejor_solucion, mejor_num_iteraciones, mejor_factibilidad