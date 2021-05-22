################
# Maximiliano Uriel Paredes - @uriparedes
# Ejercicio 3
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import tp4ej3 as soporte

def compara(numero, otroNumero):
    if(numero > otroNumero):
        return 1
    elif(numero < otroNumero):
        return -1
    else:
        return 0
    

def prueba():
    msg = "Ingrese un numero #"
    print (compara(soporte.ingreso_real(msg), soporte.ingreso_real(msg)))
if __name__ == "__main__":
    prueba()