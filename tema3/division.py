class Division:
    def leer(self):
        self.__a = int(input('Ingresa el primer número: '))     
        self.__b = int(input('Ingresa el segundo número: '))
        
    def calcular(self):
        self.__res = self.__a / self.__b
        
    def mostrar(self):
        if self.__res > 5:
            print(f"El resultado es: {self.__res}")