################
# Maximiliano Uriel Paredes - @uriparedes
# Ejercicio 3
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import tp4ej3 as soporte

def signo(numero):
    if(numero > 0):
        print(f"{numero} es positivo")
    elif(numero < 0):
        print(f"{numero} es negativo")
    else:
        print(f"{numero} es 0")
        
def prueba():
    msg = "Ingrese un numero #"
    signo(soporte.ingreso_real(msg))
    
if __name__ == "__main__":
    prueba()