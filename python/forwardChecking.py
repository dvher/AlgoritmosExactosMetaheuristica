from Globales import soluciones
from Globales import row_order
from Globales import time_start
from Dominio import Pre_Inconsistencias
from Dominio import Next_pos
import time
import copy
import sys


class Nodo:
    def __init__(self, matriz, dominio, rows, cols, row_pos, row_block, pos):
        self.matriz = matriz
        self.dominio = dominio
        self.rows = rows
        self.cols = cols
        self.row_pos = row_pos
        self.row_block = row_block
        self.pos = pos
        self.hijos = []

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)


def forward_checking(nodo):
    global soluciones
    rows = nodo.rows.copy()
    cols = nodo.cols.copy()
    row_pos = nodo.row_pos.copy()
    row_block = nodo.row_block.copy()
    pos = nodo.pos.copy()
    dominio = nodo.dominio.copy()
    brek = False
    if (all(rows[a] == "resolve" for a in row_block)) or (len(row_block) == 0):
        if rows[pos[1]] != 'resolve' or cols[pos[0]] != 'resolve':
            # Asignar el pos a la dominio
            matriz = nodo.matriz.copy()
            # Realizar propagación de restricciones
            matriz[pos[1]][pos[0]] = 1
            # matriz, dominio, A, B, brek = eliminar_inconsistencia(matriz, dominio, pos, X, Y)
            matriz,  dominio, rows, cols, row_pos, row_block, brek = Pre_Inconsistencias(
                matriz, dominio, pos, rows, cols, row_pos, row_block)
            # for linea in matriz:
            #    print(linea)
            # print("------------------------------")
        else:
            return False
        # Si no hay poses posibles para alguna dominio, podar el árbol
        if brek:
            return False
        # Si no hay dominios restantes, se llegó a una solución
        if all(a == "resolve" for a in cols) and all(b == "resolve" for b in rows):
            time_resuelto = time.time()
            print("Resuelto - Time = ", time_resuelto - time_start, " segundos")
            soluciones.append(matriz)
            return True

        if len(nodo.dominio) == 0:
            return False

        # breaker = len(dominio)
        for i in range(len(dominio)):
            dominio, row_pos, row_block, posi = Next_pos(
                dominio, row_pos, row_block, pos)
            # if pos[1] != posi[1]:
            #    breaker = len(dominio) - row_order[row_pos[0]] + 1
            Hijo = Nodo(copy.deepcopy(matriz), dominio,
                        rows, cols, row_pos, row_block, posi)
            nodo.agregar_hijo(Hijo)
            # Llamada recursiva al algoritmo con el nuevo nodo hijo
            if forward_checking(Hijo):
                return True
            # breaker -= 1
            # if breaker == 0:
            #    break

    # Si no se encontró una solución, podar el árbol
    return False
