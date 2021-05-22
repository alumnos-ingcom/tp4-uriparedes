################
# Maximiliano Uriel Paredes - @uriparedes
# Ejercicio 8
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import random

def ordenar_mayor_a_menor(lista):#lo cambie a que reciba directamente un array para que sea mas facil la recursividad
    """Recibe un array y devuelve el mismo pero ordenado de menor a mayor"""
    for x in range(len(lista)-1):#llega hasta la longitud -1 porque cuando compara, compara al numero actual contra el siguiente
        if (lista[x] < lista[x+1]):#compara el valor actual con el siguiente
            lista[x], lista[x+1] = lista[x+1], lista[x] #intercambia los valores
            lista = ordenar_mayor_a_menor(lista)#vuelve a llamar la funcion para corregir los elementos
    return lista

def ordenar_menor_a_mayor(lista):
    """Recibe un array y devuelve el mismo pero ordenado de mayor a menor"""
    for x in range(len(lista)-1):#llega hasta la longitud -1 porque cuando compara, compara al numero actual contra el siguiente
        if (lista[x] > lista[x+1]):#compara el valor actual con el siguiente
            lista[x], lista[x+1] = lista[x+1], lista[x] #intercambia los valores
            lista = ordenar_menor_a_mayor(lista)
    return lista

def prueba():
    desordenada = list(range(10))#crea una lista de n cantidad de numeros
    random.shuffle(desordenada)#ordena de manera aleatoria los numeros de la lista
    print(f"Lista desordenada: {desordenada}")
    print(f"Lista ordenada de mayor a menor: {ordenar_mayor_a_menor(desordenada)}")
    print(f"Lista ordenada de menor a mayor: {ordenar_menor_a_mayor(desordenada)}")
    
if __name__ == "__main__":
    prueba()