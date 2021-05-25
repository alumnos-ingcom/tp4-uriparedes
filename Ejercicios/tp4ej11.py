################
# Maximiliano Uriel Paredes - @uriparedes
# Ejercicio 11

# UNRN Andina - Introducción a la Ingenieria en Computación
################

def es_palindromo(texto):
    """toma un string, calcula la longitud y compara las letras en los extremos. Devuelve true si es un palindromo y false si no lo es"""
    for i in range(len(texto)//2):
        j = len(texto) -1 - i
        if(texto[i] != texto[j]):
            return False
    return True
    
def prueba():
    palabra = input("ingrese una palabra: ")
    if(es_palindromo(palabra)):
        print(f"La palabra '{palabra}' es un palindromo!")
    else:
        print(f"La palabra '{palabra}' no es un palindroma!")

if __name__ == "__main__":
    prueba()
