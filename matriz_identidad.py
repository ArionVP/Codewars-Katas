# Dada una lista de lista representando una matriz n*n:
# Define una rutina que devuelve True si la entrada es una matriz indentidad
# y False en otro caso.

# Una matriz identidad es una matriz cuadrada en la que todos los elementos
# en la diagonal principal son 1 y el resto de elementos fuera de la
# diagonal principal son 0. 
# (Una matriz cuadrada es una matriz con el numero de filas
# igual al numero de columnas)

def esMatrizCuadrada(matrix):   
        for fila in matrix:
            if len(fila) != len(matrix):
              return False
        return True
       
# Casos test:


matrix =  [[1,0,1],
           [0,1,0],
           [0,1,0]]

assert esMatrizCuadrada(matrix) is True

matrix1 = [[1,0,0,0],
           [0,1,0,0],
           [0,0,1,0],
           [0,0,0,1]]

assert esMatrizCuadrada(matrix1) is True

matrix2 = [[1,0,0],
           [0,1,0],
          [0,0,0]]

assert esMatrizCuadrada(matrix2) is True

matrix5 = [[1,0,0,0,0,0,0,0,0]]
assert esMatrizCuadrada(matrix5) is True
