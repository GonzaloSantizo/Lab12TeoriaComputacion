D = [
    {'make': 'Nokia', 'model': 216, 'color': 'black'},
    {'make': 'Apple', 'model': 2, 'color': 'silver'},
    {'make': 'Huawei', 'model': 50, 'color': 'gold'},
    {'make': 'Samsung', 'model': 7, 'color': 'blue'}
]

# Indica la clave por la cual deseas ordenar los diccionarios
clave_de_orden = 'model'

# Usa sorted con una función lambda para ordenar la lista de diccionarios
D_ordenado = sorted(D, key=lambda x: x[clave_de_orden])

# Imprime la lista ordenada
for diccionario in D_ordenado:
    print(diccionario)
