def ejecutar():
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))

    DOS = 2
    superficie = (base * altura) / DOS
    print("La superficie del triángulo es:", superficie)


if __name__ == "__main__":
    ejecutar()
