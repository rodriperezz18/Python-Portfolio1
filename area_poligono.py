#Crea una única función (importante que sólo sea una) que sea capaz
# * de calcular y retornar el área de un polígono.
# * - La función recibirá por parámetro sólo UN polígono a la vez.
#* - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
# * - Imprime el cálculo del área de un polígono de cada tipo.

def area():
    poligono = input("Por favor indique el polígono (Triangulo, Cuadrado, Rectangulo): ").lower()
    
    if poligono == "triangulo":
        base = float(input("Por favor ingrese la base del triángulo: "))
        altura = float(input("Por favor ingrese la altura del triángulo: "))
        area = (base * altura)/2
        return f"El área del triangulo es: {area}"
    
    elif poligono == "cuadrado":
        lado = float(input("Por favor ingrese el valor del lado del cuadrado: "))
        area = lado ** 2
        return f"El área del cuadrado es: {area}"
    
    elif poligono == "rectangulo":
        base = float(input("Por favor ingrese la base del cuadrado: "))
        altura = float(input("Por favor ingrese la altura del cuadrado: "))
        area = base * altura
        return f"El área del crectangulo es: {area}"
    
    else:
        return "Polígono no soportado, porfavor intenta con Triangulo, Cuadrado o Rectangulo."
        
print(area())

#Por dios esta pelotudes me hace sentir un dios...