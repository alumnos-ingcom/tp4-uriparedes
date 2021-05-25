################
# Maximiliano Uriel Paredes - @uriparedes
# Ejercicio 9
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import tp4ej1 as soporte

def es_primo(numero):
    for i in range(2, numero):
        if(numero%(i) == 0):
            return False
    return True

def prueba():
    msg = "Ingrese un numero entero: "
    if (es_primo(soporte.ingreso_entero(msg))):
        print("El numero es primo!")
    else:
        print("El numero no es primo!")
    
if __name__ == "__main__":
    prueba()