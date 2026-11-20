def ejecutar():
    fecha = int(input("Ingrese la fecha con formato DDMMAAAA: "))

    dia = fecha // 1000000
    mes = (fecha // 10000) % 100
    anio = fecha % 10000

    print("Día:", dia)
    print("Mes:", mes)
    print("Año:", anio)


if __name__ == "__main__":
    ejecutar()
