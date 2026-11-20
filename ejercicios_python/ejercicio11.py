def ejecutar():
    autos = int(input("Ingrese la cantidad de autos vendidos: "))
    valor_auto = float(input("Ingrese el valor de venta de cada auto: "))

    sueldo_basico = 5500
    comision_por_auto = 200
    porcentaje_adicional = 0.05

    comisiones = autos * comision_por_auto
    adicional = autos * valor_auto * porcentaje_adicional
    sueldo_total = sueldo_basico + comisiones + adicional

    print("El salario total del vendedor es:", sueldo_total)


if __name__ == "__main__":
    ejecutar()
