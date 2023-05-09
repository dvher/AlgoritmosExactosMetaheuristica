from typing import List, Tuple
import random

def read_file(file_name: str) -> Tuple[List[int], List[List[int]]]:
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


def greedy_determinista(num_uavs, uavs, t_espera):
    ord_actual = 0 # En que valor del orden va
    orden = sorted(range(num_uavs), key=lambda i: uavs[i][1])  # Ordena los UAV por tiempo preferente
    print(orden)
    tiempos_aterrizaje = [0] * num_uavs # Hace un arreglo de 0ros de tamaño num_uavs
    costo = 0

    for i in orden:
        tiempo_aterrizaje = max(uavs[i][0], tiempos_aterrizaje[orden[ord_actual - 1]] + t_espera[orden[ord_actual - 1]][i] if i > 0 else 0)
        tiempos_aterrizaje[i] = tiempo_aterrizaje
        if tiempo_aterrizaje < uavs[i][1]:
            costo += (uavs[i][1] - tiempo_aterrizaje) * 2  # Costo adicional por estar por debajo del tiempo preferente
        elif tiempo_aterrizaje > uavs[i][2]:
            costo += (tiempo_aterrizaje - uavs[i][2]) * 100 # Muy costoso solucion pasa a ser infactible
        else:
            costo += abs(tiempo_aterrizaje - uavs[i][1])
        ord_actual += 1


    return costo, tiempos_aterrizaje

def greedy_estocastico(num_uavs, uavs, t_espera, seed):
    ord_actual = 0 # En que valor del orden va
    random.seed(seed)
    orden = sorted(range(num_uavs), key=lambda i: uavs[i][1])  # Ordena los UAV por tiempo preferente
    tiempos_aterrizaje = [0] * num_uavs # Hace un arreglo de 0ros de tamaño num_uavs
    costo = 0

    for i in orden:
        t_sig_aterrizaje = max(uavs[i][0], tiempos_aterrizaje[orden[ord_actual - 1]] + t_espera[orden[ord_actual - 1]][i] if i > 0 else 0)
        rango_tiempo = list(range(t_sig_aterrizaje, t_sig_aterrizaje + 50)) # Aca para hacerlo estocastico que elija entre un rango de tiempos desde el que puede aterrizar
        tiempo_aterrizaje = random.choice(rango_tiempo)
        tiempos_aterrizaje[i] = tiempo_aterrizaje
        if tiempo_aterrizaje < uavs[i][1]:
            costo += (uavs[i][1] - tiempo_aterrizaje) * 2  # Costo adicional por estar por debajo del tiempo preferente
        elif tiempo_aterrizaje > uavs[i][2]:
            costo += (tiempo_aterrizaje - uavs[i][2]) * 100 # Muy costoso solucion pasa a ser infactible
        else:
            costo += abs(tiempo_aterrizaje - uavs[i][1])
        ord_actual += 1


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
