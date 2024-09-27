#Escribe un programa que se encargue de comprobar si un número es o no primo.
#Hecho esto, imprime los números primos entre 1 y 100.

numero = int(input("Escribe un número por favor: ")) 

def es_primo(numero):
    if numero < 2:  
        return False
    for i in range(2, numero):  
        if numero % i == 0: 
            return False
    return True 

#Imprimir los numeros primos del 1 al 100
for num in range(1, numero):
    if es_primo(num):
        print(num)
