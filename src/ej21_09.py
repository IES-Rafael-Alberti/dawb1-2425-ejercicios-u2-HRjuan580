""""
Escribir un programa para una empresa que tiene salas de juegos para todas las edades y 
quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. 

El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, 
si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.
"""


def calcular_edad(edad):
    if edad < 4:
        return 0
    elif 4 <= edad <= 18:
        return 5
    else: 
        return 40

def comprobar_numero(entrada):
    try:
        return int(entrada)
    except ValueError:
        return None
def main():
    while True:
        entrada = input("Introduce la edad el cliente: ")
        edad =comprobar_numero(entrada)

        if edad is None:
            print("Por favor, introduce un numero valido.")
            continue
        precio = calcular_edad(edad)

        if precio == 0:
            print("El cliente entra gratis.")
        else: 
            print(f"El precio de la entrada es: {precio}€")

if __name__ == "__main__":
    main()