import math

class Circulo:
    def radio(self):
        self.__radio = float(input('Ingresa el radio del circulo: '))
        
    def calcular(self):
        self.__area = math.pi * self.__radio ** 2
        
    def mostrar(self):
        print(f"El area de la circunferencia con radio {self.__radio} es: {self.__area}")