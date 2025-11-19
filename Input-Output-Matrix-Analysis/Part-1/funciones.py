import numpy as np

# TODO Ver posibles problemas con invertir L y U cuando la matriz de Leontief
# No tiene inversa

def calcularLU(A: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    '''
    Args: 

        A (np.ndarray): Matriz a factorizar en LU

    Retorno:

        L (np.ndarray): Matriz triangular inferior con diagonal de unos 
            de la factorización.

        U (np.ndarray): Matriz triangular superior de la factorización.

        P (np.ndarray): Matriz de permutación. 

    La función calcula la factorización LU de la matriz A iterando por cada
    columna, asignando los coeficientes de L y triangulando para llegar a U.
    Se respeta la optimización de memoria y la optimización del pivote.
    '''
    m: int = A.shape[0]
    n: int = A.shape[1]
    Ac: np.ndarray = A.copy()
    P: np.ndarray = np.eye(n)
    
    # Chequeo de dimensión
    if m != n:
        raise AssertionError('La matriz no es cuadrada.')
        
    # Iteramos por cada columna
    for j in range(n - 1):

        # Chequeo si estamos en un sistema con ceros en la columna
        if np.allclose(Ac[j:, j], np.zeros(n - j), rtol=1e-16): break

        # Veo el máximo de la columna desde j hacía "abajo"
        idx_max: int = np.argmax(np.abs(Ac[j:, j])) + j 

        # Si mi pivote no es el máx en modulo, lo cambio para optimizar
        if j != idx_max:
            
            # Cambio filas en Ac y P
            Ac[[j, idx_max], :] = Ac[[idx_max, j], :]
            P[[j, idx_max], :] = P[[idx_max, j], :]

        # Para cada fila, modificamos los valores para obtener U
        for i in range(j + 1, m):

            # Asigno el coeficiente de L
            Ac[i][j] = Ac[i][j] /  Ac[j][j]

            # Implementación que aprovecha el formato de vector
            # actualizando columnas con la columna por el factor de la operacion
            Ac[i][j + 1 : n] -= Ac[j][j + 1: n] * Ac[i][j]         
            
    L = np.tril(Ac, -1) + np.eye(m) 
    U = np.triu(Ac)
    
    return L, U, P


def inversaLU(L: np.ndarray, U: np.ndarray, P: np.ndarray = None) -> np.ndarray:
    
    '''
    Args: 

        L (np.ndarray): Matriz triangular inferior a invertir

        U (np.ndarray): Matriz triangular superior a invertir

        P (np.ndarray): Matriz de permutación correspondiente a la 
        descomposición LU

    Retorno:

        invLU (np.ndaray): Matriz inversa de la matriz LU indicada

    Esta función utiliza las funciones inversaL e inversaU para calcular 
    la inversa de LU de una matriz aprovechando que son triangulares. Como las
    anteriores, no para de ser O(n^3) en su complejidad.
    '''

    # Calculo inversas por separado
    invL = inversaL(L)
    invU = inversaU(U)

    # Calculo la inversa del total
    invLU: np.ndarray = invU @ invL
    if not P is None: invLU = invLU @ P

    return invLU


def inversaL(L: np.ndarray) -> np.ndarray:
    '''
    Args: 

        L (np.ndarray): Matriz triangular inferior a invertir

    Retorno:

        invL (np.ndaray): Matriz triangular inferior ya invertida

    La función solo se encarga de calcular la inversa de una matriz triangular
    inferior asumiendo que está es inversible desde el vamos. La complejidad 
    es O(n^3) pero está medio oculto en las operaciones vectoriales.
    '''

    # Creo la matriz y almaceno la dimensión
    n: int = L.shape[0]
    invL: np.ndarray = np.eye(n)

    # Modifico invU de abajo hacía arriba
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            invL[j] -= (L[j][i]/L[i][i]) * invL[i]

    # Divido cada fila por el coeficiente correspondiente
    for k in range(n):
        invL[k] = invL[k] / L[k][k]            

    return invL


def inversaU(U: np.ndarray) -> np.ndarray:

    '''
    Args: 

        U (np.ndarray): Matriz triangular superior a invertir

    Retorno:

        invU (np.ndaray): Matriz triangular superior ya invertida

    La función solo se encarga de calcular la inversa de una matriz triangular
    superior asumiendo que está es inversible desde el vamos. La complejidad 
    es O(n^3) pero está medio oculto en las operaciones vectoriales.
    '''

    # Creo la matriz y almaceno la dimensión
    n: int = U.shape[0]
    invU: np.ndarray = np.eye(n)

    # Modifico invU de abajo hacía arriba
    for i in range(n - 1, 0, -1):
        for j in range(i - 1, -1, -1):
            invU[j] -= (U[j][i]/U[i][i]) * invU[i]

    # Divido cada fila por el coeficiente correspondiente
    for k in range(n):
        invU[k] = invU[k] / U[k][k]            

    return invU


def solveLy(L: np.ndarray, b: np.ndarray) -> np.ndarray:
    '''
    Args:

        L (np.array)

        b (np.array)

    Retorno:

        res (np.array)

    La funcion resuelve el sistema L.y=b para luego ser utilizado por el
    siguiente paso de la factorización LU. El algoritmo se basa en que la 
    diagonal de L contiene unos y L es una matriz triangular inferior. 
    '''

    # Inicializamos res con el primer elemento de b
    res: list[float] = [b[0]]

    # Para cada fila, empezando por la segunda, calculamos los proximos y
    for row in range(1, L.shape[0]):

        # Asignamos b según el 1 de la diagonal
        current_y: float = b[row]

        # Restamos con los coeficientes y diferentes y
        for column in range(0, row):
            current_y -= L[row][column]*res[column]

        # Por últio, agregamos el y a res
        res.append(current_y)

    return np.array(res)


def solveUx(U: np.ndarray, y: np.ndarray) -> np.ndarray:
    '''
    Args:
        U (np.array)

        y (np.array)

    Retorno:
        res (np.array)

    La funcion resuelve el sistema U.x=y como paso siguiente a el uso 
    de solveLy. El vector y tiene que ser el que sale como respuesta de utilizar
    solveLy El algoritmo se basa en un concepto parecido al anterior pero sin la
    ventaja de tener la diagonal de unos. Recordemos que U es de triangular 
    superior.
    '''

    # Consigo las dimensiones de U y asigno el valor inicial de res como la
    # asignación trivial del último elemento de y div el último elemento de
    # la matriz
    rows, columns = U.shape
    res: list[float] = [y[rows - 1]/U[rows - 1][columns - 1]] 

    # Empezamos ahora a loopear sobre las filas
    for row in range(rows - 2, -1, -1): 

        # Asigno el primer valor como el valor de y
        current_x: float = y[row]

        # Resto los valores de x con coeficientes correspondientes
        for column in range(columns - 1, row, -1):
            current_x -= U[row][column]*res[column - row - 1]

        # Divido por el coeficiente de la matrz en la diagonal
        current_x /= U[row][row]

        # Agrego al principio de res para respetar el orden
        res.insert(0, current_x)

    return np.array(res)
              

if __name__ == "__main__":

    # Declaro vector a descomponer
    A = np.array([
        [ 0.7,   0.,   -0.1],
        [-0.05,  0.,   -0.2],
        [-0.1,  -0.15,  0.9]
    ])

    L, U, P = calcularLU(A)
    invLU = inversaLU(L, U, P)
    print("Matriz:\n", P.T @ L @ U, sep="")
    print("Inversa:\n", invLU, sep="")
    print( "Chequeo de inversa:",
        np.allclose(np.eye(A.shape[0]), invLU @ P.T @ L @ U, rtol=1e-17)
        )
