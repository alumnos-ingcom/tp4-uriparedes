class IngresoIncorrecto(Exception):
    """Esta es la exepcion para un numero ingresado incorrecto"""
    pass

def ingresoNumEntero():
    numero = input("Ingrese un numero entero ")
    try:
        entero = int(numero)
        return entero
    except ValueError as err:
        raise IngresoIncorrecto("No era un Entero!") from None
        ingresoNumEntero();
        return

ingresoNumEntero();
