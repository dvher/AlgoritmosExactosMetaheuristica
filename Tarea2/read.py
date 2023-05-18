from typing import List, Tuple
from Greedy import greedy_determinista
from Greedy import greedy_estocastico
from Hill_Climbing import hill_climbing
from Hill_Climbing import hill_climbing_mejor
from Tabu_Search import tabu_search
import argparse

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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="The file to use the algorithms from")
    args = parser.parse_args()

    archivo = args.file

    num_uavs, uavs, t_espera = read_file(archivo)

    while True:    
        print("Seleccione la información que desea ver:")
        print("1. Solo los Costos")
        print("2. Costo en la nave i")
        print("3. Tiempos de aterrizaje de cada nave i")
        print("4. Todos")
        print("0. Salir")
        
        opcion = int(input("Ingrese el número de opción: "))
        
        if opcion == 0:
            break

        costo_determinista, tiempos_aterrizaje_determinista, orden, orden_costos, fact = greedy_determinista(
            num_uavs, uavs, t_espera)
        
        print(f"Archivo: {archivo}")

        print(f"Greedy Determinista - Costo Total: {costo_determinista} {fact}")
        if opcion == 2 or opcion == 4:
            print(f"Greedy Determinista - Costo en la nave i: {orden_costos}")
        if opcion == 3 or opcion == 4:
            print(f"Tiempos de aterrizaje de cada nave i: {tiempos_aterrizaje_determinista}")

        best_cost = costo_determinista
        best_cost_name = f"Greedy Determinista {fact}"
        
        print("Hill Climbing - Greedy determinista:")
        costo_hill_climbing, tiempos_aterrizaje_hill_climbing, orden_costos_hill, fact = hill_climbing(
            num_uavs, uavs, t_espera, costo_determinista, tiempos_aterrizaje_determinista, orden, orden_costos)
        
        print(f"  Costo Total: {costo_hill_climbing} {fact}")
        if opcion == 2 or opcion == 4:
            print(f"  Costo en la nave i: {orden_costos_hill}")
        if opcion == 3 or opcion == 4:
            print(f"  Tiempos de aterrizaje de cada nave i: {tiempos_aterrizaje_hill_climbing}")
        if costo_hill_climbing < best_cost:
            best_cost = costo_hill_climbing
            best_cost_name = f"Hill climbing Alguna Mejora en Determinista {fact}"
        
        print("Hill Climbing Mejor Mejora - Greedy determinista:")
        costo_hill_climbing, tiempos_aterrizaje_hill_climbing, orden_costos_hill_mejor, fact= hill_climbing_mejor(
            num_uavs, uavs, t_espera, costo_determinista, tiempos_aterrizaje_determinista, orden, orden_costos)
        
        print(f"  Costo Total: {costo_hill_climbing} {fact}")
        if opcion == 2 or opcion == 4:
            print(f"  Costo en la nave i: {orden_costos_hill_mejor}")
        if opcion == 3 or opcion == 4:
            print(f"  Tiempos de aterrizaje de cada nave i: {tiempos_aterrizaje_hill_climbing}")
        if costo_hill_climbing < best_cost:
            best_cost = costo_hill_climbing
            best_cost_name = f"Hill climbing Mejor Mejora en Determinista {fact}"

        print("Tabu Search - Greedy determinista:")
        costo_tabu_search, tiempos_aterrizaje_tabu_search, orden_tabu_search, fact= tabu_search(
            num_uavs, uavs, t_espera, costo_determinista, tiempos_aterrizaje_determinista, orden, orden_costos)
        print(f"  Costo Total: {costo_tabu_search} {fact}")
        if opcion == 2 or opcion == 4:
            print(f"  Costo en la nave i: {orden_tabu_search}")
        if opcion == 3 or opcion == 4:
            print(f"  Tiempos de aterrizaje de cada nave i: {tiempos_aterrizaje_tabu_search}")
        if costo_tabu_search < best_cost:
            best_cost = costo_tabu_search
            best_cost_name = f"Tabu Search en Determinista"
        
        print()
        for seed in range(5):
            print(f"Greedy Estocástico seed {seed}:")
            costo_estocastico, tiempos_aterrizaje_estocastico, orden, orden_costos, fact = greedy_estocastico(
                num_uavs, uavs, t_espera, seed)
            
            print(f"  Seed {seed} - Costo Total: {costo_estocastico} {fact}")
            if opcion == 2 or opcion == 4:
                print(f"  Seed {seed} - Costo en la nave i: {orden_costos}")
            if opcion == 3 or opcion == 4:
                print(f"  Seed {seed} - Tiempos de aterrizaje de cada nave i: {tiempos_aterrizaje_estocastico}")
            if costo_estocastico < best_cost:
                best_cost = costo_estocastico
                best_cost_name = f"Greedy Estocástico Seed {seed} {fact}"
            
            print(f"  Hill Climbing - Greedy estocastico:")
            costo_hill_climbing, tiempos_aterrizaje_hill_climbing, orden_costos_hill, fact = hill_climbing(
                num_uavs, uavs, t_espera, costo_estocastico, tiempos_aterrizaje_estocastico, orden, orden_costos)
            
            print(f"     Seed {seed} - Costo Total: {costo_hill_climbing} {fact}")
            if opcion == 2 or opcion == 4:
                print(f"     Seed {seed} - Costo en la nave i: {orden_costos_hill}")
            if opcion == 3 or opcion == 4:
                print(f"     Seed {seed} - Tiempos de aterrizaje de cada nave i: {tiempos_aterrizaje_hill_climbing}")
            if costo_hill_climbing < best_cost:
                best_cost = costo_hill_climbing
                best_cost_name = f"Hill Climbing Alguna Mejora en Estocástico Seed {seed} {fact}"
            
            print(f"  Hill Climbing Mejor Mejora - Greedy estocastico:")
            costo_hill_climbing_mejor, tiempos_aterrizaje_hill_climbing_mejor, orden_costos_hill_mejor, fact = hill_climbing_mejor(
                num_uavs, uavs, t_espera, costo_estocastico, tiempos_aterrizaje_estocastico, orden, orden_costos)
            
            if opcion == 1:
                print(f"     Seed {seed} - Costo Total: {costo_hill_climbing_mejor} {fact}")
            if opcion == 2 or opcion == 4:
                print(f"     Seed {seed} - Costo en la nave i: {orden_costos_hill_mejor}")
            if opcion == 3 or opcion == 4:
                print(f"     Seed {seed} - Tiempos de aterrizaje de cada nave i: {tiempos_aterrizaje_hill_climbing_mejor}")
            if costo_hill_climbing_mejor < best_cost:
                best_cost = costo_hill_climbing_mejor
                best_cost_name = f"Hill Climbing Mejor Mejora en Estocástico Seed {seed} {fact}"
            
            print("  Tabu Search - Greedy estocastico:")
            costo_tabu_search, tiempos_aterrizaje_tabu_search, orden_tabu_search, fact= tabu_search(
                num_uavs, uavs, t_espera, costo_determinista, tiempos_aterrizaje_determinista, orden, orden_costos)
            print(f"     Seed {seed} - Costo Total: {costo_tabu_search} {fact}")
            if opcion == 2 or opcion == 4:
                print(f"     Seed {seed} - Costo en la nave i: {orden_tabu_search}")
            if opcion == 3 or opcion == 4:
                print(f"     Seed {seed} - Tiempos de aterrizaje de cada nave i: {tiempos_aterrizaje_tabu_search}")
            if costo_tabu_search < best_cost:
                best_cost = costo_tabu_search
                best_cost_name = f"Tabu Search en Estocastico Seed {seed}"
            
            print()
        print(best_cost_name)
        print(f"Mejor costo obtenido: {best_cost}")
        print()

if __name__ == '__main__':
    main()
