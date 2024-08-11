var canvas = document.getElementById('sudokuCanvas');
var ctx = canvas.getContext('2d');
var size = 50; // Tamaño de cada celda en píxeles
var highlightedCell = null;
var board = Array(9).fill(null).map(() => Array(9).fill(0));
var resultado = Array(9).fill(null).map(() => Array(9).fill(0));
var dificultadGlobal = "Facil"; // arranca con la dificultad en facil


ctx.font = '20px Arial';
ctx.textAlign = 'center';
ctx.textBaseline = 'middle';


function simularKeyDown(key) {
    // Crea un evento de teclado
    const event = new KeyboardEvent('keydown', {
      key: key,
      code: `Digit${key}`,
      keyCode: key.charCodeAt(0),
      which: key.charCodeAt(0),
      bubbles: true,
      cancelable: true
    });
  
    // Despacha el evento para que se procese como si se hubiera presionado una tecla
    document.dispatchEvent(event);
  }


function devolverDificultadActual(){
    return dificultadGlobal;
}

function mostrarDificultad(){
    document.getElementById("mostrarDificultad").innerText = "Dificultad elgida: " + dificultadGlobal;
}
function generarNumeroAleatorio(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}
document.addEventListener("DOMContentLoaded", function() {
    mostrarDificultad();
});

const tablero = async (dificultad) => {
    
    const res = await fetch(`http://127.0.0.1:8000/?dificultad=${dificultad}`);
    const data = await res.json();

    return data;
};
// Este pide el sudoku nuevo
const traerNuevoBoard = async (dificultad) => {
    switch(dificultad) {
        case "Facil":
            espaciosEnBlanco = generarNumeroAleatorio(32, 40);
            break;
        case "Medio":
            espaciosEnBlanco = generarNumeroAleatorio(41, 49);
            break;
        case "Dificil":
            espaciosEnBlanco = generarNumeroAleatorio(50, 54);
            break;
        case "Muy dificil":
            espaciosEnBlanco = generarNumeroAleatorio(55, 63);
            break;
        default:
            console.error("Dificultad desconocida:", dificultad);
            return;
    }
    dificultadGlobal = dificultad
    const data = await tablero(espaciosEnBlanco);
    board = data["Sudoku"];
    resultado = data["Respuesta"];
    console.log("Respuesta = ", resultado)
    mostrarDificultad()
    for (var row = 0; row < 9; row++) {
        for (var col = 0; col < 9; col++) {
            if (board[row][col] != 0){
                ctx.fillText(board[row][col], col * size + size / 2, row * size + size / 2);  
            }   
        }
    }
   actualizarBoard()
};

const jugadaValida = async (num, fila, col) => {
    try {
        const res = await fetch(`http://127.0.0.1:8000/ingresarNumero/?num=${num}&fila=${fila}&columna=${col}`);
        if (!res.ok) {
            throw new Error(`Error: ${res.statusText}`);
        }
        const data = await res.json();
       
        return data
    } catch (error) {
        console.error('Error al validar jugada:', error);
    }
};



//Resalta la celda que se selecciona
function highlightCell(row, col) {
    highlightedCell = { row: row, col: col };
    drawBoard();

}

function resaltarCelda(){
    // Resaltar la celda si hay alguna seleccionada
    if (highlightedCell) {
        ctx.fillStyle = 'rgba(0, 100, 255, 0.5)';
        ctx.fillRect(highlightedCell.col * size, highlightedCell.row * size, size, size);
    }
}

function escribirNumeros(){
    ctx.fillStyle = 'rgba(0, 0, 0, 1)';
    for (var row = 0; row < 9; row++) {
        for (var col = 0; col < 9; col++) {
            if (board[row][col] !== 0) {
                ctx.fillText(board[row][col], col * size + size / 2, row * size + size / 2);
            }
        }
    }
}

// Actualiza la matriz
function actualizarBoard(error){
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    drawBoard()
    if (!error){
        resaltarCelda()
    }
    

    //aNDA MEDIO MAL
    if (error) {
        let blinkCount = 0;
        let maxBlinks = 5; // Número total de parpadeos (rojo + transparente = 1 parpadeo)
        let interval = setInterval(() => {
            blinkCount++;
          
            if (blinkCount % 2 === 0) {
                ctx.clearRect(highlightedCell.col * size, highlightedCell.row * size, size, size);
            } else {
                ctx.fillStyle = 'rgba(255, 0, 0, 0.5)';
                ctx.fillRect(
                    highlightedCell.col * size + 0.5, 
                    highlightedCell.row * size + 0.5, 
                    size - 1, 
                    size - 1 
                );
            }
    
            if (blinkCount >= maxBlinks) {
                clearInterval(interval);
                ctx.clearRect(highlightedCell.col * size, highlightedCell.row * size, size, size);
                drawBoard();
                escribirNumeros();
            }
        }, 100); // Ajusta el tiempo entre parpadeos aquí
    }

    escribirNumeros()

    
}
//Evento click. revisa que fila y columna se selecciona y se resalta.
canvas.addEventListener('click', function(event) {
    var rect = canvas.getBoundingClientRect();
    var x = event.clientX - rect.left;
    var y = event.clientY - rect.top;

    var row = Math.floor(y / size);
    var col = Math.floor(x / size);

    highlightCell(row, col);
    actualizarBoard()
});




function drawBoard() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Dibujar las líneas de la cuadrícula
    for (var i = 0; i <= 9; i++) {
        ctx.beginPath();
        ctx.moveTo(i * size, 0);
        ctx.lineTo(i * size, canvas.height);
        ctx.moveTo(0, i * size);
        ctx.lineTo(canvas.width, i * size);
        ctx.lineWidth = (i % 3 === 0) ? 3 : 1;
        ctx.strokeStyle = 'black';
        ctx.stroke();
    }
}

function matrizVacia(){
    for(let i = 0; i < board.length; i++){
        for(let j = 0; j<board.length; j++){
            if (board[i][j] != 0){
                return false;
            }
        }
    }
    
    return true;
}

function contieneCero() {
    let encontrado = false;
    board.forEach(fila => {
        fila.forEach(valor => {
            if (valor === 0) {
                encontrado = true;
            }
        });
    });
    return encontrado;
}

function resolverSudoku(){
    board = resultado
    actualizarBoard()
}

//
function esperarUnCachito() {
    return new Promise(resolve => {
        setTimeout(() => {
            resolve();
        }, 250); 
    });
}
  
async function juego(){

    if (matrizVacia()){
        await traerNuevoBoard(dificultadGlobal)
    
    }
    
    actualizarBoard()
    document.addEventListener('keydown', async function(event) {
        if (highlightedCell) {
            const row = highlightedCell.row;
            const col = highlightedCell.col;
            const key = event.key;
            if ((key >= '1' && key <= '9') &&  board[row][col] =='') {
                const num = parseInt(key);
                const esValida = await jugadaValida(num, row, col);
  
                if (esValida["Valido"]) {
                    resultado = esValida["Respuesta"]
                    board[row][col] = parseInt(key);
                    actualizarBoard();
                    console.log("Respuesta = ", resultado)
    
                }else{
                    actualizarBoard(error=true)
                }
                
            } else if (key === 'Backspace' || key === 'Delete') {
                board[row][col] = 0;
                actualizarBoard();
            }
        }
    });

    
    
    actualizarBoard()

   
    //await esperarUnCachito()
    //window.requestAnimationFrame(juego)
}

juego()

