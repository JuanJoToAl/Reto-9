# Configuración para manejar números grandes
import sys
sys.set_int_max_str_digits(1000000000)

import time

# Función para calcular el término n de la sucesión de Fibonacci
def Fibonacci(sumando, terminoAnterior) -> int:
  
    # Cálculo iterativo de los términos
    # Se suman los dos últimos términos para obtener el siguiente
    suma = sumando + terminoAnterior
    print(f" {sumando} + {terminoAnterior} = {suma} (término {termino})")

    # Actualización de variables para el siguiente cálculo
    # El último término se convierte en el penúltimo
    terminoAnterior = sumando
    # La suma de los dos últimos términos se convierte en el último
    sumando = suma

    return sumando, terminoAnterior

# Pide al usuario el término deseado
if __name__ == "__main__":
    # Inicialización de variables
    sumando: int = 1
    termino: int = 1
    terminoAnterior = 0

    # Medición del tiempo de ejecución para el primer término
    start_time = time.time()
    sumando, terminoAnterior = Fibonacci(sumando, terminoAnterior)
    end_time = time.time()
    timer = end_time - start_time

    # Bucle para aumentar el número de términos hasta superar 4 segundos
    while timer <= 4:
        termino += 1
        # Medición del tiempo de ejecución para cada término
        start_time = time.time()
        sumando, terminoAnterior = Fibonacci(sumando, terminoAnterior)
        end_time = time.time()
        # Actualización del tiempo total
        timer += end_time - start_time

    # Impresión del resultado
    print(f"El valor de la sucesión en el término {termino + 1} es: {sumando}")
    print(f"El tiempo de ejecución para {termino + 1} términos es significativo")
    print(f"Tiempo total: {timer}")
