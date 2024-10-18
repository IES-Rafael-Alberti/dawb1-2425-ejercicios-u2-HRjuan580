"""
Ejercicio 2.1.1
Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
"""



def mayor_de_edad(edad):
   return edad >= 18

    
def main():
    while True:
        try: 
            edad = int(input("Introduzca su edad: "))
            if mayor_de_edad(edad):
                print("Eres mayor de edad.")
            else:
                print("No eres mayor de edad.")
        except ValueError:
            print("Introduce un numero que sea valido. ")

if __name__ == "__main__":
    main()






    