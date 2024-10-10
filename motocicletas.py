class motocicleta:
    nueva = True
    motor = False  # El motor debe estar apagado por defecto
    
    def __init__(self, color, matricula, combustible_litros, numero_ruedas, marca, modelo, fecha_fabricacion, velocidad_punta, peso, cilindrada=None, transmision=None):
        self.color = color
        self.matricula = matricula
        self.combustible_litros = combustible_litros
        self.numero_ruedas = numero_ruedas
        self.marca = marca
        self.modelo = modelo
        self.fecha_fabricacion = fecha_fabricacion
        self.velocidad_punta = velocidad_punta
        self.peso = peso
        self.cilindrada = cilindrada  # Atributo opcional
        self.transmision = transmision  # Atributo opcional
    
    
    
    
    # Método para arrancar el motor
    def arrancar(self):
        if not motocicleta.motor:
            motocicleta.motor = True
            print(f"El motor de {self.marca} {self.modelo} ha arrancado.")
        else:
            print(f"El motor de {self.marca} {self.modelo} ya está en marcha.")
    
    
    
    
    # Método para detener el motor
    def detener(self):
        if motocicleta.motor:
            motocicleta.motor = False
            print(f"El motor de {self.marca} {self.modelo} se ha detenido.")
        else:
            print(f"El motor de {self.marca} {self.modelo} ya estaba detenido.")
    
    
    
    
    # Método para consultar el precio
    def consultar_precio(self):
        if hasattr(self, 'precio'):
            print(f"El precio de la motocicleta '{self.marca} {self.modelo}' es de {self.precio} $.")
        else:
            print(f"La motocicleta '{self.marca} {self.modelo}' no tiene precio asignado.")
            
            
            
            
    #Metodo para reporte de combustible
    def reporte_combustible(self, capacidad_max):
        litros_faltantes = capacidad_max - self.combustible_litros_litros
        print(f"–> Reporte del depósito de {self.marca} {self.modelo} <–")
        print(f"Combustible actual: {self.combustible_litros} litros")
        print(f"Capacidad máxima: {capacidad_max} litros")
        print(f"Litros faltantes para llenar el depósito: {litros_faltantes} litros")
    
    
    
    
    #Metodo para reponer nafta
    def reponer(self,capacidad_max):
        while True:
            try:
                cantidad_reponer = float(input("Cuantos litros queres reponer?"))
                if cantidad_reponer + self.combustible_litros > capacidad_max:
                    print("No se puede reponer esa cantidad, intentá de nuevo.")
                else:
                    self.combustible_litros += cantidad_reponer
                    print(f"Has repuesto {cantidad_reponer} litros. Combustible actual: {self.combustible_litros} litros.")
                    break
            except ValueError:
                print("Por favor, introducí un número válido.")
                
                
                
# Primera instancia de argumentos posicionales
moto1 = motocicleta("Rojo", "ABC123", 10, 2, "Yamaha", "YZF-R3", "2023-01-15", 190, 170)
moto2 = motocicleta(marca="Honda", modelo="CBR500R", color="Negro", combustible_litros=0, numero_ruedas=2, matricula="DEF456", fecha_fabricacion="2022-06-10", velocidad_punta=180, peso=192)




# Añadir el atributo precio a moto1
#moto1.precio = 7500
#print(f"El precio de la motocicleta '{moto1.marca} {moto1.modelo}' es de {moto1.precio} $.")




#Aañdir el atributo de precio a moto2
#moto2.precio = 6400
#print(f"El precio de la motocicleta '{moto2.marca} {moto2.modelo}' es de {moto2.precio}$.")




# Consultar el precio de ambas motocicletas
#moto1.consultar_precio()  # Moto con precio
#moto2.consultar_precio()  # Moto sin precio

