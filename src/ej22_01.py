"""
Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
"""

def pedir_palabra():
    return input("Por favor, ingrese una palabra: ")


def imprimir_palabra(palabra):
    print(palabra)


def repetir_palabra():
    palabra = pedir_palabra()
    contador = 0
    while contador < 10:
        imprimir_palabra(palabra)
        contador += 1

def main():
    repetir_palabra()


if __name__ == "__main__":
    main()
    
