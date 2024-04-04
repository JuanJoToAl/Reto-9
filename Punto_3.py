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
