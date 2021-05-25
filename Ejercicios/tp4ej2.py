################
# Maximiliano Uriel Paredes - @uriparedes
# Ejercicio 2
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import tp4ej1 as soporte

def suma_lenta(numero1, numero2):
    suma = numero1
    while (suma != (numero1+numero2)):
        if(numero2 > 0):
            suma = suma+1
        else:
            suma = suma-1
    return suma

def prueba():
    msg = "Ingrese un numero entero "
    num = suma_lenta(soporte.ingreso_entero(msg), soporte.ingreso_entero(msg))
    print(f"la suma de los numeros es {num}")

if __name__ == "__main__":
    prueba()