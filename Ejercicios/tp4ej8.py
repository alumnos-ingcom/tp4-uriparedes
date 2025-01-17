################
# Maximiliano Uriel Paredes - @uriparedes
# Ejercicio 8
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import random

def ordenar_mayor_a_menor_recursivo(lista):#lo cambie a que reciba directamente un array para que sea mas facil la recursividad
    """Recibe un array y devuelve el mismo pero ordenado de menor a mayor y como una tupla"""
    for x in range(len(lista)-1):#llega hasta la longitud -1 porque cuando compara, compara al numero actual contra el siguiente
        if (lista[x] < lista[x+1]):#compara el valor actual con el siguiente
            lista[x], lista[x+1] = lista[x+1], lista[x] #intercambia los valores
            lista = ordenar_mayor_a_menor_recursivo(lista)#vuelve a llamar la funcion para corregir los elementos
    return tuple(lista)
#
# def ordenar_menor_a_mayor(lista):
#     """Recibe un array y devuelve el mismo pero ordenado de menor a mayor"""
#     for x in range(len(lista)-1):#llega hasta la longitud -1 porque cuando compara, compara al numero actual contra el siguiente
#         if (lista[x] > lista[x+1]):#compara el valor actual con el siguiente
#             lista[x], lista[x+1] = lista[x+1], lista[x] #intercambia los valores
#             lista = ordenar_menor_a_mayor(lista)#vuelve a llamar la funcion para corregir los elementos
#     return lista
#
# def prueba():
#     desordenada = list(range(10))#crea una lista de n cantidad de numeros
#     random.shuffle(desordenada)#ordena de manera aleatoria los numeros de la lista
#     print(f"Lista desordenada: {desordenada}")
#     ordenada = ordenar_mayor_a_menor(desordenada)
#     print(f"Lista ordenada de mayor a menor: {ordenada}")
#     ordenada = ordenar_menor_a_mayor(desordenada)
#     print(f"Lista ordenada de menor a mayor: {ordenada}")

def ordenar_mayor_a_menor(uno, dos, tres):
    if(uno < dos):
        uno, dos = dos, uno
    if(dos < tres):
        dos, tres = tres, dos
    if(uno < dos):
        uno, dos = dos, uno
    tupla = (uno, dos, tres)
    return tupla

def ordenar_menor_a_mayor(uno, dos, tres):
    if(uno > dos):
        uno, dos = dos, uno
    if(dos > tres):
        dos, tres = tres, dos
    if(uno > dos):
        uno, dos = dos, uno
    tupla = (uno, dos, tres)
    return tupla

def prueba():
    desordenada = list(range(20))#crea una lista de n cantidad de numeros
    random.shuffle(desordenada)#ordena de manera aleatoria los numeros de la lista
    tupla = ordenar_mayor_a_menor_recursivo(desordenada)
    print(f"Tupla aleatoria ordenada de mayor a menor de manera recursiva: {tupla}")
    tupla = ordenar_mayor_a_menor(1, 3, 2)
    print(f"Tupla ordenada de mayor a menor: {tupla}")
    tupla = ordenar_menor_a_mayor(1, 3, 2)
    print(f"Tupla ordenada de menor a mayor: {tupla}")

if __name__ == "__main__":
    prueba()
