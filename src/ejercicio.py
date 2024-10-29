MAX_NUMERO = 20
def comprobar_numero(numero): 
    comprobacion = 100
    bandera = True
        
    try:
        comprobacion = int(numero)
        if comprobacion < 0: 
            raise ZeroDivisionError("*ERROR*\nIntroduce un número entero positivo")
        if comprobacion > MAX_NUMERO:
            raise ZeroDivisionError(f"*ERROR*\nLa piramide no puede ser mayor que {MAX_NUMERO}")
         
        
    except ZeroDivisionError as e:
            print(e)
    return comprobacion

def pedir_numero():
    return input("Introduce un número: ")

def crear_triangulo(num):
    print(generar_creciente(num))
    print(generar_decreciente(num))

def generar_creciente(num: int) -> str:
    serie = ""

    for i in range(0, num, 1):
        serie += f"{i} => "
        total = 0
        for j in range(0, i + 1):
            total += j
            serie += f"{j} + "
        serie = serie[:-2] + f" = {total}\n"


    return serie

def generar_decreciente(num: int) -> str:
    serie = ""

    for i in range(num, -1, -1):
        serie += f"{i} => "
        total = 0
        for j in range(0, i + 1):
            total += j
            serie += f"{j} + "
        serie = serie[:-2] + f" = {total}\n"


    return serie




def main():
    numero = pedir_numero()
    numero = comprobar_numero(numero)
    crear_triangulo(numero)


if __name__ == "__main__":
    main()

