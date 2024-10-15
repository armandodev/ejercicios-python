class Factorial:
    def número(self):
        self.__a = -1
        while self.__a < 0:
            self.__a = int(input('Ingresa un número: '))
                
    def calcular(self):
        self.__res = 1
        i = 2
        while i <= self.__a:
            self.__res *= i
            i += 1
            
    def mostrar(self):
        print(f"El factorial del número {self.__a} es: {self.__res}")