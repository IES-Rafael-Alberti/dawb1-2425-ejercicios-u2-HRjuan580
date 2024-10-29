# Adivinar el numero y que tenga un menu de inicio
import random

def jugar():
    numero_secreto = random.randint(1, 100)
    intentos = 0
    while True:
        try:
            adivinanza = int(input("Adivina el número entre 1 y 100: "))
            intentos += 1
            if adivinanza < numero_secreto:
                print("El número secreto es mayor. Intenta de nuevo.")
            elif adivinanza > numero_secreto:
                print("El número secreto es menor. Intenta de nuevo.")
            else:
                print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.\n")
                break
        except ValueError:
            print("Por favor, ingresa un número válido.")

def main():
    opcion = None
    while opcion != "3":
        
        print("=== MENÚ PRINCIPAL ===")
        print("1. Jugar")
        print("2. Instrucciones")
        print("3. Salir")
        print("======================")
        
        
        opcion = input("Elige una opción (1, 2, o 3): ")

        if opcion == "1":
            jugar()
        elif opcion == "2":
            
            print("\n=== INSTRUCCIONES ===")
            print("Adivina el número secreto entre 1 y 100.")
            print("Después de cada intento, se te dirá si el número es más alto o más bajo.")
            print("¡Buena suerte!\n")
        elif opcion == "3":
            print("¡Gracias por jugar! Hasta luego.")
        else:
            print("Opción no válida. Intenta de nuevo.\n")

if __name__ == "__main__":
    main()
