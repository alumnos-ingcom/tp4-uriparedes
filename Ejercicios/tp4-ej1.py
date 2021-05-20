################
# Maximiliano Uriel Paredes - @uriparedes
# Ejercicio 1
# UNRN Andina - Introducción a la Ingenieria en Computación
################

#Esto no anda

def ingreso_entero(mensaje):
    """Esta funcion muestra un mensaje y agrega la # para indicar el ingreso de un numero entero"""
    ingreso = input(mensaje + " #")
    try:
        entero = int(ingreso)
    except ValueError as err:
        raise IngresoIncorrecto("No era un numero entero!") from err
    return entero


def ingreso_entero_reintento(mensaje, cantidad_reintentos=5):
    intentos = cantidad_reintentos
    while (cantidad_reintentos > 0):
        try:
            return ingreso_entero(mensaje)
        except IngresoIncorrecto as err:
            print(f"No era un numero correcto, quedan {intentos} cantidad de intentos")
            cantidad_reintentos = cantidad_reintentos-1
        raise IngresoIncorrecto("Luego e  {intentos}") from err
    
#def ingreso_entero_restringido(mensaje,valor_minimo=0, valor_maximo=10):

class IngresoIncorrecto(Exception):
    """Esta es la Excepcion para el ingreso incorrecto"""
    pass

def prueba():
    num = ingreso_entero_reintento("Ingrese un numero ", cantidad_reintentos = 5)
    print(f"El numero es: {num}")
    pass

if __name__ == "__main__":
    prueba()