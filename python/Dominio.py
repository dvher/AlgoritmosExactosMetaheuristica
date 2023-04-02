def analisis_dominio(matriz, dom, X, Y):
    # Analisis por linea
    for i in range(len(matriz)):
        count = 0
        secuen = 0
        boolean = True
        aux = 0
        suma = 0
        num = X[i].split(",")
        for x in num:
            if x != "resolve":
                suma = suma + int(x) + 1
            else:
                suma = 11
        suma = suma - 1
        for j in range(len(matriz[i])):
            # contador de secuencia
            if matriz[i][j] == 1:
                if boolean:
                    aux = j + suma
                    while aux < len(matriz):
                        dom[i][aux] = 1
                        aux = aux + 1
                    boolean = False
                count = count + 1
                # cuantas secuencia existSen
                if j < len(matriz[i])-1:
                    if matriz[i][j+1] == 0:
                        aux = j - suma
                        while aux >= 0:
                            dom[i][aux] = 1
                            aux = aux - 1
                        secuen = secuen + 1
                        count = 0
    for i in range(len(matriz)):
        count = 0
        secuen = 0
        boolean = True
        aux = 0
        suma = 0
        num = Y[i].split(",")
        for y in num:
            if y != "resolve":
                suma = suma + int(y) + 1
            else:
                suma = 11
        suma = suma - 1
        for j in range(len(matriz[i])):
            # contador de secuencia
            if matriz[j][i] == 1:
                if boolean:
                    aux = j + suma
                    while aux < len(matriz):
                        dom[aux][i] = 1
                        aux = aux + 1
                    boolean = False
                count = count + 1
                # cuantas secuencia existSen
                if j < len(matriz[i])-1:
                    if matriz[j+1][i] == 0:
                        aux = j - suma
                        while aux >= 0:
                            dom[aux][i] = 1
                            aux = aux - 1
                        secuen = secuen + 1
                        count = 0
    return dom


def arreglo_resolve(dominio, X, Y):
    valuesx = []
    i = 0
    while i < len(X):
        for coord in dominio:
            if coord[1] == i:
                valuesx.append(i)
        i += 1
    i = 0
    while i < len(X):
        if i not in valuesx:
            X[i] = "resolve"
        i += 1
    valuesy = []
    i = 0
    while i < len(Y):
        for coord in dominio:
            if coord[0] == i:
                valuesy.append(i)
        i += 1
    i = 0
    while i < len(Y):
        if i not in valuesy:
            Y[i] = "resolve"
        i += 1
    return X, Y


def Inconsistencias(matriz, dominio, pos, X, Y):
    # pintar.remove(pos)
    x, y = pos[0], pos[1]
    num_secuencia_x = X[y].split(",")
    num_secuencia_y = Y[x].split(",")
    if num_secuencia_x[0] == 'resolve' or num_secuencia_y[0] == 'resolve':
        return matriz, dominio, X, Y, True
    bool = True
    # Evaluar eje X restricciones
    i = x
    # Se ve empieza desde el primer pintado de la fila
    count = 0
    secuencia = 0
    while bool:
        if i-1 >= 0 and matriz[y][i-1] == 1:
            i -= 1
        else:
            bool = False
    x = i
    espacios = i + int(num_secuencia_x[0])
    if espacios > len(matriz):
        return matriz, dominio, X, Y, True

    while i < x + int(num_secuencia_x[0]):
        if matriz[y][i] == 1:
            secuencia += 1
        i += 1

    # Se remueve el espacio si existe en el dominio
    if [espacios, y] in dominio:
        dominio.remove([espacios, y])
    espacios += 1
    if len(num_secuencia_x) == 1:
        while espacios < len(matriz):
            if [espacios, y] in dominio:
                dominio.remove([espacios, y])
            espacios += 1

    if secuencia == int(num_secuencia_x[0]):
        if num_secuencia_x[0] in X[y]:
            if len(num_secuencia_x) > 1:
                nueva_lista = num_secuencia_x[1:]
                X[y] = ",".join(nueva_lista)
            else:
                X[y] = "resolve"
                j = 0
                while j < len(matriz):
                    if [j, y] in dominio:
                        dominio.remove([j, y])
                    j += 1

    x, y = pos[0], pos[1]
    num_secuencia_x = X[y].split(",")
    num_secuencia_y = Y[x].split(",")
    if num_secuencia_y[0] == 'resolve':
        return matriz, dominio, X, Y, False

    bool = True
    # Evaluar eje Y restricciones
    i = y
    secuencia = 0
    while bool:
        print(matriz[i-1][x])
        if i-1 >= 0 and matriz[i-1][x] == 1:
            i -= 1
        else:
            bool = False
    y = i
    espacios = i + int(num_secuencia_y[0])
    if espacios > len(matriz):
        return matriz, dominio, X, Y, True

    while i < y + int(num_secuencia_y[0]):
        if matriz[i][x] == 1:
            secuencia += 1
        i += 1
    # Se remueve el espacio si existe en el dominio
    if len(num_secuencia_y) == 1:
        while espacios < len(matriz):
            if [x, espacios] in dominio:
                dominio.remove([x, espacios])
            espacios += 1
    if espacios > len(matriz):
        return matriz, dominio, X, Y, True
    if secuencia == int(num_secuencia_y[0]):
        if num_secuencia_y[0] in Y[x]:
            if len(num_secuencia_y) > 1:
                nueva_lista = num_secuencia_y[1:]
                Y[x] = ",".join(nueva_lista)
            else:
                Y[x] = "resolve"
                j = 0
                while j < len(matriz):
                    if [x, j] in dominio:
                        dominio.remove([x, j])
                    j += 1

    return matriz, dominio, X, Y, False


# Funcion desechada
def eliminar_inconsistencia(matriz, dominio, pos, rows, cols):
    col = pos[0]
    row = pos[1]
    num_sec = 0
    brek = False
    secuencia_rows = rows[row].split(",")
    secuencia_cols = cols[col].split(",")
    if secuencia_rows[0] == 'resolve' or secuencia_cols[0] == 'resolve':
        return matriz, dominio, rows, cols, True
    # Evaluar columnas
    count = 0
    for i in range(len(matriz)):
        if matriz[row][i] == 1:
            count += 1
        if count == int(secuencia_rows[num_sec]):
            num_sec += 1
            count = 0
            if num_sec == len(secuencia_rows):
                rows[row] = "resolve"
                break
    count = 0
    num_sec = 0
    for i in range(len(matriz)):
        if matriz[i][col] == 1:
            count += 1
        if count == int(secuencia_cols[num_sec]):
            num_sec += 1
            count = 0
            if num_sec == len(secuencia_cols):
                cols[col] = "resolve"
                break

    return matriz, dominio, rows, cols, brek
