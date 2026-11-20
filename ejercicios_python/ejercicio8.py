def ejecutar():
    parcial = int(input("Ingrese la cantidad parcial: "))
    total = int(input("Ingrese la cantidad total: "))

    if total != 0:
        porcentaje = (parcial * 100) / total
        print("El porcentaje es:", porcentaje, "%")
    else:
        print("La cantidad total no puede ser cero.")


if __name__ == "__main__":
    ejecutar()
