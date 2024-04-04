import time

# Función que calcula el n-ésimo término de la sucesión de Fibonacci
# de forma recursiva.
def fiborecursivo(n: int) -> int:
    if n <= 1:
        return n
    else:
        return fiborecursivo(n - 1) + fiborecursivo(n - 2)

# Inicio del programa principal
if __name__ == "__main__":

    # Variable para el número de término
    num : int = 1

    # Medición del tiempo de ejecución
    start_time = time.time()

    # Cálculo del n-ésimo término
    seriefibo = fiborecursivo(num)
    end_time = time.time()
    
    # Cálculo del tiempo de ejecución
    timer = end_time - start_time

    # Bucle para aumentar el número de términos hasta superar 4 segundos
    while timer <= 4:
        num += 1
        start_time = time.time()
        seriefibo = fiborecursivo(num)
        end_time = time.time()
        timer += end_time - start_time

    # Impresión del resultado
    print(f"La sucesión en el término {num} es {seriefibo}")
    print(f"El tiempo de ejecución para {num} términos es significativo")
    print(f"Tiempo: {timer} segundos")
