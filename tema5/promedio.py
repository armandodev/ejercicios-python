from fp.lib import Datos

class Promedio:
    def cantidad(self):
        can = 0
        while can < 1:
            can = Datos().entero('Cantidad de calificaciones: ')
        return can
    
    def __calificación(self, con, can):
        cal = -1
        while cal < 0 or cal > 100:
            cal = Datos().entero(f"{con}/{can} Calificación: ")
        return cal
    
    def calcular(self, can):
        pro = 0
        for i in range(1, can + 1):
            pro += self.__calificación(i, can)
        return pro // can
    
    def mostrar(self, pro):
        print(f"El promedio del alumno es: {pro}")