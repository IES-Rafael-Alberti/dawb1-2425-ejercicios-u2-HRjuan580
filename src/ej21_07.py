"""
Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

Renta	Tipo impositivo
Menos de 10000€	5%
Entre 10000€ y 20000€	15%
Entre 20000€ y 35000€	20%
Entre 35000€ y 60000€	30%
Más de 60000€	45%

Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.
"""

def tipo_impositivo(renta):
    if renta < 10000:
        return '5%'
    elif renta < 20000:
        return '15%'
    elif renta < 35000:
        return '20%'
    elif renta < 60000:
        return '30%'
    else:
        return '45%'

def main():
    while True:
        try:
            renta = float(input("Introduce tu renta anual en euros: "))
            
            if renta < 0:
                raise ValueError("La renta no puede ser negativa.")
            
            impuesto = tipo_impositivo(renta)
            print(f'Tu tipo impositivo es: {impuesto}')
            
            break

        except ValueError as e:
            print(e)
        else:
            print("Consulta exitosa.")

if __name__ == "__main__":
    main()


