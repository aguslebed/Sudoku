from typing import Union, List
from fastapi import FastAPI, HTTPException
import copy
from ClaseSudoku import generar_sudoku, sacar_numeros, es_valido, resolver
from fastapi.middleware.cors import CORSMiddleware

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
    sudokuAux = copy.deepcopy(sudoku)
    valido = False
    try:
        # Verifica si la jugada es válida
        if es_valido(sudoku,num,fila,columna):
            sudokuAux[fila][columna] = num
            if resolver(sudokuAux):
                valido = True
                sudoku[fila][columna] = num
                sudoku_respuesta = copy.deepcopy(sudokuAux)
            else:
                print("La jugada es valida, pero el sudoku no tiene solucion") 
        else:
            print("La jugada no es valida")

        return {"Valido": valido,
                "Respuesta": sudoku_respuesta}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



#Para que no salga el problema de CORS
origins = [
    "http://localhost:5500" 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"], 
)



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)