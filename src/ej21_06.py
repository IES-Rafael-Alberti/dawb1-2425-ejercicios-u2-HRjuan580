"""
Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
"""

def determinar_grupo(nombre, sexo):
    if sexo == 'femenino':
        if nombre.lower() < 'm':
            return 'Grupo A'
        else:
            return 'Grupo B'
    elif sexo == 'masculino':
        if nombre.lower() > 'n':
            return 'Grupo A'
        else:
            return 'Grupo B'
    else:
        raise ValueError('Sexo no válido')

def main():
    while True:
        try:
            nombre = input("Introduce tu nombre: ")
            sexo = input("Introduce tu sexo (masculino/femenino): ").lower()
            
            grupo = determinar_grupo(nombre, sexo)
            print(f'Perteneces al: {grupo}')
            
            # Salimos del bucle si todo está bien
            break
        except ValueError as e:
            print(e)
        else:
            print("Consulta exitosa.")

if __name__ == "__main__":
    main()







