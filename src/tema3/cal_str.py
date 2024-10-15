class CalStr:
    def calificación(self):
        self.__cal = int(input('Ingresa una calificación numérica: '))
    
    def calcular(self):
        match self.__cal // 10:
            case 10:
                self.__msg = 'A'
            case 9:
                self.__msg = 'B'
            case 8:
                self.__msg = 'C'
            case 7:
                self.__msg = 'D'
            case _:
                self.__msg = 'N/A'
                
    def mostrar(self):
        print(f"La calificación {self.__cal} en letras sería: {self.__msg}")