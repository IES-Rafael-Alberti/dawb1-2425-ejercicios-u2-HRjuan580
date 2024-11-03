"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
"""


# Metodo para validar el numero introducido
def validar_numero(num: int):
    if num < 1:
        raise ValueError("El número no puede ser negativo")
    if num == 0:
        raise ValueError("El número no puede ser 0")

# Método para pedir número entero
def pedir_numero() -> int:
    numero_correcto = False
    num = None

    while not numero_correcto:
        try:
            num = int(input("Introduce un número entero: "))
            validar_numero(num)
            numero_correcto = True  # Se ha ingresado un número válido
        except ValueError as e:
            print(f"*ERROR* {e}. Inténtalo de nuevo!")

    return num

# Método para saber si es par o impar el número entero
def par_or_impar(num: int):
    if num % 2 == 0:
        print('El número', num, 'es par.')
    else:
        print('El número', num, 'es impar.')

def main():
    num = pedir_numero()
    par_or_impar(num)

if __name__ == "__main__":
    main()
