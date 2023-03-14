try:
    with open("sudoku.txt", "r") as Sudoku:
        sudoku = []
        for linea in Sudoku:
            sudoku.append([int(i) for i in linea[:-1].split(",")])
except FileNotFoundError:
    print("No se encontró el archivo sudoku.txt")
print("Sudoku a resolver:")
for renglón in sudoku:
    print(renglón[0], renglón[1], renglón[2], renglón[3], renglón[4], renglón[5], renglón[6], renglón[7], renglón[8])
#revisarColumna: Su funcionalidad será el revisar cada columna y saber que números están escritos.
def revisarColumna(sudoku, columna, numero):
    for fila in range(9):
        if sudoku[fila][columna] == numero:
            return False
    return True
#revisarRenglón Su funcionalidad será el revisar cada renglón y saber que números están escritos.
def revisarRenglón(sudoku, fila, numero):
    for columna in range(9):
        if sudoku[fila][columna] == numero:
            return False
    return True
#Revisar Fila Su funcionalidad será el revisar cada fila y saber que números están escritos.
def revisarFila(sudoku, fila, numero):
    for columna in range(9):
        if sudoku[fila][columna] == numero:
            return False
    return True
# Función para revisar el cuadrante
def revisarCuadrante(sudoku, fila, columna, numero):
    fila, columna = ajusteDeCoordenadas(fila, columna)
    for i in range(3):
        for j in range(3):
            if sudoku[i + fila][j + columna] == numero:
                return False
    return True
# Función para ajustar las coordenadas del cuadrante
def ajusteDeCoordenadas(fila, columna):
    return 3*(fila//3), 3*(columna//3)
#Función para copiar el sudoku
def clonarSudoku(sudoku):
    nuevoSudoku = []
    for fila in sudoku:
        nuevoSudoku.append(fila.copy())
    return nuevoSudoku
# Función para obtener las siguientes coordenadas
def siguientesCordenadas(fila, columna):
    if columna == 8:
        return fila + 1, 0
    else:
        return fila, columna + 1

sudokuClon = clonarSudoku(sudoku)

ganamos = False
# resolverSudoku Será el encargado de utilizar los módulos ya definidos y con base a eso, comparar todos los datos y si no hay conflicto, resolver el Sudoku. Debe decir el resultado y si no hay resultado, especificarlo.

def resolverSudoku(sudoku, fila, columna):
    global ganamos
    if ganamos:
        return
    if fila == 9 and columna == 0: # Si ya revisamos todas las filas, entonces ya ganamos
        ganamos = True
        print("Sudoku resuelto:")
        for renglón in sudoku:
            print(renglón[0], renglón[1], renglón[2],renglón[3], renglón[4], renglón[5], renglón[6], renglón[7], renglón[8])
    elif sudoku[fila][columna] != 0:
        SigFila, SigColumna = siguientesCordenadas(fila, columna)
        resolverSudoku(sudoku, SigFila, SigColumna)
    else:
        for i in range(1, 10):
            if revisarColumna(sudoku, columna, i) and revisarRenglón(sudoku, fila, i) and revisarCuadrante(sudoku, fila, columna, i):
                sudoku[fila][columna] = i
                SigFila, SigColumna = siguientesCordenadas(fila, columna)
                resolverSudoku(sudoku, SigFila, SigColumna)
                sudoku[fila][columna] = 0
resolverSudoku(sudoku, 0, 0)

if ganamos == False:
    print('No se puede resolver el sudoku')


