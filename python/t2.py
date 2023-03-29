import copy


class Nodo:
    def __init__(self, matriz, dominio, X, Y, size):
        self.matriz = matriz
        self.dominio = dominio
        self.X = X
        self.Y = Y
        self.size = size
        self.hijos = []

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)


def forward_checking(nodo):
    # Si no hay variables restantes, se llegó a una solución
    if len(nodo.dominio) == 0:
        return True

    # Tomar la primera variable no asignada restante
    variable = nodo.dominio[0]

    for valor in variable.posibles_valores:
        # Asignar el valor a la variable
        asignaciones = nodo.asignaciones.copy()
        asignaciones[variable.nombre] = valor

        # Realizar propagación de restricciones
        dominio = nodo.dominio.copy()
        dominio.remove(variable)
        for var in dominio:
            var.eliminar_valor_inconsistente(asignaciones)

        # Si no hay valores posibles para alguna variable, podar el árbol
        if any(len(var.posibles_valores) == 0 for var in dominio):
            continue

        # Crear un nuevo nodo hijo con las asignaciones y variables restantes actualizadas
        hijo = Nodo(asignaciones, dominio)

        # Agregar el nodo hijo al nodo actual
        nodo.agregar_hijo(hijo)

        # Llamada recursiva al algoritmo con el nuevo nodo hijo
        if forward_checking(hijo):
            return True

    # Si no se encontró una solución, podar el árbol
    return False


# Crear matriz y variables a utilizar
matriz = []
posiciones = []
dom = []
X = []
Y = []

# Leer archivo
with open('/home/ketbome/AlgoritmosExactosMetaheuristica/python/puzzle.txt', 'r') as archivo:
    linea = archivo.readline()
    boolean = True
    while linea != '':
        linea = linea.replace('\n', '')  # Eliminar salto de linea
        if boolean:
            X = linea.split(' ')
        else:
            Y = linea.split(' ')
        linea = archivo.readline()
        boolean = False

# Largo de linea y columnas
rows = len(X)
cols = len(Y)
# Inicializar elementos de matriz en 0
for i in range(rows):
    fila = []
    for j in range(cols):
        fila.append(0)
    matriz.append(fila)

# Imprimir matriz inicial
# for fila in matriz:
#    print(fila)

print(X)
print(Y)

# Copiar la matriz para sacar su dominio
dom = copy.deepcopy(matriz)

# Para la siguiente reduccion solo se veran los casos donde solo hay una posibilidad de valores
# Reduccion de dominio en filas
aux = []
row = 0
for num in Y:
    aux = num.split(',')
    suma = 0
    for cons in aux:
        suma = suma + int(cons) + 1
    suma = suma - 1
    if suma == 10:
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
for num in X:
    aux = num.split(',')
    suma = 0
    for cons in aux:
        suma = suma + int(cons) + 1
    suma = suma - 1
    if suma == 10:
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

for i in range(len(dom)):
    for j in range(len(dom[i])):
        if matriz[i][j] == 0:
            posiciones.append([i, j])  # agregar la posición a 'posiciones'

print(posiciones)  # mostrar las posiciones encontradas

print("------------------------------")
for fila in matriz:
    print(fila)

print("------------------------------")
for fila in dom:
    print(fila)
print("------------------------------")
print(posiciones)
print("------------------------------")


nodo_raiz = Nodo(matriz, posiciones, X, Y, len(Y))
