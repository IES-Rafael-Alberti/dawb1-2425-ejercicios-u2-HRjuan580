"""
Ejercicio 2.1.2¶
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
"""


def almacenar_contraseña():
    return "contraseña"


def verificar_contraseña(contraseña_guardada, contraseña_usuario):
    return contraseña_guardada.lower() == contraseña_usuario.lower()


def main():
    contraseña_guardada = almacenar_contraseña()
    contraseña_usuario = input("Introduce la contraseña: ")
    
    if verificar_contraseña(contraseña_guardada, contraseña_usuario):
        print("La contraseña es correcta.")
    else:
        print("La contraseña es incorrecta.")


if __name__ == "__main__":
    main()




