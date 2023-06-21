import pygame

# TODO: Hacer el tamaño de los cuadrados dinámicos
# TODO: Hacer un objeto que contenga el color según el valor de la matriz

# Valores posibles de la matriz, cualquier valor fuera de este se considerará un cuadrado vacío
MATRIX_EMPTY = 0
MATRIX_PLAYER = 1
MATRIX_WALL = 2
MATRIX_TRAIL = 3

COLOR_GRID = (255, 255, 255)  # White color for grid lines
COLOR_SQUARE = (0, 0, 255)  # Blue color for squares
COLOR_PLAYER = (255, 0, 0)  # Red color for player
COLOR_TRAIL = (0, 255, 0)   # Green color for trail

def graph_path(matrix):
    # Define el tamaño de cada cuadrado
    square_size = 50
    margin = 5

    # Calcular el alto y ancho para la pantalla
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    grid_width = num_cols * (square_size + margin) + margin
    grid_height = num_rows * (square_size + margin) + margin

    pygame.init()

    window = pygame.display.set_mode((grid_width, grid_height))
    pygame.display.set_caption("Ruta más corta")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Llenar la pantalla negra
        window.fill((0, 0, 0))

        # Dibujar el grid
        for row in range(num_rows):
            for col in range(num_cols):
                x = col * (square_size + margin) + margin
                y = row * (square_size + margin) + margin

                # Cambia el color del cuadrado según el valor de la matriz
                if matrix[row][col] == MATRIX_WALL:
                    color = COLOR_GRID
                elif matrix[row][col] == MATRIX_PLAYER:
                    color = COLOR_PLAYER
                elif matrix[row][col] == MATRIX_TRAIL:
                    color = COLOR_TRAIL
                else:
                    color = COLOR_SQUARE

                # Dibujar el cuadrado que corresponda
                pygame.draw.rect(window, color, (x, y, square_size, square_size))

        # Actualizar la imagen
        pygame.display.flip()

    # Salir
    pygame.quit()
