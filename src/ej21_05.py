"""
Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.
"""

def validar_edad(edad):
    return edad >= 16  


def validar_sueldo(sueldo):
    return sueldo >= 1000 


def pedir_edad() -> int:
    while True:
        try:
            edad = int(input("Introduce tu edad: "))  
            if validar_edad(edad):  
                return edad 
            else:
                print("*Error* Debes ser mayor de 16 años para tributar.")  
        except ValueError:
            print("*Error* El número introducido no es válido. Inténtalo de nuevo.")

def pedir_sueldo() -> int:
    while True:
        try:
            sueldo = int(input("Introduce tu sueldo mensual: "))  
            if validar_sueldo(sueldo):  
                return sueldo  
            else:
                print("*Error* Debes tener ingresos iguales o superiores a 1000 €.")  
        except ValueError:
            print("*Error* El sueldo introducido no es correcto. Inténtalo de nuevo.") 


def main():
    edad = pedir_edad() 
    sueldo = pedir_sueldo()  
    
    
    if validar_edad(edad) and validar_sueldo(sueldo):
        print("Tienes que tributar.")  
    else:
        print("No tienes que tributar.") 


if __name__ == "__main__":
    main()  

