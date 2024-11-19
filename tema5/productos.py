from fp.lib import Datos

class Productos:
    def __init__(self):
        can = 0
        while can < 1:
            can = Datos().entero('Cantidad maxima de productos: ')
        self.__lp = [None for _ in range(can)]
    
    def nuevo(self):
        pass
    
    def lista(self):
        pass
    
    def buscar(self):
        pass
    
    def modificar(self):
        pass
    
    def borrar(self):
        pass
    
    def compra(self):
        pass
    
    def venta(self):
        pass