"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.

1
3 1
5 3 1
7 5 3 1
9 7 5 3 1
"""



def pedir_numero(n):
    while True:
        try:
            n = int(input("Introduce un numero entero: "))
            if n > 0:
                return n
            else:
             print("Por favor, introduce un numero entero valido")
        except ValueError:
            print("Entrada no valida. Hazlo de nuevo")


def construir_fila(inicio: int) -> str:
    for i in range(inicio, 0, -2):
        fila += str
            


def triangulo_rectangulo(n: int) -> str:
    cadena = ""
    triangulo = ''
    if num%2 != 0:
        for i in range(1, n1, 2):
            cadena += str(1) +


            
            
def main():
    n = pedir_numero("Introduce un numero entero")






if __name__ == "__main__":
    main()
