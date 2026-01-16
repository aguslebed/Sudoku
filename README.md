# Sudoku

Este proyecto es una aplicacion web para jugar al Sudoku. Permite generar tableros con diferentes dificultades, validar jugadas en tiempo real y resolver el tablero automaticamente.

## Caracteristicas

- Generacion de Sudokus con 4 niveles de dificultad: Facil, Medio, Dificil y Muy Dificil.
- Validacion de movimientos.
- Solucionador automatico de Sudokus.
- Interfaz responsive y moderna.

## Tecnologias Utilizadas

### Backend
- **Lenguaje:** Python
- **Framework:** FastAPI
- **Logica:** Algoritmos de backtracking para generar y resolver tableros.

### Frontend
- **Lenguaje:** HTML5, JavaScript (Vanilla)
- **Estilos:** Tailwind CSS
- **Renderizado:** HTML5 Canvas API para el tablero de juego.

## Como Iniciar el Proyecto

### 1. Iniciar el Backend

El backend se encarga de la logica del juego y la generacion de tableros.

1. Navega a la carpeta `api`.
2. Ejecuta el servidor de desarrollo de FastAPI:

```bash
fastapi dev api.py
```

El servidor estara corriendo en `http://127.0.0.1:8000`.

### 2. Iniciar el Frontend

El frontend es la interfaz grafica del juego.

1. Navega a la carpeta `pagina`.
2. (Opcional) Si necesitas regenerar los estilos CSS, asegurate de tener las dependencias instaladas y ejecuta:

```bash
npx tailwindcss -i ./src/styles.css -o ./src/output.css
```

3. Abre el archivo `src/index.html` en tu navegador web.
