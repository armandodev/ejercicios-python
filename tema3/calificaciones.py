class Calificaciones:
    def leer(self):
        self.__c1 = int(input('Ingresa la primera calificación: '))
        self.__c2 = int(input('Ingresa la segunda calificación: '))
        self.__c3 = int(input('Ingresa la tercera calificación: '))
        
    def calcular(self):
        if self.__c1 >= 70 and self.__c2 >= 70 and self.__c3 >= 70:
            self.__prom = (self.__c1 + self.__c2 + self.__c3) / 3
            self.__mostrar()
            
    def __mostrar(self):
        print(f"El promedio de las 3 calificaciones es: {self.__prom:.0f}")