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
