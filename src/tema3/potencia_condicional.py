class PotenciaCondicional:
    def leer(self):
        self.__a = int(input('Ingrese un numero: '))
        
    def calcular(self):
        if self.__a >= 0:
            self.__a2 = self.__a ** 2
            self.__a3 = self.__a ** 3
            self.__mostrar()
        
    def __mostrar(self):
        print(f"El cuadrado del número {self.__a} es {self.__a2} y el cubo del mismo es {self.__a3}")