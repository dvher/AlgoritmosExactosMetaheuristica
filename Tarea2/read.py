from typing import List, Tuple
from Greedy import greedy_determinista
from Greedy import greedy_estocastico
from Hill_Climbing import hill_climbing
from Hill_Climbing import hill_climbing_mejor

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


archivo = 'C:/Users/Ketbome/Desktop/AlgoritmosExactosMetaheuristica/Tarea2/t2_Titan.txt'

num_uavs, uavs, t_espera = read_file(archivo)
costo_determinista, tiempos_aterrizaje_determinista, orden, orden_costos = greedy_determinista(
    num_uavs, uavs, t_espera)
print(f"Archivo: {archivo}")
print(f"Greedy Determinista - Costo Total: {costo_determinista}")
print(f"Greedy Determinista - Costo en la nave i: {orden_costos}")
print(f"Tiempos de aterrizaje de cada nave i: {tiempos_aterrizaje_determinista}")
print("Hill Climbing - Greedy determinista:")
costo_hill_climbing, tiempos_aterrizaje_hill_climbing, orden_costos_hill = hill_climbing(
    num_uavs, uavs, t_espera, costo_determinista, tiempos_aterrizaje_determinista, orden, orden_costos)
print(f"  Costo Total: {costo_hill_climbing}")
print(f"  Costo en la nave i: {orden_costos_hill}")
print(f"  Tiempos de aterrizaje de cada nave i: {tiempos_aterrizaje_hill_climbing}")
print("Hill Climbing Mejor Mejora- Greedy determinista:")
costo_hill_climbing, tiempos_aterrizaje_hill_climbing, orden_costos_hill_mejor = hill_climbing_mejor(
    num_uavs, uavs, t_espera, costo_determinista, tiempos_aterrizaje_determinista, orden, orden_costos)
print(f"  Costo Total: {costo_hill_climbing}")
print(f"  Costo en la nave i: {orden_costos_hill_mejor}")
print(f"  Tiempos de aterrizaje de cada nave i: {tiempos_aterrizaje_hill_climbing}")
print()
for seed in range(5):
    print(f"Greedy Estocástico seed {seed}:")
    costo_estocastico, tiempos_aterrizaje_estocastico, orden, orden_costos = greedy_estocastico(
        num_uavs, uavs, t_espera, seed)
    print(f"  Seed {seed} - Costo Total: {costo_estocastico}")
    print(f"  Costo en la nave i: {orden_costos}")
    print(f"  Tiempos de aterrizaje de cada nave i: {tiempos_aterrizaje_estocastico}")
    print(f"  Hill Climbing - Greedy estocastico:")
    costo_hill_climbing, tiempos_aterrizaje_hill_climbing, orden_costos_hill = hill_climbing(
        num_uavs, uavs, t_espera, costo_estocastico, tiempos_aterrizaje_estocastico, orden, orden_costos)
    print(f"     Seed {seed} - Costo Total: {costo_hill_climbing}")
    print(f"     Costo en la nave i: {orden_costos_hill}")
    print(f"     Tiempos de aterrizaje de cada nave i: {tiempos_aterrizaje_hill_climbing}")
    print(f"  Hill Climbing Mejor Mejora- Greedy estocastico:")
    costo_hill_climbing_mejor, tiempos_aterrizaje_hill_climbing_mejor, orden_costos_hill_mejor = hill_climbing_mejor(
        num_uavs, uavs, t_espera, costo_estocastico, tiempos_aterrizaje_estocastico, orden, orden_costos)
    print(f"     Seed {seed} - Costo Total: {costo_hill_climbing}")
    print(f"     Costo en la nave i: {orden_costos_hill}")
    print(f"     Tiempos de aterrizaje de cada nave i: {tiempos_aterrizaje_hill_climbing}")
    print()
print()
