################
# Maximiliano Uriel Paredes - @uriparedes
# Ejercicio 1
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def ingreso_entero(mensaje):
    """Esta funcion muestra un mensaje y agrega la # para indicar el ingreso de un numero entero"""
    ingreso = input(mensaje + " #")
    try:
        entero = int(ingreso)
    except ValueError as err:
        raise IngresoIncorrecto("No era un numero entero!") from err
    return entero


def ingreso_entero_reintento(mensaje, cantidad_reintentos=5):
    if (cantidad_reintentos > 0):
        try:
            return ingreso_entero(mensaje)
        except IngresoIncorrecto as err:
            cantidad_reintentos = cantidad_reintentos-1
            print(f"No era un numero correcto, quedan {cantidad_reintentos} cantidad de intentos")
            ingreso_entero_reintento(mensaje, cantidad_reintentos)
    else:
        raise IngresoIncorrecto("Luego e  {intentos}") from err
    
def ingreso_entero_restringido(mensaje,valor_minimo=0, valor_maximo=10):
    msg = f"{mensaje}entre {valor_minimo} y {valor_maximo} "
    numero = ingreso_entero(msg)
    if(numero>=valor_minimo and numero<=valor_maximo):
        return numero
    else:
        raise IngresoIncorrecto(msg)

class IngresoIncorrecto(Exception):
    """Esta es la Excepcion para el ingreso incorrecto"""
    pass

def prueba():
    msg = "Ingrese un numero "
    num = ingreso_entero(msg)
    num = ingreso_entero_reintento(msg, cantidad_reintentos = 5)
    num = ingreso_entero_restringido(msg, 0, 5)
    pass

if __name__ == "__main__":
    prueba()