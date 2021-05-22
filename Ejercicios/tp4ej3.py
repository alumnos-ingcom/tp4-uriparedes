################
# Maximiliano Uriel Paredes - @uriparedes
# Ejercicio 3
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def ingreso_real(mensaje):
    num = input(mensaje)
    try:
        real = float(num)
    except ValueError as err:
        raise IngresoIncorrecto("No era un numero real!") from err
    return real

def convertir_a_fahrenheit(centigrados):
    fahrrenheit = (centigrados - 32) * (5/2)
    return fahrrenheit

def convertir_a_centigrados(fahrenheit):
    centigrados = (fahrenheit * (2/5)) + 32
    return centigrados

class IngresoIncorrecto(Exception):
    """Esta es la Excepcion para el ingreso incorrecto"""
    pass

def prueba():
    #temperatura = ingreso_real("Ingrese una temperatura en grados centigrados: ")
    msg = "Ingrese una temperatura en grados "
    print(f"La temperatura en fahrenheit es : {convertir_a_fahrenheit(ingreso_real(msg + 'centigrados: '))}")
    print(f"La temperatura en centigrados es : {convertir_a_centigrados(ingreso_real(msg + 'fahrenheit: '))}")
    
if __name__ == "__main__":
    prueba()