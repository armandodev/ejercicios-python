class FactorialFor:
    def número(self):
        self.__a = -1
        while self.__a < 0:
            self.__a = int(input('Ingresa un número: '))
                
    def calcular(self):
        self.__res = 1
        for i in range(2, self.__a + 1):
            self.__res *= i
            
    def mostrar(self):
        print(f"El factorial del número {self.__a} es: {self.__res}")