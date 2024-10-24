"""
Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.
"""
# Función para validar si la edad es adecuada para tributar
def validar_edad(edad):
    return edad >= 16  # Retorna True si la edad es mayor o igual a 16

# Función para validar si el sueldo es suficiente para tributar
def validar_sueldo(sueldo):
    return sueldo >= 1000  # Retorna True si el sueldo es mayor o igual a 1000 €

# Función para pedir la edad del usuario
def pedir_edad() -> int:
    while True:
        try:
            edad = int(input("Introduce tu edad: "))  # Solicita la edad
            if validar_edad(edad):  # Verifica si la edad es válida
                return edad  # Devuelve la edad si es válida
            else:
                print("*Error* Debes ser mayor de 16 años para tributar.")  # Mensaje de error
        except ValueError:
            print("*Error* El número introducido no es válido. Inténtalo de nuevo.")  # Manejo de excepciones

# Función para pedir el sueldo del usuario
def pedir_sueldo() -> int:
    while True:
        try:
            sueldo = int(input("Introduce tu sueldo mensual: "))  # Solicita el sueldo
            if validar_sueldo(sueldo):  # Verifica si el sueldo es válido
                return sueldo  # Devuelve el sueldo si es válido
            else:
                print("*Error* Debes tener ingresos iguales o superiores a 1000 €.")  # Mensaje de error
        except ValueError:
            print("*Error* El sueldo introducido no es correcto. Inténtalo de nuevo.")  # Manejo de excepciones

# Función principal para determinar si el usuario debe tributar
def main():
    edad = pedir_edad()  # Llama a la función para pedir la edad
    sueldo = pedir_sueldo()  # Llama a la función para pedir el sueldo
    
    # Comprueba si el usuario debe tributar
    if validar_edad(edad) and validar_sueldo(sueldo):
        print("Tienes que tributar.")  # Mensaje si debe tributar
    else:
        print("No tienes que tributar.")  # Mensaje si no debe tributar

# Punto de entrada del programa
if __name__ == "__main__":
    main()  # Ejecuta la función principal

