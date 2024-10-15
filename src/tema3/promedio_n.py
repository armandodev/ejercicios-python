class PromedioN:
    def cantidad(self):
        self.__can = 0
        while self.__can < 1:
            self.__can = int(input('Ingresa la cantidad de números a promediar: '))
            
    def __número(self):
        self.__num = float(input(f"{self.__i + 1}/{self.__can} Ingresa un número: "))
        
    def calcular(self):
        self.__pro = 0
        for self.__i in range(0, self.__can):
            self.__número()
            self.__pro += self.__num
        self.__pro /= self.__can
        
    def mostrar(self):
        print(f"El promedio de los números es: {self.__pro:.2f}")