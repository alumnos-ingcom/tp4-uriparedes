################
# Maximiliano Uriel Paredes - @uriparedes
# Ejercicio 6
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def minimo(lista):
    minimo = lista[0]
    for i in lista:
        if (i < minimo):
            minimo = i
    return minimo

def maximo(lista):
    maximo = lista[0]
    for i in lista:
        if (i > maximo):
            maximo = i
    return maximo

def prueba():
    array = [3, 1, 2, 0, 4, 5]
    maximo = maximo(array)
    minimo = minimo(array)
    print(f"el valor minimo es: {minimo}")
    print(f"el valor maximo es: {maximo}")

if __name__ == "__main__":
    prueba()