from graphics import graph_path
from astar import astar
from constants import MATRIX_START, MATRIX_END
import argparse
from time import perf_counter_ns

argparser = argparse.ArgumentParser()
argparser.add_argument("-f", "--file", help="Archivo de entrada", required=True)

args = argparser.parse_args()

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


def main():

    filename = args.file

    matrix, start, end = get_matrix(filename)

    astar_start = perf_counter_ns()
    # Buscar el camino más corto
    path = astar(matrix, start, end)
    astar_end = perf_counter_ns()

    # Marcar el camino en la matriz
    graph_path(matrix, path, caption=f"Ruta: {filename} A*", path_speed=50)

    print(f"Tiempo de ejecución A*: {astar_end - astar_start} ns")

if __name__ == "__main__":
    main()
