from graphics import graph_path
from astar import astar
from aco import aco
from constants import MATRIX_START, MATRIX_END, SCREEN_SIZE
import argparse
from time import perf_counter
import pygame

argparser = argparse.ArgumentParser()
argparser.add_argument("-f", "--file", help="Archivo de entrada", required=True)

args = argparser.parse_args()

PATH_SPEED=50

def get_matrix(filename):
    with open(filename, 'r', encoding="utf-8") as f:
        lines = [line.strip() for line in f.readlines()]

    matrix =  [list(map(int, line.split())) for line in lines]

    start = (0, 0)
    end = (0, 0)

    # Buscar el nodo inicial y final
    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if col == MATRIX_START:
                start = (i, j)
            elif col == MATRIX_END:
                end = (i, j)

    if start == end == (0, 0):
        raise Exception("No se encontró el nodo inicial o final")

    return matrix, start, end

def run_astar(matrix, start, end, filename):

    start_time = perf_counter()
    # Buscar el camino más corto
    path, cost = astar(matrix, start, end)
    end_time = perf_counter()

    pygame.init()

    # Define el tamaño de cada cuadrado
    square_size = SCREEN_SIZE[0] // len(matrix[0])
    margin = SCREEN_SIZE[0] // 100

    # Calcular el alto y ancho para la pantalla
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    grid_width = num_cols * (square_size + margin) + margin
    grid_height = num_rows * (square_size + margin) + margin

    window = pygame.display.set_mode((grid_width, grid_height))
    pygame.display.set_caption(f"Ruta: {filename}")

    # Marcar el camino en la matriz
    graph_path(matrix, path, window, path_speed=PATH_SPEED)

    pygame.time.wait(3000)

    pygame.image.save(window, f'Aº_{filename[:-4]}.jpg')

    pygame.quit()

    return cost, end_time - start_time

def run_aco(matrix, start, end, filename):

    # Run ACO algorithm
    num_ants = 10
    evaporation = 1
    alpha = 0.7
    beta = 1.5
    iterations = 200
    start_time = perf_counter()
    path_aco, cost_aco = aco(matrix, start, end, num_ants, evaporation, alpha, beta, iterations)
    end_time = perf_counter()

    pygame.init()

    # Define el tamaño de cada cuadrado
    square_size = SCREEN_SIZE[0] // len(matrix[0])
    margin = SCREEN_SIZE[0] // 100

    # Calcular el alto y ancho para la pantalla
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    grid_width = num_cols * (square_size + margin) + margin
    grid_height = num_rows * (square_size + margin) + margin

    window = pygame.display.set_mode((grid_width, grid_height))
    pygame.display.set_caption(f"Ruta: {filename}")

    # Marcar el camino en la matriz
    graph_path(matrix, path_aco, window, path_speed=PATH_SPEED)

    pygame.time.wait(3000)

    pygame.image.save(window, f'ACO_{filename[:-4]}.jpg')
    pygame.quit()

    return cost_aco, end_time - start_time

def show_puzzle(matrix, filename):
    square_size = SCREEN_SIZE[0] // len(matrix[0])
    margin = SCREEN_SIZE[0] // 100

    num_rows = len(matrix)
    num_cols = len(matrix[0])
    grid_width = num_cols * (square_size + margin) + margin
    grid_height = num_rows * (square_size + margin) + margin
    pygame.init()
    window = pygame.display.set_mode((grid_width, grid_height))
    pygame.display.set_caption('Puzzle')

    graph_path(matrix, [], window, path_speed=PATH_SPEED)

    pygame.time.wait(3000)

    pygame.image.save(window, f'{filename[:-4]}.jpg')
    pygame.quit()

def main():

    filename = args.file

    matrix, start, end = get_matrix(filename)

    opcion = 0

    print("Seleccione el algoritmo a utilizar:")
    print("1. A*")
    print("2. ACO")
    print("3. Ambos")
    print("4. Ver puzzle")
    print("5. Salir")

    while opcion not in [1, 2, 3, 4, 5]:
        opcion = int(input("Opción: "))

    if opcion == 1:
        cost, time = run_astar(matrix, start, end, filename)
        print(f"Tiempo de ejecución A*: {time} s")
        print(f"Costo del camino: {cost}")
        return
    
    if opcion == 2:
        cost, time = run_aco(matrix, start, end, filename)
        print(f"Tiempo de ejecución ACO: {time} s")
        print(f"Costo del camino: {cost}")
        return

    if opcion == 4:
        show_puzzle(matrix, filename)
        return
    
    if opcion == 5:
        return

    astar_start = perf_counter()
    # Buscar el camino más corto
    path, cost = astar(matrix, start, end)
    astar_end = perf_counter()

    # Run ACO algorithm
    num_ants = 2
    evaporation = 1
    alpha = 0.7
    beta = 1.5
    iterations = 2
    aco_start = perf_counter()
    path_aco, cost_aco = aco(matrix, start, end, num_ants, evaporation, alpha, beta, iterations)
    aco_end = perf_counter()

    print(f"Tiempo de ejecución ACO: {aco_end - aco_start} s")
    print(f"Costo del camino: {cost_aco}")

    print(f"Tiempo de ejecución A*: {astar_end - astar_start} s")
    print(f"Costo del camino: {cost}")

    pygame.init()

    # Define el tamaño de cada cuadrado
    square_size = SCREEN_SIZE[0] // len(matrix[0])
    margin = SCREEN_SIZE[0] // 100

    # Calcular el alto y ancho para la pantalla
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    grid_width = num_cols * (square_size + margin) + margin
    grid_height = num_rows * (square_size + margin) + margin

    window = pygame.display.set_mode((grid_width, grid_height))
    pygame.display.set_caption(f"Ruta: {filename} ACO vs A*")

    # Marcar el camino en la matriz
    graph_path(matrix, path_aco, window, path_speed=PATH_SPEED)

    pygame.time.wait(1000)

    graph_path(matrix, path, window, path_speed=PATH_SPEED)

    pygame.time.wait(3000)

    pygame.quit()

if __name__ == "__main__":
    main()
