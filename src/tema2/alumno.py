class Alumno:
    def leer(self):
        self.no_control = input('Ingresa el número de control: ')
        self.nombre = input('Ingresa la nombre: ')
        self.promedio = input('Ingresa el promedio: ')
    
    def mostrar(self):
        print(f"No. control: {self.no_control}", f"Nombre: {self.nombre}", f"Promedio: {self.promedio}", sep='\n')