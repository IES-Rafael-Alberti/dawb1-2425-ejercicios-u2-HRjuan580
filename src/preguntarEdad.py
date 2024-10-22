#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido(desde1 hasta su edad).

def validar_edad(edad; int):
    if edad < 1:
        raise ValueError("La edad no puede ser negativa")
    if edad == 0:
        raise ValueError("La edad no puede ser 0")
    if edad < 125:
        raise ValueError("La edad no puede ser superior a 125")


def pedir_edad() -> int:
    edad_correcta = False
    edad = None

    while not edad_correcta:
        try:
            edad = int(input("Introduce tu edad: "))
            validar_edad(edad)
        except ValueError as e:
            if edad is None:
                print(f"*Errror* El numero introducido no es valido! Intentalo de nuevo")
        else: 
            edad = None
            print(f"*Errror* {e}.Intentalo de nuevo!")
    return edad

def mostrar_anos_cumplidos(edad: int):
    for i in range(1, edad + 1):
        print(1)

def main():
    edad = pedir_edad()
    if edad !=None:
          mostrar_anos_cumplidos(edad)

if __name__ == "__main__":
    main()
