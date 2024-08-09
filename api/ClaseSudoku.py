import random
import copy
from typing import List, Tuple

# Estructuras globales para mantener el estado del Sudoku
sudoku = [[0] * 9 for _ in range(9)]
sudoku_respuesta = copy.deepcopy(sudoku)

def generar_sudoku() -> List[List[int]]:
    global sudoku, sudoku_respuesta
    sudoku = [[0] * 9 for _ in range(9)]
    sudoku_respuesta = copy.deepcopy(sudoku)
    # Completa los cuadraditos en diagonal
    for i in range(0, 9, 3):
        llenar_cuadradito(sudoku, i, i)
    resolver(sudoku)
    sudoku_respuesta = [row[:] for row in sudoku]
    return sudoku

def sacar_numeros(cant_espacios_vacios: int, sudoku:List[List[int]]) -> List[List[int]]:
    #global sudoku
    if cant_espacios_vacios > 64:
        cant_espacios_vacios = 64
    espacios_vacios = 0
    while espacios_vacios < cant_espacios_vacios:
        fila = random.randint(0, 8)
        columna = random.randint(0, 8)
        if sudoku[fila][columna] != 0:
            sudoku[fila][columna] = 0
            espacios_vacios += 1
    return sudoku

def llenar_cuadradito(sudoku: List[List[int]], fila: int, columna: int):
    nums = random.sample(range(1, 10), 9)
    indice = 0
    for i in range(3):
        for j in range(3):
            sudoku[fila + i][columna + j] = nums[indice]
            indice += 1

def es_valido(sudoku: List[List[int]], num: int, fila: int, columna: int) -> bool:
    # Verifica si el número está en la fila
    for col in range(9):
        if sudoku[fila][col] == num:
            return False
    # Verifica si el número está en la columna
    for row in range(9):
        if sudoku[row][columna] == num:
            return False
    # Verifica el cuadrado de 3x3
    fila_inicio, columna_inicio = 3 * (fila // 3), 3 * (columna // 3)
    for i in range(3):
        for j in range(3):
            if sudoku[fila_inicio + i][columna_inicio + j] == num:
                return False
    return True

def sudoku_resuelto(sudoku: List[List[int]]) -> bool:
    for fila in sudoku:
        for columna in fila:
            if columna == 0:
                return False
    return True

def resolver(sudoku: List[List[int]]) -> bool:
    if sudoku_resuelto(sudoku):
        return True
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                for num in range(1, 10):
                    if es_valido(sudoku, num, i, j):
                        sudoku[i][j] = num
                        if resolver(sudoku):
                            return True
                        sudoku[i][j] = 0
                return False
    return False

def verificarJugada(num,fila,columna,solucion):
    if num == solucion[fila][columna]:
        return True
    else:
        return False

def imprimir_sudoku(sudoku: List[List[int]]):
    for fila in sudoku:
        fila_string = ''
        for num in fila:
            if num == 0:
                fila_string += ' . '
            else:
                fila_string += ' ' + str(num) + ' '
        print(fila_string)

