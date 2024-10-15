class Promedio:
    def leer(self):
        self.c1 = int(input('Ingresa la primera calificación: '))
        self.c2 = int(input('Ingresa la segunda calificación: '))
        self.c3 = int(input('Ingresa la tercera calificación: '))
        
    def calcular(self):
        self.prom = (self.c1 + self.c2 + self.c3) / 3
        
    def mostrar(self):
        print(f"El promedio de las 3 calificaciones ingresadas es {self.prom:.2f}")