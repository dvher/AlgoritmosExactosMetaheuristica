import copy
from Dominio import analisis_dominio
from forwardChecking import Nodo
from forwardChecking import forward_checking
from Dominio import arreglo_resolve

# Crear matriz cols variables a utilizar
matriz = []
posiciones = []
dom = []
rows = []
cols = []

# Leer archivo
with open('/home/ketbome/AlgoritmosExactosMetaheuristica/python/puzzle.txt', 'r') as archivo:
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

print(rows)
print(cols)

# Copiar la matriz para sacar su dominio
dom = copy.deepcopy(matriz)

# Para la siguiente reduccion solo se veran los casos donde solo hacols una posibilidad de valores
# Reduccion de dominio en filas
aux = []
row = 0
for num in rows:
    aux = num.split(',')
    suma = 0
    for cons in aux:
        suma = suma + int(cons) + 1
    suma = suma - 1
    if suma == 10:
        rows[row] = "resolve"
        col = 0
        for cons in aux:
            # print(suma, " ", cons, " ", row, " ", col)
            for i in range(int(cons)):
                # print(row, " ", col)
                matriz[row][col] = 1
                dom[row][col] = 1
                col = col + 1
            if col < 10:
                dom[row][col] = 1
            col = col + 1
    row = row + 1

# Reduccion de dominio por columnas
aux = []
row = 0
for num in cols:
    aux = num.split(',')
    suma = 0
    for cons in aux:
        suma = suma + int(cons) + 1
    suma = suma - 1
    if suma == 10:
        cols[row] = "resolve"
        col = 0
        for cons in aux:
            # print(suma, " ", cons, " ", row, " ", col)
            for i in range(int(cons)):
                # print(row, " ", col)
                matriz[col][row] = 1
                dom[col][row] = 1
                col = col + 1
            if col < 10:
                dom[col][row] = 1
            col = col + 1
    row = row + 1

print("------------------------------")
for fila in matriz:
    print(fila)

print("------------------------------")
dom = analisis_dominio(matriz, dom, rows, cols)

for fila in dom:
    print(fila)
print("------------------------------")

for i in range(len(dom)):
    for j in range(len(dom[i])):
        if dom[i][j] == 0:
            posiciones.append([j, i])  # agregar la posición a 'posiciones'

print(posiciones)  # mostrar las posiciones encontradas
print("------------------------------")
rows, cols = arreglo_resolve(posiciones, rows, cols)


for i in range(len(posiciones)):
    nodo_raiz = Nodo(copy.deepcopy(matriz), posiciones, rows, cols)
    forward_checking(nodo_raiz)
    posiciones.remove(posiciones[0])
