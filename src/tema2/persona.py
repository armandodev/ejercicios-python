class Persona:
    def leer(self):
        self.nombre = input('Ingresa el nombre: ')
        self.edad = input('Ingresa la edad: ')
        self.sexo = input('Ingresa el sexo: ')
    
    def mostrar(self):
        print(f"Nombre: {self.nombre}", f"Edad: {self.edad}", f"Sexo: {self.sexo}", sep='\n')