#Escribe un programa que imprima los 50 primeros números de la sucesión
#* de Fibonacci empezando en 0.
#* - La serie Fibonacci se compone por una sucesión de números en
#*   la que el siguiente siempre es la suma de los dos anteriores.
#*   0, 1, 1, 2, 3, 5, 8, 13...

fibonacci = [0, 1] #Inicializar la lista

for i in range(2,50):
    siguiente = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(siguiente)

print(fibonacci[:50])
    
        