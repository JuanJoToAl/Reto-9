# Función para calcular la mediana de una lista de números
def mediana(*args) -> float:

    # Se inicializan las variables
    suma: int = 0
    contador: int = 0

    # Se recorren los números
    for num in args:

        # Se suman los números
        suma += num
        
        # Se aumenta el contador
        contador += 1

        # Si se han procesado 4 números, se calcula la mediana de los 4 primeros
        if contador == 4:
            mediana_x = (b + c) / 2
            print(f"Mediana de los cuatro primeros números: {mediana_x}")

    # Se calcula la mediana final
    resultadoMediana = suma / contador

    # Se retorna la mediana
    return resultadoMediana


if __name__ == "__main__":

    # Se solicitan los números al usuario
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    c = float(input("Ingrese el tercer número: "))
    d = float(input("Ingrese el cuarto número: "))
    e = float(input("Ingrese el quinto número: "))

    # Se calcula y se imprime la mediana de los dos primeros números
    print(f"Mediana de los dos primeros números: {mediana(a, b)}")

    # Se calcula y se imprime la mediana de los tres primeros números
    print(f"Mediana de los tres primeros números: {mediana(a, b, c)}")

    # Se calcula y se imprime la mediana de los cinco números
    print(f"Mediana de los cinco números: {mediana(a, b, c, d, e)}")