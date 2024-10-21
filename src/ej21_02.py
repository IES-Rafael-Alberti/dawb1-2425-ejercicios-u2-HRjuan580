"""
Ejercicio 2.1.2¶
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
"""


def verificar_contrasena():
    contrasena_guardada = "contraseña"
    intentos = 3  

    for i in range(intentos):
        contrasena_usuario = input("Introduce la contraseña: ")

        try:
            if contrasena_guardada.lower() == contrasena_usuario.lower():
                return "La contraseña es correcta."
            else:
                print("La contraseña es incorrecta.")
        except Exception as e:
            print(f"Ocurrió un error: {e}")

    return None 

def main():
    resultado = verificar_contrasena()
    if resultado is not None:
        print(resultado)
    else:
        print("Has agotado los intentos.")

if __name__ == "__main__":
    main()
