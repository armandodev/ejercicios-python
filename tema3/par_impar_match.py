class ParImparMatch:
    def número(self):
        self.__cal = int(input('Ingresa un número de 1 - 10: '))
        
    def calcular(self):
        match self.__cal:
            case 1 | 3 | 5 | 7 | 9:
                self.__msg = 'Impar'
            case 2 | 4 | 6 | 8 | 10:
                self.__msg = 'Par'
            case _:
                self.__msg = 'Número fuera de rango'
                
    def mostrar(self):
        print(self.__msg)