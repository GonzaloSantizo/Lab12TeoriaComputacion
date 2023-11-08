# Definimos la lista inicial y la lista de elementos a borrar
lista_inicial = ['rojo', 'verde', 'azul', 'amarillo', 'gris', 'blanco', 'negro']
elementos_a_borrar = ['amarillo', 'café', 'blanco']

# Usamos una función lambda para filtrar los elementos que no están en la lista de elementos a borrar
filtrar_elementos = lambda lista, elementos_a_borrar: list(filter(lambda x: x not in elementos_a_borrar, lista))

# Aplicamos la función lambda para obtener la lista de elementos remanentes
elementos_remanentes = filtrar_elementos(lista_inicial, elementos_a_borrar)

print(elementos_remanentes)
