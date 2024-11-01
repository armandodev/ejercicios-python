from fp.base import Datos, Formato

class Materias:
    def __init__(self):
        self.__obd = Datos()
        self.__obf = Formato()
        
        self.__clv = self.__obd.cadena("Clave: ").upper()
        self.__nom = self.__obd.cadena("Nombre: ").upper()
        self.__cre = 0
        while self.__cre < 2 or self.__cre > 10:
            self.__cre = self.__obd.entero("Créditos: ")
        self.__tem = self.__obd.entero("Temas: ")
        
    def tamaño(self):
        tam = 0
        while tam < 1:
            tam = self.__obd.entero("Tamaño: ")
            
    def mostrar(self):
        print('| ', self.__obf.izq(self.__clv, 8), self.__obf.izq(self.__nom, 25), self.__obf.cen(self.__cre, 8), self.__obf.cen(self.__tem, 5), ' |', sep=' | ')
        
    def títulos(self):
        print('| ', self.__obf.cen("CLAVE", 8), self.__obf.izq("NOMBRE", 25), self.__obf.cen("CRÉDITOS", 8), self.__obf.cen("TEMAS", 5), ' |', sep=' | ')