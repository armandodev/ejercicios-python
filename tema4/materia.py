from fp.lib import Datos, Formato

class Materia:
    def __init__(self):
        obd = Datos()
        print('-----Datos de la materia-----')
        self.__cv = obd.cadena('Clave: ').upper()
        self.__nom = obd.cadena('Nombre: ').upper()
        self.__cre = 0
        while self.__cre < 2 or self.__cre > 10:
            self.__cre = obd.entero('Creditos: ')
        self.__tem = 0
        while self.__tem < 3 or self.__tem > 7:
            self.__tem = obd.entero('No. Temas: ')
        
    def titulos(self):
        obf = Formato()
        print(f" | {obf.cen('CLAVE', 8)} | {obf.cen('NOMBRE', 25)} | {obf.cen('CREDITOS', 8)} | {obf.cen('TEMAS', 5)} |")
            
    def mostrar(self):
        obf = Formato()
        print(f" | {obf.izq(self.__cv, 8)} | {obf.izq(self.__nom, 25)} | {obf.cen(self.__cre, 8)} | {obf.cen(self.__tem, 5)} |")
        
    def clave(self):
        return self.__cv
    
    def nombre(self):
        return self.__nom