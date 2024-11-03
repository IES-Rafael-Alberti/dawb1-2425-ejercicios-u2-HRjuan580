"""
La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. 
Los ingredientes para cada tipo de pizza aparecen a continuación.

Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, 
y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija.
Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas.
Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.
"""

def pedir_tipo_pizza():
  while True:
        tipo_pizza = input("¿Quieres una pizza vegetariana? (si/no): ").strip().lower()
        if tipo_pizza in ["si", "no"]:
            return tipo_pizza == "si"
        print("Respuesta inválida. Por favor, responde con 'si' o 'no'.")


def obtener_ingredientes(vegetariana):
    if vegetariana:
        return ["Pimiento" , "Tofu"]
    else:
        return ["Peperoni" , "Jamón" , "Samón"]
    

def seleccionar_ingredientes(ingredientes):
    while True:
        ingredientes = input("Elige un ingrediente: ")
        if ingredientes in ingredientes:
            return ingredientes
        print(f"{ingredientes} no esta disponible. Elige de nuevo.")
    

def monstrar_resultado(vegetariana, ingrediente):
    if vegetariana:
        tipo = "vegetariana"
    else: 
        tipo = "no vegetariana"
    ingrediente_base = "Mozzarella, Tomate"
    monstrar_resultado = f"Has elegido una pizza {tipo} con los ss ingredientes: {ingrediente_base}, {ingrediente}"
    print("\n" + monstrar_resultado)


def main():
    vegetariana = pedir_tipo_pizza()
    ingredientes_disponibles = obtener_ingredientes(vegetariana)
    print("\nIngredientes disponibles: ")
    for i in ingredientes_disponibles:
        print(f"-{i}")


    ingrediente_elegido = seleccionar_ingredientes(ingredientes_disponibles)
    monstrar_resultado(vegetariana, ingrediente_elegido)

if __name__ == "__main__":
    main()


