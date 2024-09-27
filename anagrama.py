
 #* Escribe una función que reciba dos palabras (String) y retorne
#* verdadero o falso (Bool) según sean o no anagramas.
# * - Un Anagrama consiste en formar una palabra reordenando TODAS
# *   las letras de otra palabra inicial.
# * - NO hace falta comprobar que ambas palabras existan.
# * - Dos palabras exactamente iguales no son anagrama.

def obtener_palabras():
    palabra1 = input("Ingresa la primera palabra: ")
    palabra2 = input("Ingresa la segunda palabra: ")
    
    if palabra1 == palabra2:
        return False
    
    if len(palabra1) != len(palabra2):
        return False
    
    if sorted(palabra1) == sorted(palabra2):
        return True
    
    return False
resultado = obtener_palabras()

if resultado:
    print("Las palabras son anagramas.")
else:
    print("Las palabras no son anagramas.")
