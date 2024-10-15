class Calificador:
    def calificación(self):
        self.__cal = int(input('Ingresa la calificación: '))
        
    def calcular(self):
            self.__msg = 'Aprobado' if self.__cal >= 70 and self.__cal <= 100 else 'Tienes otra oportunidad'
            
    def mostrar(self):
        print(self.__msg)