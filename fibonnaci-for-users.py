num = int(input("Cuantos numero de la sucesion queres ver?: "))


if num <= 0:
    print("Porfavor ingresa un numero mayor que 0.")
elif num == 1:
    print([0])
else:
    fibonacci = [0, 1] #Inicializar la lista

    for i in range(2, num):
        siguiente = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(siguiente)
    print(fibonacci[:num])n
