def ejecutar():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    num3 = float(input("Ingrese el tercer número: "))
    num4 = float(input("Ingrese el cuarto número: "))
    num5 = float(input("Ingrese el quinto número: "))
    num6 = float(input("Ingrese el sexto número: "))

    promedio = (num1 + num2 + num3 + num4 + num5 + num6) / 6
    print("El promedio es:", promedio)


if __name__ == "__main__":
    ejecutar()
