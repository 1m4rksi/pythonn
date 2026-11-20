def ejecutar():
    horas = int(input("Ingrese la cantidad de horas: "))
    minutos = int(input("Ingrese la cantidad de minutos: "))
    segundos = int(input("Ingrese la cantidad de segundos: "))

    total_segundos = horas * 3600 + minutos * 60 + segundos
    print("El tiempo expresado en segundos es:", total_segundos)


if __name__ == "__main__":
    ejecutar()
