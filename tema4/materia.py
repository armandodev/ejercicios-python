from fp.base import Datos

class Materia:
    def __init__(self):
        self.__obd = Datos()
                
        self.__clv = 0
        while self.__clv < 1:
            self.__clv = self.__obd.entero("Clave: ")
        self.__