import copy
from forwardChecking import Nodo
from forwardChecking import forward_checking
from Dominio import Next_pos
from Globales import soluciones
from Globales import row_order
from Globales import time_start
from sys import argv
import time

# Crear matriz cols variables a utilizar
matriz = []
posiciones = []
rows = []
cols = []
pos = []
row_block = []

# Leer archivo
with open(argv[1], 'r') as archivo:
    linea = archivo.readline()
    boolean = True
    while linea != '':
        linea = linea.replace('\n', '')  # Eliminar salto de linea
        if boolean:
            cols = linea.split(' ')
        else:
            rows = linea.split(' ')
        linea = archivo.readline()
        boolean = False

# Inicializar elementos de matriz en 0
for i in range(len(rows)):
    fila = []
    for j in range(len(cols)):
        fila.append(0)
    matriz.append(fila)

# Imprimir matriz inicial
# for fila in matriz:
#    print(fila)

# print(rows)
# print(cols)

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] == 0:
            posiciones.append([j, i])  # agregar la posición a 'posiciones'

# print(posiciones)  # mostrar las posiciones encontradas
# print("------------------------------")

# print("------------------------------")
# for fila in matriz:
#    print(fila)

# print("------------------------------")


for i in range(len(matriz)):
    suma = 0
    numbers = rows[i].split(",")
    for j in numbers:
        suma += int(j) + 1
    row_order.append(suma - 1)
row_pos = []
i = len(matriz)
while i > 0:
    for j in range(len(rows)):
        if row_order[j] == i:
            row_pos.append(j)
    i -= 1

for i in range(len(matriz)):
    numbers = rows[i].split(",")
    numbers2 = cols[i].split(",")
    if int(numbers[0]) == 0:
        row_block.append(i)
        rows[i] = 'resolve'
        j = 0
        while j < len(matriz):
            if [j, i] in posiciones:
                posiciones.remove([j, i])
            j += 1
    if int(numbers2[0]) == 0:
        cols[i] = 'resolve'
        j = 0
        while j < len(matriz):
            if [i, j] in posiciones:
                posiciones.remove([i, j])
            j += 1

for i in range(len(posiciones)):
    posiciones, row_pos, row_block, pos = Next_pos(
        posiciones, row_pos, row_block, pos=0)
    nodo_raiz = Nodo(copy.deepcopy(matriz), posiciones,
                     rows, cols, row_pos, row_block, pos)
    forward_checking(nodo_raiz)

print("--------Soluciones--------")
for i in soluciones:
    for linea in i:
        print(linea)
    print("------------------------------")

time_end = time.time()
print("Termino de ejecucion: ", time_end - time_start, " segundos")
