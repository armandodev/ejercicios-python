class Par:
    def numero(self):
        self.__a = int(input('Ingresa el número: '))
        
    def mostrar(self):
        if self.__a % 2 == 0:
            print(f"El número {self.__a} es par")