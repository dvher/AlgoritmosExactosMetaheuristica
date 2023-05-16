from typing import List, Tuple
import random

VALOR_INFACTIBLE = 100

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
            costo += uavs[i][1] - tiempo_aterrizaje
            orden_costos[i] = uavs[i][1] - tiempo_aterrizaje
        elif tiempo_aterrizaje > uavs[i][1]:
            # Costo adicional por estar por arriba del tiempo preferente mientras mas lejos mas costo
            costo += tiempo_aterrizaje - uavs[i][1]
            orden_costos[i] = tiempo_aterrizaje - uavs[i][1]
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
        diferencia = uavs[i][2] - uavs[i][0]
        if diferencia != 0:
            porcentaje = diferencia * 0.10 # Mientras mayor sea el porcentaje mas dispersos los tiempos que tomará, y más probabilidad de caer en soluciones infactibles
            rango_tiempo = list(range(t_sig_aterrizaje, t_sig_aterrizaje + int(porcentaje)))
            tiempo_aterrizaje = random.choice(rango_tiempo)
            tiempos_aterrizaje[i] = tiempo_aterrizaje
        else: 
            tiempo_aterrizaje = diferencia
        if tiempo_aterrizaje < uavs[i][1]:
            # Costo adicional por estar por debajo del tiempo preferente
            costo += uavs[i][1] - tiempo_aterrizaje
            orden_costos[i] = uavs[i][1] - tiempo_aterrizaje
        elif tiempo_aterrizaje > uavs[i][1]:
            # Costo adicional por estar por arriba del tiempo preferente mientras mas lejos mas costo
            costo += tiempo_aterrizaje - uavs[i][1]
            orden_costos[i] = tiempo_aterrizaje - uavs[i][1]
        elif tiempo_aterrizaje > uavs[i][2]:
            # Muy costoso solucion pasa a ser infactible
            costo += (tiempo_aterrizaje - uavs[i][2]) * VALOR_INFACTIBLE
            orden_costos[i] = (tiempo_aterrizaje - uavs[i][2]) * VALOR_INFACTIBLE
        else:
            costo += 0 #Está en el tiempo preferente
            orden_costos[i] = 0

    return costo, tiempos_aterrizaje, orden, orden_costos
