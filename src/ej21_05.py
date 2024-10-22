"""
Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.
"""
# Aqui validaremos la edadd del usuario
def validar_edad():
   edad <= 16 

 
# Aquí pediremos la edad del usuario
def pedir_edad() -> int:
    edad_correcta = False
    edad = None

    while not edad_correcta:
        try:
            edad = int(input("Introduce tu edad: "))
            validar_edad(edad)
            edad_correcta = True  # Se ha ingresado un número válido
        except ValueError as e:
            if edad is None:
                print(f"*Error* El numero introducido no es valido! Intentalo de nuevo")
        else: 
            edad = None
            print(f"*Error* {e}.Intentalo de nuevo!")
    return edad

# Pedir sueldo
def pedir_sueldo() -> int:
    sueldo = False
    sueldo = None

    while not sueldo:
        try:
            sueldo = int(input("Introduce tu sueldo"))
            validar_sueldo(sueldo)
            sueldo_correcta = True  # Se ha ingresado un número válido
        except ValueError as e:
            if sueldo is None:
                print(f"*Error* El sueldo introducido no es correcto")
        else:
            sueldo = None
            print(f"*Error* {e}. Intentalo de nuevo ¡Por favor!")
    return sueldo

# Metodo para validar el sueldo del usuario
def validar_sueldo():
# Metodo para tribunar el sueldo del usuario
def tribunar()
    sueldo <= 1000
 
if __name__ == "__main__":
    main()
