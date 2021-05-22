################
# Maximiliano Uriel Paredes - @uriparedes
# Ejercicio 7
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import tp4ej1 as soporte

def division_lenta(dividendo, divisor):
    cociente = 0
    while (dividendo >= divisor):
        dividendo = dividendo - divisor
        print(f"dividendo ={dividendo}")
        cociente = cociente +1
    return cociente, dividendo

def prueba():
    msg = "Ingrese un numero entero: "
    print(f"{division_lenta(soporte.ingreso_entero(msg), soporte.ingreso_entero(msg))}")
    

if __name__ == "__main__":
    prueba()