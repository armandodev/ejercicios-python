class Mayor:
    def números(self):
        self.__num1 = int(input('Ingresa el primer número: '))
        self.__num2 = int(input('Ingresa el segundo número: '))
        self.__num3 = int(input('Ingresa el tercer número: '))
        
    def calcular(self):
        if self.__num1 > self.__num2 and self.__num1 > self.__num3:
            self.__may = self.__num1
        elif self.__num2 > self.__num3:
            self.__may = self.__num2
        else:
            self.__may = self.__num3
            
    def mostrar(self):
        print(f"El número mayor es {self.__may}")