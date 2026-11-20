import ejercicio1
import ejercicio2
import ejercicio3
import ejercicio4
import ejercicio5
import ejercicio6
import ejercicio7
import ejercicio8
import ejercicio9
import ejercicio10
import ejercicio11


opciones = {
    "1": ("Suma de 2 números", ejercicio1.ejecutar),
    "2": ("Suma de 4 números", ejercicio2.ejecutar),
    "3": ("Superficie del rectángulo", ejercicio3.ejecutar),
    "4": ("Superficie del cuadrado", ejercicio4.ejecutar),
    "5": ("Convertir tiempo a segundos", ejercicio5.ejecutar),
    "6": ("Superficie del triángulo", ejercicio6.ejecutar),
    "7": ("Promedio de 6 números", ejercicio7.ejecutar),
    "8": ("Calcular porcentaje", ejercicio8.ejecutar),
    "9": ("Separar día, mes y año", ejercicio9.ejecutar),
    "10": ("Calcular nota final", ejercicio10.ejecutar),
    "11": ("Calcular salario del vendedor", ejercicio11.ejecutar),
}

while True:
    print("\n===== TRABAJO PRÁCTICO - PYTHON =====")
    for numero, (descripcion, _) in opciones.items():
        print(f"{numero}. {descripcion}")
    print("0. Salir")

    seleccion = input("Seleccione un ejercicio: ")

    if seleccion == "0":
        print("Programa finalizado.")
        break
    elif seleccion in opciones:
        print()
        opciones[seleccion][1]()
    else:
        print("Opción incorrecta. Intente nuevamente.")
