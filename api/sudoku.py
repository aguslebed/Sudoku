import random


def generarSudoku():
    #Llena una matriz de 9x9 con 0s
    sudoku = [[0] * 9 for _ in range(9)]

    #Completa los cuadraditos en diagonal
    for i in range(0,9,3):    
        llenarCuadradito(sudoku,i,i)
    resolver(sudoku)
    
    return sudoku

def sacarNumeros(sudoku, cantEspaciosVacios):
    fila = 0
    columna = 0
    espaciosVacios = 0

    #Esto es para que haya una solucion como minimo
    if cantEspaciosVacios > 64:
        cantEspaciosVacios = 64

    while espaciosVacios < cantEspaciosVacios:
        fila =  random.randint(0,8)
        columna = random.randint(0,8)
        if sudoku[fila][columna] != 0:
            sudoku[fila][columna] = 0
            espaciosVacios += 1


def llenarCuadradito(sudoku, fila, columna):
    nums = random.sample(range(1, 10), 9)
    indice = 0
    for i in range(3):
        for j in range(3):
            sudoku[fila + i][columna + j] = nums[indice]
            indice += 1

#Mira que se cumplan las reglas de sudoku
def esValido(num, sudoku,fila, columna):    
    #Verifica si el numero esta en la fila
    for col in range(0,len(sudoku)-1):
        if sudoku[fila][col] == num:
            return False
    
    #Verifica si el numero esta en la columna
    for row in range(0,len(sudoku)-1):
        if sudoku[row][columna] == num:
            return False 
    
    #verifica el cuadrado de 3x3
    filaInicio, columnaInicio = 3 * (fila // 3), 3 * (columna // 3)
    for i in range(3):
        for j in range(3):
           if sudoku[filaInicio+i][columnaInicio+j] == num:
               return False 
           
    return True

#Mira si hay algun 0 en el sudoku. Si encuentra alguno, el sudoku no esta resuelto
def sudokuResuelto(sudoku):
    for fila in sudoku:
        for columna in fila:
            if columna == 0:
                return False
    
    return True


def resolver(sudoku):
    if sudokuResuelto(sudoku):
        return True
    
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                for num in range(1, 10):
                    if esValido(num, sudoku, i, j):
                        sudoku[i][j] = num
                        if resolver(sudoku):
                            return True
                        sudoku[i][j] = 0
                
                return False  
    return False

def imprimirSudoku(sudoku):
   
    for fila in sudoku:
        filaString = ''
        for num in fila:
            if num == 0:
                filaString += ' . '      
            else:
                filaString += ' ' + str(num) +' '
        print(filaString)



sudoku =[[0, 1, 0, 2, 3, 5, 8, 0, 9], [3, 2, 8, 0, 9, 6, 4, 5, 7], [9, 6, 5, 0, 8, 7, 1, 3, 2], [0, 3, 0, 0, 1, 8, 9, 4, 6], [4, 0, 1, 6, 7, 9, 2, 0, 3], [6, 0, 9, 3, 0, 2, 5, 7, 1], [0, 7, 2, 0, 5, 3, 0, 1, 4], [1, 9, 3, 0, 0, 4, 7, 2, 5], [0, 0, 6, 7, 2, 0, 3, 9, 8]]
print("")
resolver(sudoku)
imprimirSudoku(sudoku)

