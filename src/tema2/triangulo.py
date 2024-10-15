class Triangulo:
    def leer(self):
        self.base = int(input('Ingresa la base: '))
        self.altura = int(input('Ingresa la altura: '))
        
    def calcular(self):
        self.area = self.base * self.altura / 2
        
    def mostrar(self):
        print(f"La area es: {self.area}")