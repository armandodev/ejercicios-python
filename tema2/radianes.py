class Radianes:
    def angulo(self):
        self.__ángulo = float(input('Ingresa el ángulo: '))
        
    def calcular(self):
        self.__radianes = self.__ángulo * (3.1416 / 180)
        
    def mostrar(self):
        print(f"El ángulo es de {self.__ángulo} grados y el valor en radianes es {self.__radianes:.2f}")