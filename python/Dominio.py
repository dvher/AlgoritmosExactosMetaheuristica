def Pre_Inconsistencias(matriz, dominio, pos, rows, cols, row_pos, row_block):
    # pintar.remove(pos)
    col, row = pos[0], pos[1]
    num_secuencia_x = rows[row].split(",")
    num_secuencia_y = cols[col].split(",")
    suma = 0
    first = matriz[row].index(1)
    for i in num_secuencia_x:
        suma += int(i)
        suma += 1
    suma -= 1
    if suma > len(matriz) - first:
        return matriz, dominio, rows, cols, row_pos, row_block, True
    if num_secuencia_x[0] == 'resolve' or num_secuencia_y[0] == 'resolve':
        return matriz, dominio, rows, cols, row_pos, row_block, True
    bool = True
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
        return matriz, dominio, rows, cols, row_pos, row_block, True

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
                row_pos.remove(row)
                row_block.append(row)
                j = 0
                while j < len(matriz):
                    if [j, row] in dominio:
                        dominio.remove([j, row])
                    j += 1

    col, row = pos[0], pos[1]
    num_secuencia_x = rows[row].split(",")
    num_secuencia_y = cols[col].split(",")
    if num_secuencia_y[0] == 'resolve':
        return matriz, dominio, rows, cols, row_pos, row_block, False
    count = 0
    for i in range(len(matriz)):
        if matriz[i][col] == 1:
            count += 1

    suma = 0
    for i in num_secuencia_y:
        suma += int(i)

    if count == suma:
        # Comprobar si cumple con la secuencia
        i = 0
        secuencia = 0
        while i < len(matriz):
            if matriz[i][col] == 1:
                secuencia += 1
            if secuencia == int(num_secuencia_y[0]):
                num_secuencia_y.remove(num_secuencia_y[0])
                secuencia = 0
                i += 1
            if len(num_secuencia_y) == 0:
                cols[col] = 'resolve'
                return matriz, dominio, rows, cols, row_pos, row_block, False
            if i > 0 and matriz[i-1][col] == 1 and matriz[i][col] == 0:
                secuencia = 0
            i += 1
        if len(num_secuencia_y) != 0:
            return matriz, dominio, rows, cols, row_pos, row_block, True
    elif count > suma:
        return matriz, dominio, rows, cols, row_pos, row_block, True
    return matriz, dominio, rows, cols, row_pos, row_block, False


def Next_pos(dominio, row_pos, row_block, pos):
    for i, (x, y) in enumerate(dominio):
        if y == row_pos[0]:
            pos = dominio[i]
            dominio.remove(pos)
            return dominio, row_pos, row_block, pos
    else:
        row_block.append(row_pos[0])
        row_pos.remove(row_pos[0])
        return Next_pos(dominio, row_pos, row_block, pos)
