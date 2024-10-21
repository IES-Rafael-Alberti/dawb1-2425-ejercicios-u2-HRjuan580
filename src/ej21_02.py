"""
Ejercicio 2.1.2¶
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
"""


def verificar_contrasena(contrasena_guardada):
    try:
        contrasena_usuario = input("Introduce la contraseña: ")
        if contrasena_usuario.lower() == contrasena_guardada.lower():
            print("La contraseña es correcta.")
        else:
            print("La contraseña es incorrecta.")
    
    except Exception as e:
        print("Ocurrió un error:", e)


def main():
    contrasena = "contraseña123"
    verificar_contrasena(contrasena)


if __name__ == "__main__":
    main()



