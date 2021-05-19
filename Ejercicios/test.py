class IngresoIncorrecto(Exception): pass
numero = input("Ingrese Num Entero: ")
try:
    entero = int(numero)
except ValueError:
    raise Exception("Numero Incorrecto!")