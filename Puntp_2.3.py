def calcular_cuadrado(*args) -> None:
    # Iteramos a través de los números proporcionados
    for numero in args:

        # Calculamos el cuadrado de cada número
        cuadrado = numero ** 2

        # Imprimimos el resultado
        print(f"El cuadrado de {numero} es {cuadrado}")

# Creamos una lista de números del 1 al 100
numeros = list(range(1, 100 + 1))

# Llamamos a la función para calcular los cuadrados
calcular_cuadrado(*numeros)
