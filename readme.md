Archivos con los datos tipo:
  En el orden de:
    -Columnas
    -Filas
  Debe ser si o si matriz cuadrada.
  Cada columna y fila separada por espacios, y si hay mas valores con una ',' en la columna o fila:
    -Ejemplo de tarea:
      4 2 7 3,4 7,2 7,2 3,4 7 2 4
      4 8 10 1,1,2,1,1 1,1,2,1,1 1,6,1 6 2,2 4 2

Archivo no optimizado:
  1.- Limpio.py 
    -Se hace la lectura del archivo que contiene los valores de las columnas y se guardan en arreglos de filas y columnas.
    -Se hace una matriz de tamaño n de valores 0 que representa que no estan pintados
    -Se sacan las posiciones posibles a tomar como el dominio posible que guarda como coordenada [fila, columna]
    -Se crea un nodo por cada posicion posible posicion, hace un forward checking pasandole el nodo
    -Finalmente imprime las soluciones con su determinado tiempo de ejecución
  2.- forwardchecking.py
    -Se hace la clase nodo con sus variables y con sus posibles hijos para hacer el arbol
    Funcion forwardchecking:
      -Toma los valores del nodo en el que va
      -Antes que nada evalua si esta en una posición que no ha sido resuelta para continuar y si la anterior fila fue resuelta, dado que es consecutivo el proceso si la fila anterior no esta resuelta no encontrara nunca una solución, en el caso de no cumplir la condición corta la rama y va a la siguiente.
      -Si cumple con las condiciones agrega el valor en la posicion pintando con un valor 1 la matriz y por consiguiente ve las inconsistencias que puede causar dicho valor puesto llamando a una función
      -Ve si todas las filas y columnas están resueltas, en caso de estarlo es una solución y la guarda en una variable global que guarda las matrices con la solución y corta la rama.
      -En el caso contrario crea un nodo con los posibles valores de dominio creando mas ramas al nodo y haciendo una recursividad de forwardchecking
      -Si no encuentra solución poda el árbol completo
  3.- Dominio.py
    Función Inconsistencias:
      -Primero ve que el primer valor de la fila y haciendo una suma de los posibles valores para que no pase el maximo de la matriz en caso de pasar el maximo corta la rama dado que no habrá solución a futuro
      -Después hace un conteo de las secuencias y una comparación, en caso de que la secuencia sea mayor corta la rama dado que no habra solución a futuro
      -Bloquea-Borra valores del dominio en Filas y Columnas que no se pueden tomar a futuro 
      -Tambien ve si con el punto pintado queda resuelta una Columna o Fila para de esta forma marcarla como Resolve
Archivo optimizado - Cambios:
  1.- Recalculado.py
    -En este caso en vez de comenzar de forma secuencial, este lo hara desde la linea que tenga mayor valor, dado que esta tiende a ser la solución mas rapido, o al mismo tiempo dar la falla mas rápido en caso de no haber solución.
    -Se hace una variable global row_order que contiene la suma de los valores de las líneas siendo row_order[0] la suma de la fila 0 y así
    -Con lo anterior se sacan las posiciones con mayor suma en orden de posición en la variable row_pos la cual contiene las posiciones de las lineas por donde comenzar a pintar
    -Se saca la posición siguiente de la linea con next_pos y se crea un Nodo para comenzar con la travesía
  2.- forwardchecking.py
    -Los únicos cambios son que se usa una nueva función Pre_Inconsistencias que evalua de forma diferente las inconsitencias de forma no secuencial.
    -Ademas antes de crear una rama se consulta la siguiente posición con next pos.
  3.- Dominio.py
    Función Pre_Inconsistencias
      -Evalua las inconsistencias Futuras de la linea en que esta, y evalua las restricciones a futuro de las columnas
      -Comprueba si se resolvió la linea o columna y las marca como resolve
    Función Next_pos
      -Ve la siguiente posicion de la linea en que se esta actualmente, en caso de no haber blockea(row_block) y la elimina de row_pos la linea en que se esta y se ve la siguiente linea a evaluar
