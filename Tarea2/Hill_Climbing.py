from typing import List, Tuple

def hill_climbing(num_uavs: int, uavs: List[List[int]], t_espera: List[List[int]], costo_actual, solucion_anterior, orden, costos) -> Tuple[int, List[int]]:
    tiempos_aterrizaje_actual = solucion_anterior.copy()
    costo_orden = costos.copy()
    
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
            elif tiempos_aterrizaje_actual[orden[n + 1]] - t_espera[orden[n + 1]][i] < uavs[i][1]:
                nuevo_tiempo_aterrizaje = tiempos_aterrizaje_actual[orden[n + 1]] - t_espera[orden[n + 1]][i]
                nuevo_costo = uavs[i][1] - nuevo_tiempo_aterrizaje
                if nuevo_costo < costo_orden[i]:
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
            if n <= 0:
                nuevo_tiempo_aterrizaje = uavs[i][1]
                nuevo_costo = 0
                if nuevo_costo < costo_orden[i]:
                    costo_actual += nuevo_costo - costo_orden[i]
                    costo_orden[i] = nuevo_costo
                    tiempos_aterrizaje_actual[i] = nuevo_tiempo_aterrizaje
            elif tiempos_aterrizaje_actual[orden[n - 1]] + t_espera[orden[n - 1]][i] > uavs[i][1]:
                nuevo_tiempo_aterrizaje = tiempos_aterrizaje_actual[orden[n - 1]] + t_espera[orden[n - 1]][i]
                nuevo_costo = nuevo_tiempo_aterrizaje - uavs[i][1]
                if nuevo_costo < costo_orden[i]:
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


    return costo_actual, tiempos_aterrizaje_actual, costo_orden


def hill_climbing_mejor(num_uavs: int, uavs: List[List[int]], t_espera: List[List[int]], costo_actual, solucion_anterior, orden, costos) -> Tuple[int, List[int]]:
    tiempos_aterrizaje_actual = solucion_anterior.copy()
    costo_orden = costos.copy()
    boolean = True
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
                elif tiempos_aterrizaje_actual[orden[n + 1]] - t_espera[orden[n + 1]][i] < uavs[i][1]:
                    nuevo_tiempo_aterrizaje = tiempos_aterrizaje_actual[orden[n + 1]] - t_espera[orden[n + 1]][i]
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
                    nuevo_costo = nuevo_tiempo_aterrizaje - uavs[i][1]
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
        if cambios == 0:
            boolean = False


    return costo_actual, tiempos_aterrizaje_actual, costo_orden