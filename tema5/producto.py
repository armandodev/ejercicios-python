from tema5.get_set_pro import GetSetPro
from fp.lib import Datos, Formato, Menú

class Producto:
    def __init__(self, clv):
        self.__obd = Datos()
        self.__obf = Formato()
        self.__pro = GetSetPro()
        print('Escribe los datos del producto')
        self.__pro.set_clave(clv)
        print(f"Clave: {clv}")
        self.__pro.set_nombre(self.__obd.cadena('Ingresa el nombre del producto: ').upper())
        self.__pro.set_precio(0)
        while self.__pro.get_precio() < 1:
            self.__pro.set_precio(self.__obd.entero('Ingresa el precio: '))
        self.__pro.set_existencia(-1)
        while self.__pro.get_existencia() < 0:
            self.__pro.set_existencia(self.__obd.entero('Ingresa las existencias: '))
            
    def títulos(self):
        print(f"{self.__obf.cen('CLAVE', 6)}", end=' ')
        print(f"{self.__obf.izq('NOMBRE', 25)}", end=' ')
        print(f"{self.__obf.der('PRECIO', 15)}", end=' ')
        print(f"{self.__obf.der('EXISTENCIAS', 6)}", end=' \n')
            
    def mostrar(self):
        print(f"{self.__obf.cen(self.__pro.get_clave(), 6)}", end=' ')
        print(f"{self.__obf.izq(self.__pro.get_nombre(), 25)}", end=' ')
        print(f"{self.__obf.der(self.__obf.mon(self.__pro.get_precio()), 15)}", end=' ')
        print(f"{self.__obf.der(self.__pro.get_existencia(), 6)}", end=' \n')
        
    def clave(self):
        return self.__pro.get_clave()
    
    def nombre(self):
        return self.__pro.get_nombre()
    
    def modificar(self):
        op = 0
        obm = Menú('MODIFICAR', ['NOMBRE', 'PRECIO', 'EXISTENCIA'])
        while op != obm.salir():
            match op := obm.opción():
                case 1:
                    print(f"Nombre actual: {self.__pro.get_nombre()}")
                    self.__pro.set_nombre(self.__obd.cadena('Ingresa el nuevo nombre: ').upper())
                case 2:
                    print(f"Precio actual: {self.__obf.mon(self.__pro.get_precio())}")
                    self.__pro.set_precio(0)
                    while self.__pro.get_precio() < 1:
                        self.__pro.set_precio(self.__obd.entero('Ingresa el precio: '))
                case 3:
                    print(f"Existencias actuales: {self.__pro.get_existencia()}")
                    self.__pro.set_existencia(-1)
                    while self.__pro.get_existencia() < 0:
                        self.__pro.set_existencia(self.__obd.entero('Ingresa las existencias: '))