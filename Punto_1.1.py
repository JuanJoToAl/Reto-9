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
