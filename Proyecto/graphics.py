import pygame
from constants import MATRIX_WALL, MATRIX_START, MATRIX_END, SCREEN_SIZE
from typing import List, Tuple

COLOR_SQUARE = (255, 255, 255)
COLOR_WALL = (23, 23, 23)
COLOR_PLAYER = (19, 56, 190)
COLOR_TRAIL = (128, 128, 128)
COLOR_END = (178, 32, 32)

PATH_SPEED = 500

def graph_path(matrix: List[List[int]], path: List[Tuple[int, int]], window: pygame.Surface, path_speed: int = PATH_SPEED):

    finish = False

    # Define el tamaño de cada cuadrado
    square_size = SCREEN_SIZE[0] // len(matrix[0])
    margin = SCREEN_SIZE[0] // 100

    # Calcular el alto y ancho para la pantalla
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    player_pos = (0, 0)

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if finish:
            return

        # Llenar la pantalla negra
        window.fill((0, 0, 0))
        # Dibujar el grid
        for row in range(num_rows):
            for col in range(num_cols):
                x = col * (square_size + margin) + margin
                y = row * (square_size + margin) + margin

                # Cambia el color del cuadrado según el valor de la matriz
                if matrix[row][col] == MATRIX_WALL:
                    color = COLOR_WALL
                elif matrix[row][col] == MATRIX_START:
                    player_pos = (row, col)
                    color = COLOR_PLAYER
                elif matrix[row][col] == MATRIX_END:
                    color = COLOR_END
                else:
                    color = COLOR_SQUARE

                # Dibujar el cuadrado que corresponda
                pygame.draw.rect(window, color, (x, y, square_size, square_size))

        # Actualizar la imagen
        pygame.display.flip()

        for coord in path:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
            pygame.time.wait(path_speed)
            row1, col1 = player_pos
            x1 = col1 * (square_size + margin) + margin
            y1 = row1 * (square_size + margin) + margin
            
            row2, col2 = coord
            x2 = col2 * (square_size + margin) + margin
            y2 = row2 * (square_size + margin) + margin

            # Dibujar el cuadrado que corresponda
            pygame.draw.rect(window, COLOR_TRAIL, (x1, y1, square_size, square_size))
            pygame.draw.rect(window, COLOR_PLAYER, (x2, y2, square_size, square_size))

            player_pos = coord

            # Actualizar la imagen
            pygame.display.flip()
        else:
            finish = True

