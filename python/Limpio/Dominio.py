import copy


def Inconsistencias(matriz, dominio, pos, rows, cols):
    # pintar.remove(pos)
    col, row = pos[0], pos[1]
    num_secuencia_x = rows[row].split(",")
    num_secuencia_y = cols[col].split(",")
    if num_secuencia_x[0] == 'resolve' or num_secuencia_y[0] == 'resolve':
        return matriz, dominio, rows, cols, True
    bool = True
    suma = 0
    first = matriz[row].index(1)
    for i in num_secuencia_x:
        suma += int(i)
        suma += 1
    suma -= 1
    if suma > len(matriz) - first:
        return matriz, dominio, rows, cols, True
    # Evaluar eje rows restricciones
    i = col
    # Se ve empieza desde el primer pintado de la fila
    count = 0
    secuencia = 0
    while bool:
        if i-1 >= 0 and matriz[row][i-1] == 1:
            i -= 1
        else:
            bool = False
    col = i
    espacios = i + int(num_secuencia_x[0])
    if espacios > len(matriz):
        return matriz, dominio, rows, cols, True

    while i < col + int(num_secuencia_x[0]):
        if matriz[row][i] == 1:
            secuencia += 1
        i += 1

    # Se remueve el espacio si existe en el dominio
    if [espacios, row] in dominio:
        dominio.remove([espacios, row])
    espacios += 1
    if len(num_secuencia_x) == 1:
        while espacios < len(matriz):
            if [espacios, row] in dominio:
                dominio.remove([espacios, row])
            espacios += 1

    if secuencia == int(num_secuencia_x[0]):
        if num_secuencia_x[0] in rows[row]:
            if len(num_secuencia_x) > 1:
                nueva_lista = num_secuencia_x[1:]
                rows[row] = ",".join(nueva_lista)
            else:
                rows[row] = "resolve"
                j = 0
                while j < len(matriz):
                    if [j, row] in dominio:
                        dominio.remove([j, row])
                    j += 1

    col, row = pos[0], pos[1]
    num_secuencia_x = rows[row].split(",")
    num_secuencia_y = cols[col].split(",")
    if num_secuencia_y[0] == 'resolve':
        return matriz, dominio, rows, cols, False

    bool = True
    # Evaluar eje cols restricciones
    i = row
    secuencia = 0
    while bool:
        if i-1 >= 0 and matriz[i-1][col] == 1:
            i -= 1
        else:
            bool = False
    row = i
    espacios = i + int(num_secuencia_y[0])
    if espacios > len(matriz):
        return matriz, dominio, rows, cols, True

    while i < row + int(num_secuencia_y[0]):
        if matriz[i][col] == 1:
            secuencia += 1
        i += 1
    # Se remueve el espacio si existe en el dominio
    if len(num_secuencia_y) == 1:
        while espacios < len(matriz):
            if [col, espacios] in dominio:
                dominio.remove([col, espacios])
            espacios += 1
    if espacios > len(matriz):
        return matriz, dominio, rows, cols, True
    if secuencia == int(num_secuencia_y[0]):
        if num_secuencia_y[0] in cols[col]:
            if len(num_secuencia_y) > 1:
                nueva_lista = num_secuencia_y[1:]
                cols[col] = ",".join(nueva_lista)
            else:
                cols[col] = "resolve"
                j = 0
                while j < len(matriz):
                    if [col, j] in dominio:
                        dominio.remove([col, j])
                    j += 1

    return matriz, dominio, rows, cols, False
