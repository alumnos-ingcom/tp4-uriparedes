class IngresoIncorrecto(Exception):
    """Esta es la Excepcion para el ingreso incorrecto"""
    pass

def prueba():
    num = input("Ingrese un numero ")
    try:
        check = int(num)
    except ValueError as err:
        raise IngresoIncorrecto("Valor invalido!") from err
    return entero

if __name__ == "__main__":
    prueba()