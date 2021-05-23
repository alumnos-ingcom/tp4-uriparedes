################
# Maximiliano Uriel Paredes - @uriparedes
# Ejercicio 10

# UNRN Andina - Introducción a la Ingenieria en Computación
################
import tp4ej9 as primos
import tp4ej1 as enteros

def factores_primos(numero):
    """toma un numero y calcula los divisores, chequea cada uno si es un numero primo o no. Si el divisor es primo, lo agrega a una tupla"""
    tupla = ()
    for i in range(2, numero):
        if(numero%i == 0):
            if(primos.es_primo(i)):
                print(f"{i} es primo")
                tupla = tupla + (i, )
    return tupla
    
def es_palindromo(texto):
    """toma un string, calcula la longitud y compara las letras en los extremos. Devuelve true si es un palindromo y false si no lo es"""
    for i in range(int(len(texto)/2)):
        j = len(texto) -1 - i
        if(texto[i] != texto[j]):
            return False
    return True
    
def prueba():
    msg = "Ingrese un numero entero"
    numero = enteros.ingreso_entero(msg)
    tupla = factores_primos(numero)
    print(f"Los numeros primos divisores de {numero} son {tupla}")
    palabra = "asdfghjklññlkjhgfdsa"
    if(es_palindromo(palabra)):
        print(f"La palabra '{palabra}' es un palindrom!")
    else:
        print(f"La palabra '{palabra}' no es un palindroma!")

if __name__ == "__main__":
    prueba()