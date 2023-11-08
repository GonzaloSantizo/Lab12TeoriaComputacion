n = 3  # Cambia el valor de n según lo que necesites
lista_enteros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Usamos una función lambda para calcular la potencia n-ésima de un número
potencia_n = lambda x: x ** n

# Aplicamos la función lambda a cada elemento de la lista usando una comprensión de lista
resultado = [potencia_n(x) for x in lista_enteros]

print(resultado)
