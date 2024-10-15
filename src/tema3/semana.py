class Semana:
    def número(self):
        self.__a = int(input('Ingresa un número: '))
        
    def calcular(self):
        match self.__a:
            case 1:
                self.__día = 'Domingo'
            case 2:
                self.__día = 'Lunes'
            case 3:
                self.__día = 'Martes'
            case 4:
                self.__día = 'Miércoles'
            case 5:
                self.__día = 'Jueves'
            case 6:
                self.__día = 'Viernes'
            case 7:
                self.__día = 'Sabado'
            case _:
                self.__día = 'Número fuera de rango'
                
    def mostrar(self):
        print(self.__día)