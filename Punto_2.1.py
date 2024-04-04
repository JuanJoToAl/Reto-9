# Función para calcular el promedio de una lista de números
def promedio(*args) -> float:
    # Inicializamos variables
    suma: int = 0
    contador: int = 0

    # Recorremos los números
    for num in args:
        # Sumamos cada número
        suma += num
        # Aumentamos el contador
        contador += 1

    # Calculamos el promedio
    resultadoPromedio = suma / contador

    # Retornamos el resultado
    return resultadoPromedio

if __name__ == "__main__":
    
    # Pedimos los números al usuario
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    c = float(input("Ingrese el tercer número: "))
    d = float(input("Ingrese el cuarto número: "))
    e = float(input("Ingrese el quinto número: "))

    # Imprimimos los resultados
    print(f"Promedio de los dos primeros números: {promedio(a, b)}")
    print(f"Promedio de los tres primeros números: {promedio(a, b, c)}")
    print(f"Promedio de los cuatro primeros números: {promedio(a, b, c, d)}")
    print(f"Promedio de los cinco números: {promedio(a, b, c, d, e)}")
