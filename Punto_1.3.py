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
