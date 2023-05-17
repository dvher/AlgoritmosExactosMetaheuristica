from typing import List, Tuple
import copy

VALOR_INFACTIBLE = 100

"""
def hill_climbing(num_uavs: int, uavs: List[List[int]], t_espera: List[List[int]], costo_actual, solucion_anterior, orden, costos) -> Tuple[int, List[int]]:
    tiempos_aterrizaje_actual = solucion_anterior.copy()
    costo_orden = costos.copy()
    fact = "Factible"
    
    for n, i in enumerate(orden):
        if tiempos_aterrizaje_actual[i] < uavs[i][1]:
            # Se ve si se puede mejorar el tiempo acercandolo a el tiempo preferente para bajar el costo
            if n >= 14: # en el caso de ser el último al ser menor el tiempo de aterrizaje que el preferente, este puede llegar al preferente dado que no hay naves que deban aterrizar despues de él
                nuevo_tiempo_aterrizaje = uavs[i][1]
                nuevo_costo = 0
                if nuevo_costo < costo_orden[i]: # Si el costo nuevo es menor se agrega y tiempos de aterrizaje recien se actualiza
                    costo_actual += nuevo_costo - costo_orden[i]
                    costo_orden[i] = nuevo_costo
                    tiempos_aterrizaje_actual[i] = nuevo_tiempo_aterrizaje
            elif tiempos_aterrizaje_actual[orden[n + 1]] - t_espera[orden[n]][i] < uavs[i][1]: # Se ve el tiempo de aterrizaje al siguiente y se le resta la espera
                nuevo_tiempo_aterrizaje = tiempos_aterrizaje_actual[orden[n + 1]] - t_espera[orden[n]][i]
                nuevo_costo = uavs[i][1] - nuevo_tiempo_aterrizaje
                if nuevo_costo < costo_orden[i]: # Si el nuevo costo es menor se agrega y se actualiza el aterrizaje
                    costo_actual += nuevo_costo - costo_orden[i]
                    costo_orden[i] = nuevo_costo
                    tiempos_aterrizaje_actual[i] = nuevo_tiempo_aterrizaje
            else:
                nuevo_tiempo_aterrizaje = uavs[i][1]
                nuevo_costo = 0
                if nuevo_costo < costo_orden[i]:
                    costo_actual += nuevo_costo - costo_orden[i]
                    costo_orden[i] = nuevo_costo
                    tiempos_aterrizaje_actual[i] = nuevo_tiempo_aterrizaje
        elif tiempos_aterrizaje_actual[i] > uavs[i][1]:
            # Se ve si se puede mejorar el tiempo acercandolo a el tiempo preferente para bajar el costo
            if n <= 0: # Si es mayor el tiempo de aterrizaje de la primera nave que el preferente puede tomar altiro el tiempo mas optimo
                nuevo_tiempo_aterrizaje = uavs[i][1]
                nuevo_costo = 0
                if nuevo_costo < costo_orden[i]:
                    costo_actual += nuevo_costo - costo_orden[i]
                    costo_orden[i] = nuevo_costo
                    tiempos_aterrizaje_actual[i] = nuevo_tiempo_aterrizaje
            elif tiempos_aterrizaje_actual[orden[n - 1]] + t_espera[orden[n - 1]][i] > uavs[i][1]:
                nuevo_tiempo_aterrizaje = tiempos_aterrizaje_actual[orden[n - 1]] + t_espera[orden[n - 1]][i]
                if tiempos_aterrizaje_actual[orden[n - 1]] + t_espera[orden[n - 1]][i] > uavs[i][2]:
                    fact = "Infactible"
                    nuevo_costo = nuevo_tiempo_aterrizaje - uavs[i][1] * VALOR_INFACTIBLE
                else: 
                    nuevo_costo = nuevo_tiempo_aterrizaje - uavs[i][1]
                if nuevo_costo < costo_orden[i]:
                    costo_actual += nuevo_costo - costo_orden[i]
                    costo_orden[i] = nuevo_costo
                    tiempos_aterrizaje_actual[i] = nuevo_tiempo_aterrizaje
                    if tiempos_aterrizaje_actual[i] > uavs[i][2]:
                        fact = "Infactible"
                    else: 
                        fact = "Factible"
            else:
                nuevo_tiempo_aterrizaje = uavs[i][1]
                nuevo_costo = 0
                if nuevo_costo < costo_orden[i]:
                    costo_actual += nuevo_costo - costo_orden[i]
                    costo_orden[i] = nuevo_costo
                    tiempos_aterrizaje_actual[i] = nuevo_tiempo_aterrizaje


    return costo_actual, tiempos_aterrizaje_actual, costo_orden, fact
"""

# Hill climbing alguna mejora evalua la primera mejora y la aplica
def hill_climbing(num_uavs: int, uavs: List[Tuple[int, int, int]], t_espera: List[List[int]],costo_actual: int, solucion_anterior: List[int], orden: List[int], costos: List[int]) -> Tuple[int, List[int]]:
    tiempos_aterrizaje_actual = copy.deepcopy(solucion_anterior)
    costo_orden = copy.deepcopy(costos)
    boolean = True
    fact = "Factible"
    while(boolean):
        cambios = 0
        for n, i in enumerate(orden):
            if tiempos_aterrizaje_actual[i] < uavs[i][1]:
                # Se ve si se puede mejorar el tiempo acercandolo a el tiempo preferente para bajar el costo
                if n >= 14:
                    nuevo_tiempo_aterrizaje = uavs[i][1]
                    nuevo_costo = 0
                    if nuevo_costo < costo_orden[i]:
                        costo_actual += nuevo_costo - costo_orden[i]
                        costo_orden[i] = nuevo_costo
                        tiempos_aterrizaje_actual[i] = nuevo_tiempo_aterrizaje
                        cambios += 1
                elif tiempos_aterrizaje_actual[orden[n + 1]] - t_espera[orden[n]][i] < uavs[i][1]:
                    nuevo_tiempo_aterrizaje = tiempos_aterrizaje_actual[orden[n + 1]] - t_espera[orden[n]][i]
                    nuevo_costo = uavs[i][1] - nuevo_tiempo_aterrizaje
                    if nuevo_costo < costo_orden[i]:
                        costo_actual += nuevo_costo - costo_orden[i]
                        costo_orden[i] = nuevo_costo
                        tiempos_aterrizaje_actual[i] = nuevo_tiempo_aterrizaje
                        cambios += 1
                else:
                    nuevo_tiempo_aterrizaje = uavs[i][1]
                    nuevo_costo = 0
                    if nuevo_costo < costo_orden[i]:
                        costo_actual += nuevo_costo - costo_orden[i]
                        costo_orden[i] = nuevo_costo
                        tiempos_aterrizaje_actual[i] = nuevo_tiempo_aterrizaje
                        cambios += 1
            elif tiempos_aterrizaje_actual[i] > uavs[i][1]:
                # Se ve si se puede mejorar el tiempo acercandolo a el tiempo preferente para bajar el costo
                if n <= 0:
                    nuevo_tiempo_aterrizaje = uavs[i][1]
                    nuevo_costo = 0
                    if nuevo_costo < costo_orden[i]:
                        costo_actual += nuevo_costo - costo_orden[i]
                        costo_orden[i] = nuevo_costo
                        tiempos_aterrizaje_actual[i] = nuevo_tiempo_aterrizaje
                        cambios += 1
                elif tiempos_aterrizaje_actual[orden[n - 1]] + t_espera[orden[n - 1]][i] > uavs[i][1]:
                    nuevo_tiempo_aterrizaje = tiempos_aterrizaje_actual[orden[n - 1]] + t_espera[orden[n - 1]][i]
                    if tiempos_aterrizaje_actual[orden[n - 1]] + t_espera[orden[n - 1]][i] > uavs[i][2]:
                        fact = "Infactible"
                        nuevo_costo = (nuevo_tiempo_aterrizaje - uavs[i][1]) * VALOR_INFACTIBLE
                    else: 
                        nuevo_costo = nuevo_tiempo_aterrizaje - uavs[i][1]
                    if nuevo_costo < costo_orden[i]:
                        costo_actual += nuevo_costo - costo_orden[i]
                        costo_orden[i] = nuevo_costo
                        tiempos_aterrizaje_actual[i] = nuevo_tiempo_aterrizaje
                        if tiempos_aterrizaje_actual[i] > uavs[i][2]:
                            fact = "Infactible"
                        else: 
                            fact = "Factible"
                else:
                    nuevo_tiempo_aterrizaje = uavs[i][1]
                    nuevo_costo = 0
                    if nuevo_costo < costo_orden[i]:
                        costo_actual += nuevo_costo - costo_orden[i]
                        costo_orden[i] = nuevo_costo
                        tiempos_aterrizaje_actual[i] = nuevo_tiempo_aterrizaje
                        cambios += 1
        if cambios == 0:
            boolean = False


    return costo_actual, tiempos_aterrizaje_actual, costo_orden, fact

# Hill climbing mejor mejora evalua la mejor mejora a hacer y la aplica, cuando ya no hayan mejoras termina
def hill_climbing_mejor(num_uavs: int, uavs: List[Tuple[int, int, int]], t_espera: List[List[int]],costo_actual: int, solucion_anterior: List[int], orden: List[int], costos: List[int]) -> Tuple[int, List[int]]:
    tiempos_aterrizaje_actual = copy.deepcopy(solucion_anterior)
    costo_orden = copy.deepcopy(costos)
    boolean = True
    fact = "Factible"
    while(boolean):
        cambios = 0
        Mas_mejora = 0
        for n, i in enumerate(orden):
            if tiempos_aterrizaje_actual[i] < uavs[i][1]:
                # Se ve si se puede mejorar el tiempo acercandolo a el tiempo preferente para bajar el costo
                if n >= 14:
                    nuevo_tiempo_aterrizaje = uavs[i][1]
                    nuevo_costo = 0
                    if nuevo_costo < costo_orden[i]:
                        mejora = abs(costo_orden[i] - nuevo_costo)
                        if mejora > Mas_mejora:
                            Mas_mejora = mejora
                            UAV_mejor = i
                            costo_mejor = nuevo_costo
                            nuevo_aterrizaje_mejor = nuevo_tiempo_aterrizaje 
                elif tiempos_aterrizaje_actual[orden[n + 1]] - t_espera[orden[n]][i] < uavs[i][1]:
                    nuevo_tiempo_aterrizaje = tiempos_aterrizaje_actual[orden[n + 1]] - t_espera[orden[n]][i]
                    nuevo_costo = uavs[i][1] - nuevo_tiempo_aterrizaje
                    if nuevo_costo < costo_orden[i]:
                        mejora = abs(costo_orden[i] - nuevo_costo)
                        if mejora > Mas_mejora:
                            Mas_mejora = mejora
                            UAV_mejor = i
                            costo_mejor = nuevo_costo
                            nuevo_aterrizaje_mejor = nuevo_tiempo_aterrizaje 
                else:
                    nuevo_tiempo_aterrizaje = uavs[i][1]
                    nuevo_costo = 0
                    if nuevo_costo < costo_orden[i]:
                        mejora = abs(costo_orden[i] - nuevo_costo)
                        if mejora > Mas_mejora:
                            Mas_mejora = mejora
                            UAV_mejor = i
                            costo_mejor = nuevo_costo
                            nuevo_aterrizaje_mejor = nuevo_tiempo_aterrizaje 
            elif tiempos_aterrizaje_actual[i] > uavs[i][1]:
                # Se ve si se puede mejorar el tiempo acercandolo a el tiempo preferente para bajar el costo
                if n <= 0:
                    nuevo_tiempo_aterrizaje = uavs[i][1]
                    nuevo_costo = 0
                    if nuevo_costo < costo_orden[i]:
                        mejora = abs(costo_orden[i] - nuevo_costo)
                        if mejora > Mas_mejora:
                            Mas_mejora = mejora
                            UAV_mejor = i
                            costo_mejor = nuevo_costo
                            nuevo_aterrizaje_mejor = nuevo_tiempo_aterrizaje 
                elif tiempos_aterrizaje_actual[orden[n - 1]] + t_espera[orden[n - 1]][i] > uavs[i][1] and tiempos_aterrizaje_actual[orden[n - 1]] + t_espera[orden[n - 1]][i] <= uavs[i][2]:
                    nuevo_tiempo_aterrizaje = tiempos_aterrizaje_actual[orden[n - 1]] + t_espera[orden[n - 1]][i]
                    nuevo_costo = nuevo_tiempo_aterrizaje - uavs[i][1]
                    if nuevo_costo < costo_orden[i]:
                        mejora = abs(costo_orden[i] - nuevo_costo)
                        if mejora > Mas_mejora:
                            Mas_mejora = mejora
                            UAV_mejor = i
                            costo_mejor = nuevo_costo
                            nuevo_aterrizaje_mejor = nuevo_tiempo_aterrizaje 
                elif tiempos_aterrizaje_actual[orden[n - 1]] + t_espera[orden[n - 1]][i] > uavs[i][2]: 
                    nuevo_tiempo_aterrizaje = tiempos_aterrizaje_actual[orden[n - 1]] + t_espera[orden[n - 1]][i]   
                    fact = "Infactible"
                    nuevo_costo = (nuevo_tiempo_aterrizaje - uavs[i][1]) * VALOR_INFACTIBLE
                    mejora = abs(costo_orden[i] - nuevo_costo)
                    if mejora > Mas_mejora:
                        Mas_mejora = mejora
                        UAV_mejor = i
                        costo_mejor = nuevo_costo
                        nuevo_aterrizaje_mejor = nuevo_tiempo_aterrizaje
                else:
                    nuevo_tiempo_aterrizaje = uavs[i][1]
                    nuevo_costo = 0
                    if nuevo_costo < costo_orden[i]:
                        mejora = abs(costo_orden[i] - nuevo_costo)
                        if mejora > Mas_mejora:
                            Mas_mejora = mejora
                            UAV_mejor = i
                            costo_mejor = nuevo_costo
                            nuevo_aterrizaje_mejor = nuevo_tiempo_aterrizaje 
        # Se hace la modificación al que tiene mayor mejora en el costo
        if Mas_mejora != 0:
            costo_actual += costo_mejor - costo_orden[UAV_mejor]
            costo_orden[UAV_mejor] = costo_mejor
            tiempos_aterrizaje_actual[UAV_mejor] = nuevo_aterrizaje_mejor
            if tiempos_aterrizaje_actual[UAV_mejor] > uavs[UAV_mejor][2]:
                fact = "Infactible"
            else:
                fact = "Factible"
        elif cambios == 0: # No se hicieron cambios
            boolean = False


    return costo_actual, tiempos_aterrizaje_actual, costo_orden, fact