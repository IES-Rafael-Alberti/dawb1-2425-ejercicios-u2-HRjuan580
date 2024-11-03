"""
Escribir un programa que pida al usuario dos números y muestre por pantalla su división. 
Si el divisor es cero el programa debe mostrar un error.
"""

    


def dividir_numeros():
    for i in range(3):  # Permitir hasta 3 intentos
        try:
            # Solicitar dos números al usuario
            num1 = input("Introduce el numerador: ")
            num2 = input("Introduce el divisor: ")

            if num1 is None or num2 is None or num1.strip() == "" or num2.strip() == "":
                raise ValueError("No se puede dejar vacío el input.")

            # Convertir a float
            num1 = float(num1)
            num2 = float(num2)

            # Realizar la división
            resultado = num1 / num2
            
            # Mostrar el resultado
            print(f"La división de {num1} entre {num2} es: {resultado}")
            break  # Salir del bucle si la operación es exitosa

        except ValueError as e:
            print(f"Error: {e}. Intenta de nuevo.")
        
        except ZeroDivisionError:
            print("Error: No se puede dividir entre cero. Intenta de nuevo.")
        
        if i == 2:  # Si se han agotado los intentos
            print("Has agotado el número de intentos.")

def main():
    dividir_numeros()

# Ejecutar la función principal
if __name__ == "__main__":
    main()




