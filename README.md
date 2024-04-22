# Reto 9

### 1. De los retos anteriores selecione 3 funciones y escribalas en forma de lambdas.

* Clase 9 / Reto 6 / Punto 3: 
Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.
```python
if __name__ == "__main__":

    # Pedimos la cantidad de aves por tipo
    numGallina = float(input("Ingrese la cantidad de gallinas: "))
    numGallo = float(input("Ingrese la cantidad de gallos: "))
    numPollito = float(input("Ingrese la cantidad de pollitos: "))

    # Calculamos la carne de gallina
    carneGallina = (lambda x: 6 * x)(numGallina)  # 6 kg por gallina

    # Calculamos la carne de gallo
    carneGallo = (lambda y: 7 * y)(numGallo)  # 7 kg por gallo

    # Calculamos la carne total
    totalCarne = (lambda x, y, z: x + y + z)(carneGallina, carneGallo, numPollito)

    # Mostramos la información
    print(f"La cantidad de carne de aves es {totalCarne}kg")
    print(f"La cantidad de carne de gallina es {carneGallina}kg")
    print(f"La cantidad de carne de gallo es {carneGallo}kg")
    print(f"La cantidad de carne de pollito es {numPollito}kg")
```

* Clase 9 / Reto 6 / Punto 4: 
Mi mamá me manda a comprar P panes a 300 cada uno, M bolsas de leche a 3300 cada una y H huevos a 350 cada uno. Hacer un programa que me diga las vueltas (o lo que quedo debiendo) cuando me da un billete de B pesos.

```python
if __name__ == "__main__":
 
    # Preguntamos las cantidades por ingrediente
    pan = float(input("¿Cuántos panes dijo mamá?"))  
    leche = float(input("¿Cuánta leche dijo mamá?"))
    huevos = float(input("¿Cuántos huevos dijo mamá?"))

    # Preguntamos el dinero que entregó
    billete = float(input("¿Cuánta plata me dio mamá?"))

    # Función para calcular el total
    total = lambda w, x, y, z: w - (300 * x + 3300 * y + 350 * z)  
    vueltas = total(billete, pan, leche, huevos)  

    # Si hay vueltas, las mostramos
    if vueltas >= 0:
        print(f"Las vueltas son {vueltas}")  

    # Si no hay vueltas, mostramos la deuda
    else:
        print(f"Pailas doña Mariluz, le quedo debiendo {vueltas}")  
```

* Clase 9 / Reto 6 / Punto 6: 
El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día. Hacer un programa que diga el número total de personas que se han contagiado cuando pasen D días a partir de hoy, si el número de contagiados actuales es C.

```python
if __name__ == "__main__":

    # Solicitamos la cantidad actual de enfermos
    enfermos = int(input("Cantidad de enfermos actuales"))

    # Solicitamos la cantidad de días para estimar el número de enfermos
    dias = int(input("Cantidad de días a estimar el número de enfermos"))

    # Calculamos el total de contagios utilizando la fórmula dada
    totalContagios = (lambda x, y: x * 2 ** y)(enfermos, dias)

    # Mostramos los días para estimar la cantidad de enfermos
    print(f"Los días a estimar la cantidad de enfermos son {dias}")

    # Mostramos el número de personas contagiadas
    print(f"El número de personas contagiadas será {totalContagios}")
```

### 2. De los retos anteriores selecione 3 funciones y escribalas con argumentos no definidos (*args).

* Clase 9 / Reto 6 / Punto 7: 
Escriba un programa que pida 5 números reales y calcule la siguiente operación usando una función:
El promedio

```python
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
```

* Clase 9 / Reto 6 / Punto 7: 
Escriba un programa que pida 5 números reales y calcule la siguiente operación usando una función:
La mediana

```python
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
```

* Clase 10 / Reto 7 / Punto 1: 
Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.

```python
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
```

### 3. Escriba una función recursiva para calcular la operación de la potencia.

```python
def exponenteRecursivo(base: int, exponenteParada: int) -> int:

    # Caso base: Si el exponente es 0, la potencia es 1
    if exponenteParada == 0:
        return 1
   
    # Caso base: Si el exponente es 1, la potencia es igual a la base
    elif exponenteParada == 1:
        return base
   
    # Si el exponente es negativo, calculamos la potencia inversa
    elif exponenteParada < 0:
        return 1 / (base * exponenteRecursivo(base, -exponenteParada - 1))
   
    # Caso general: Calculamos la potencia recursivamente
    else:
        return base * exponenteRecursivo(base, exponenteParada - 1)

if __name__ == "__main__":

    # Solicitamos al usuario los valores de la base y el exponente
    base = int(input("Valor de la base: "))
    exponenteParada = int(input("Valor del exponente: "))

    # Calculamos la potencia utilizando la función recursiva
    potencia = exponenteRecursivo(base, exponenteParada)
    
    # Imprimimos el resultado
    print(f"La potencia de {base} elevado a {exponenteParada} es {potencia}")
```

### 4. Utilice la siguiente plantilla de code para contar el tiempo:

```python
import time

start_time = time.time()
# instrucciones sobre las cuales se quiere medir tiempo de ejecución
end_time = time.time()

timer = end_time - start_time
print(timer)
```

* Realice pruebas para calcular fibonacci con iteración o con recursión. Determine desde que número de la serie la diferencia de tiempo se vuelve significativa.
**Importante:** Revisar este [hilo](https://stackoverflow.com/questions/8220801/how-to-use-timeit-module).

```python
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
```
### 4.1. Extra: código que determina desde que número de la serie la diferencia de tiempo se vuelve significativa usando iteración de sumas.

```python
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
```

### 5. Crear cuenta en [stackoverflow](https://stackoverflow.com/) y adjuntar imagen en el repo

[![Anotaci-n-2024-03-29-220026.png](https://i.postimg.cc/1529cTd0/Anotaci-n-2024-03-29-220026.png)](https://postimg.cc/F7b5hPN1)

### 6. Cosas de adultos....ir a [linkedin](https://www.linkedin.com/) y crear perfil....NO IMPORTA que estén iniciando, si tienen tiempo para redes poco útiles como fb, insta, o tiktok tienen tiempo para crear un perfil mamalón. Dejar enlace en el repo.

Enlace de perfil en linkedin: 
www.linkedin.com/in/juan-jose-tobar-alvarez
