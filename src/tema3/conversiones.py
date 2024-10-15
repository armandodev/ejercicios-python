class Conversiones:
    def pulgadas(self):
        self.__pulgadas = float(input('Ingresa la cantidad de pulgadas: '))

    def calcular(self):
        self.__centímetros = self.__pulgadas * 2.54

    def mostrar(self):
        print(f"{self.__pulgadas} pulgadas equivalen a {self.__centímetros}cm")