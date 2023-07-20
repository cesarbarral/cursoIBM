import random

def generar_matriz(n):
    """
    Genera una matriz cuadrada de tamaño NxN y la rellena con números aleatorios entre 0 y 9.

    Parameters:
        n (int): Tamaño de la matriz (número de filas y columnas).

    Returns:
        list: Matriz generada.
    """
    matriz = [[random.randint(0, 9) for _ in range(n)] for _ in range(n)]
    return matriz

def imprimir_matriz(matriz):
    """
    Imprime la matriz en pantalla.

    Parameters:
        matriz (list): La matriz a imprimir.
    """
    for fila in matriz:
        print(" ".join(str(elemento) for elemento in fila))

def calcular_suma_filas_columnas(matriz):
    """
    Calcula la suma de los elementos de cada fila y columna.

    Parameters:
        matriz (list): La matriz a analizar.

    Returns:
        tuple: Dos listas, una con la suma de cada fila y otra con la suma de cada columna.
    """
    n = len(matriz)
    sumas_filas = [sum(fila) for fila in matriz]
    sumas_columnas = [sum(matriz[i][j] for i in range(n)) for j in range(n)]
    return sumas_filas, sumas_columnas

def imprimir_suma_filas_columnas(sumas_filas, sumas_columnas):
    """
    Imprime la suma de cada fila y columna en pantalla.

    Parameters:
        sumas_filas (list): Lista con la suma de cada fila.
        sumas_columnas (list): Lista con la suma de cada columna.
    """
    print("\nSuma de cada fila:")
    print(" ".join(str(suma) for suma in sumas_filas))

    print("\nSuma de cada columna:")
    print(" ".join(str(suma) for suma in sumas_columnas))

def main():
    try:
        n = int(input("Ingrese el tamaño de la matriz (N): "))
        if n <= 0:
            raise ValueError("N debe ser un número entero positivo.")

        matriz = generar_matriz(n)

        print("\nMatriz generada:")
        imprimir_matriz(matriz)

        sumas_filas, sumas_columnas = calcular_suma_filas_columnas(matriz)

        imprimir_suma_filas_columnas(sumas_filas, sumas_columnas)

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()