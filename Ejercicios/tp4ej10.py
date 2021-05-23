################
# Maximiliano Uriel Paredes - @uriparedes
# Ejercicio 10

# UNRN Andina - Introducción a la Ingenieria en Computación
################
import tp4ej9 as primos
import tp4ej1 as enteros

def factores_primos(numero):
    """toma un numero y calcula los divisores, chequea cada uno si es un numero primo o no. Si el divisor es primo, lo agrega a una tupla"""
    lista = []
    for i in range(2, numero):
        if(numero%i == 0):
            if(primos.es_primo(i)):
                lista.append(i)
    return tuple(lista)
    
def prueba():
    msg = "Ingrese un numero entero"
    numero = enteros.ingreso_entero(msg)
    tupla = factores_primos(numero)
    print(f"Los numeros primos divisores de {numero} son {tupla}")
    
if __name__ == "__main__":
    prueba()