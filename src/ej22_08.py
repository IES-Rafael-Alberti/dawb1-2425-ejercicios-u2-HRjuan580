"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.

1
3 1
5 3 1
7 5 3 1
9 7 5 3 1
"""
# Hacer las 2 formas "Par o Impar".

# Función principal para generar y mostrar el triángulo
def generar_triangulo(n):
    # Iteramos desde 0 hasta n-1 para crear cada fila
    for i in range(n):
        # Calcular el valor inicial para la fila actual
        start = 2 * i + 1
        # Crear una lista de números decrecientes
        fila = [str(start - 2 * j) for j in range(i + 1)]
        
        # Mostrar la fila unida por espacios
        print(" ".join(fila))

# Solicitar al usuario un número entero
def solicitar_numero():
    while True:
        try:
            n = int(input("Introduce un número entero positivo: "))
            if n > 0:
                return n
            else:
                print("Por favor, introduce un número entero positivo.")
        except ValueError:
            print("Entrada no válida. Inténtalo de nuevo.")

# Función principal que coordina el flujo del programa
def main():
    n = solicitar_numero()  # Llamar a la función para obtener un número
    generar_triangulo(n)    # Generar y mostrar el triángulo

# Ejecutar el programa
if __name__ == "__main__":
    main()

