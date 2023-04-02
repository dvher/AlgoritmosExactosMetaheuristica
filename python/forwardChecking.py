from Dominio import eliminar_inconsistencia
from Dominio import Inconsistencias
import copy
import sys


class Nodo:
    def __init__(self, matriz, dominio, rows, cols):
        self.matriz = matriz
        self.dominio = dominio
        self.rows = rows
        self.cols = cols
        self.hijos = []

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)


def forward_checking(nodo):
    rows = nodo.rows.copy()
    cols = nodo.cols.copy()
    brek = False
    if len(nodo.dominio) == 0:
        return False
    # Tomar la primera dominio no asignada restante
    dominio = nodo.dominio.copy()
    pos = dominio[0]
    if rows[pos[1]] != 'resolve' or cols[pos[0]] != 'resolve':
        # Asignar el pos a la dominio
        matriz = nodo.matriz.copy()
        # Realizar propagación de restricciones
        dominio.remove(pos)
        matriz[pos[1]][pos[0]] = 1
        # matriz, dominio, A, B, brek = eliminar_inconsistencia(matriz, dominio, pos, X, Y)
        matriz,  dominio, rows, cols, brek = Inconsistencias(
            matriz, dominio, pos, rows, cols)
        for linea in matriz:
            print(linea)
        print("------------------------------")
    else:
        brek = True
    # Si no hay poses posibles para alguna dominio, podar el árbol
    if brek:
        return False
    # Si no hay dominios restantes, se llegó a una solución
    if all(a == "resolve" for a in cols) and all(b == "resolve" for b in rows):
        print("RESUELTOOOOOOOOOOOOOOOOOOOOOOOO")
        sys.exit()
        return True

    for i in range(len(dominio)):
        Hijo = Nodo(copy.deepcopy(matriz), dominio, rows, cols)
        nodo.agregar_hijo(Hijo)
        # Llamada recursiva al algoritmo con el nuevo nodo hijo
        if forward_checking(Hijo):
            return True
        dominio.remove(dominio[0])

    # Si no se encontró una solución, podar el árbol
    return False
