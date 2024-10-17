class MayorMenor:
    def __número(self):
        self.__num = int(input(f"{self.__i + 1}/{self.__can} Ingresa un número: "))
        
    def cantidad(self):
        self.__can = 0
        while self.__can < 1:
            self.__can = int(input('Ingresa la cantidad de números a leer: '))
        
    def calcular(self):
        for self.__i in range (0, self.__can):
            self.__número()
            
            if self.__i == 0:
                self.__me = self.__num
                self.__ma = self.__num

            if self.__num > self.__ma:
                self.__ma = self.__num

            if self.__num < self.__me:
                self.__me = self.__num
                
    def mostrar(self):
        print(f"El número mayor es el: {self.__ma}", f"El número menor es: {self.__me}", sep='\n')