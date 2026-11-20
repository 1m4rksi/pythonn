def ejecutar():
    parciales = float(input("Ingrese la nota de los exámenes parciales (0 a 10): "))
    trabajos = float(input("Ingrese la nota de los trabajos prácticos (0 a 10): "))
    integrador = float(input("Ingrese la nota del examen integrador (0 a 10): "))

    nota_final = parciales * 0.30 + trabajos * 0.20 + integrador * 0.50
    print("La nota final es:", nota_final)


if __name__ == "__main__":
    ejecutar()
