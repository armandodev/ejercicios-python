from tema4.formato import Formato
from tema4.datos import Datos

class Producto():
    def __init__(self):
        obd = Datos()
        print('-----Ingresa los datos del producto-----')
        self.__clv = -1
        while self.__clv < 0:
            self.__clv = obd.entero('Clave: ')
        self.__nom = ''
        while self.__nom == '':
            self.__nom = obd.cadena('Nombre: ').capitalize()
        self.__exi = -1
        while self.__exi < 0:
            self.__exi = obd.entero('Existencias: ')
        self.__pre = 0
        while self.__pre < 1:
            self.__pre = obd.real('Precio: ')
            
    def mostrar(self):
        obf = Formato()
        print(obf.der('CLAVE', 6), obf.izq('NOMBRE', 25), obf.izq('EXIST', 5), obf.der('PRECIO', 15), sep=' | ')
        print('| ', obf.der(self.__clv, 6), obf.izq(self.__nom, 25), obf.izq(self.__exi, 5), obf.der(obf.mon(self.__pre), 15), ' |', sep=' | ')