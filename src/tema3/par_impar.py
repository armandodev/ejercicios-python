class ParImpar:
    def numero(self):
        self.__num = int(input('Ingresa el número: '))
                         
    def calcular(self):
        self.__msg = 'Numero par' if self.__num % 2 == 0 else 'Numero impar'
            
    def mostrar(self):
        print(self.__msg)