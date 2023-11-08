# Definimos la matriz X como una lista de listas
X = [[1, 2, 3, 1],
     [4, 5, 6, 0],
     [7, 8, 9, -1]]

# Usamos una función lambda para obtener la matriz transpuesta
transpuesta = lambda X: list(map(list, zip(*X)))

# Aplicamos la función lambda a la matriz X
matriz_transpuesta = transpuesta(X)

# Imprimimos la matriz transpuesta
for fila in matriz_transpuesta:
    print(fila)
