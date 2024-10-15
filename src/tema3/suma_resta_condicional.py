class SumaRestaCondicional:
    def números(self):
        self.__a = int(input('Ingresa el primer numero: '))
        self.__b = int(input('Ingresa el segundo numero: '))
        
    def calcular(self):
        if self.__a > 10 and self.__b > 10:
            self.__msg = f"La resta de ambos números es igual a {self.__a - self.__b}"
        else:
            self.__msg = f"La suma de ambos números es igual a {self.__a + self.__b}"
            
    def mostrar(self):
        print(self.__msg)