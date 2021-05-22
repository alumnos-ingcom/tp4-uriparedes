################
# Maximiliano Uriel Paredes - @uriparedes
# Ejercicio 4
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
    numero1 = soporte.ingreso_real(msg)
    numero2 = soporte.ingreso_real(msg)
    #comparacion = compara( numero1 = soporte.ingreso_real(msg), numero2 = soporte.ingreso_real(msg)) #esto no anda
    comparacion = compara( numero1, numero2)
    if (comparacion > 0):
        print(f"{numero1} es mayor a {numero2}!")
    elif(comparacion < 0):
        print(f"{numero1} es menor a {numero2}!")
    else:
        print(f"{numero1} y {numero2} son iguales!")

if __name__ == "__main__":
    prueba()