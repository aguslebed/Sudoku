from typing import Union, List
from fastapi import FastAPI, HTTPException
import copy
from ClaseSudoku import generar_sudoku, sacar_numeros, es_valido, verificarJugada


app = FastAPI()

response = []
sudoku = [[0] * 9 for _ in range(9)]
sudoku_respuesta = copy.deepcopy(sudoku)

@app.get("/")
def read_root(dificultad:int):
    global sudoku, sudoku_respuesta
    sudoku = generar_sudoku()
    sudoku_respuesta = copy.deepcopy(sudoku)
    sudoku = sacar_numeros(dificultad,sudoku)
    print(sudoku)
    return {"Sudoku": sudoku, "Respuesta": sudoku_respuesta}

@app.get("/ingresarNumero/")
def ingresarNumero(num: int, fila: int, columna: int):
    global sudoku
    global sudoku_respuesta
    try:
        # Verifica si la jugada es válida
        valido = verificarJugada(num, fila, columna,sudoku_respuesta)
        return {"Valido": valido}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)