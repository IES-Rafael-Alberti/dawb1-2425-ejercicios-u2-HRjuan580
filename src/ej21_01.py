"""
Ejercicio 2.1.1
Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
"""



def verificar_edad(edad):
    return edad >= 18

def obtener_edad():
        try:
            edad = int(input("Por favor, ingresa tu edad: "))
            return edad
        except ValueError:
            print("Error: Debes ingresar un número válido.")

def main():
    edad = obtener_edad()
    
    if verificar_edad(edad):
        print("Eres mayor de edad.")
    else:
        print("No eres mayor de edad.")

if __name__ == "__main__":
    main()







    