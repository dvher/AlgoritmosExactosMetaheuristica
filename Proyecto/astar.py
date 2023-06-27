from constants import MATRIX_WALL

from queue import PriorityQueue

from typing import List, Tuple

movimientos = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]

def is_valid(matrix, pos):
    rows = len(matrix)
    cols = len(matrix[0]) if rows else 0
    return 0 <= pos[0] < rows and 0 <= pos[1] < cols and matrix[pos[0]][pos[1]] != MATRIX_WALL

def get_neighbours(matrix, pos):
    return [p for p in [(pos[0] + move[0], pos[1] + move[1]) for move in movimientos] if is_valid(matrix, p)]

def manhattan_distance(start, end):
    dx = abs(start[0] - end[0])
    dy = abs(start[1] - end[1])
    return max(dx, dy)

def astar(matrix: List[List[int]], start: Tuple[int, int], end: Tuple[int, int]) -> List[Tuple[int, int]]:

    heuristic = lambda pos: manhattan_distance(pos, end)

    visited = set()
    parent = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start)}
    paths = {start: [start]}

    queue = PriorityQueue()
    queue.put((f_score[start], start))

    while not queue.empty():

        current = queue.get()[1]

        if current == end:
            path = []
            for x in paths:
                if x == end:
                    continue
                for y in paths[x]:
                    if y not in path:
                        path.append(y)

            path.append(end)
            return path, len(path)
        
        visited.add(current)

        for neighbour in get_neighbours(matrix, current):
            if neighbour in visited:
                continue

            tentative_g_score = g_score[current] + manhattan_distance(current, neighbour)

            if neighbour not in g_score or tentative_g_score < g_score[neighbour]:
                parent[neighbour] = current
                g_score[neighbour] = tentative_g_score
                f_score[neighbour] = tentative_g_score + heuristic(neighbour)
                paths[neighbour] = paths[current] + [neighbour]
                queue.put((f_score[neighbour], neighbour))

    return [], 0