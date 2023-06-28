from typing import List, Tuple
from random import random
from constants import MATRIX_WALL


class Ant:
    def __init__(self, start: Tuple[int, int]):
        self.path = [start]
        self.visited = set([start])
        self.total_distance = 0
        self.available_moves = []

    def move_to(self, position: Tuple[int, int], distance: int):
        self.path.append(position)
        self.visited.add(position)
        self.total_distance += distance

    def update_available_moves(self, matrix: List[List[int]]):
        current = self.path[-1]
        neighbours = get_neighbours(matrix, current)
        self.available_moves = []

        for neighbour in neighbours:
            if neighbour not in self.visited:
                self.available_moves.append(neighbour)

    def backtrack(self):
        if len(self.path) >= 2:
            self.total_distance -= calculate_distance(self.path[-1], self.path[-2])
        self.path.pop()





def calculate_distance(start: Tuple[int, int], end: Tuple[int, int]) -> int:
    dx = abs(start[0] - end[0])
    dy = abs(start[1] - end[1])
    return max(dx, dy)


def get_neighbours(matrix: List[List[int]], pos: Tuple[int, int]) -> List[Tuple[int, int]]:
    rows = len(matrix)
    cols = len(matrix[0]) if rows else 0
    neighbours = [(pos[0] + dx, pos[1] + dy) for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]]
    return [(nx, ny) for nx, ny in neighbours if 0 <= nx < rows and 0 <= ny < cols and matrix[nx][ny] != MATRIX_WALL]



def aco(matrix: List[List[int]], start: Tuple[int, int], end: Tuple[int, int], num_ants: int, evaporation: float,
        alpha: float, beta: float, iterations: int) -> List[Tuple[int, int]]:
    num_rows = len(matrix)
    num_cols = len(matrix[0]) if num_rows else 0

    pheromone_matrix = [[1.0] * num_cols for _ in range(num_rows)]

    best_path = []
    best_distance = float('inf')

    for _ in range(iterations):
        ants = [Ant(start) for _ in range(num_ants)]

        for ant in ants:
            while ant.path[-1] != end:
                ant.update_available_moves(matrix)
                current = ant.path[-1]

                if not ant.available_moves:
                    ant.backtrack()
                else:
                    probabilities = []
                    total = 0.0

                    for neighbour in ant.available_moves:
                        distance = calculate_distance(current, neighbour)
                        pheromone = pheromone_matrix[neighbour[0]][neighbour[1]] ** alpha
                        attractiveness = (1.0 / distance) ** beta
                        total += pheromone * attractiveness
                        probabilities.append((neighbour, pheromone * attractiveness))

                    probabilities = [(neighbour, prob / total) for neighbour, prob in probabilities]

                    selected = None

                    while not selected:
                        rand = random()
                        cumulative_prob = 0.0

                        for neighbour, prob in probabilities:
                            cumulative_prob += prob
                            if cumulative_prob >= rand:
                                selected = neighbour
                                break

                    ant.move_to(selected, calculate_distance(current, selected))
                    ant.update_available_moves(matrix)

            if ant.total_distance < best_distance:
                best_path = ant.path
                best_distance = ant.total_distance

        for i in range(num_rows):
            for j in range(num_cols):
                pheromone_matrix[i][j] *= evaporation

        for i in range(len(best_path) - 1):
            current = best_path[i]
            next_pos = best_path[i + 1]
            pheromone_matrix[next_pos[0]][next_pos[1]] += (1.0 / best_distance)

    return best_path, best_distance
