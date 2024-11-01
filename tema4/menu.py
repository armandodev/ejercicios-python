from tema4.datos import Datos

class Menú:
    def __init__(self, titulo = 'MENÚ PRINCIPAL', opciones=None):
        self.__titulo = titulo.upper()
        self.__opciones = ['' for _ in range(len(opciones) + 1)]
        for i in range(len(opciones)):
            self.__opciones[i] = opciones[i].upper()
        self.__opciones[i + 1] = 'SALIR'
        
    def __mostrar(self):
        print(f"-----{self.__titulo}-----")
        for i in range(len(self.__opciones)):
            print(f"  {i + 1}) {self.__opciones[i]}")
            
    def opcion(self):
        obd = Datos()
        op = 0
        while op < 1 or op > len(self.__opciones):
            self.__mostrar()
            op = obd.entero('SELECCIONA UNA OPCIÓN: ')
        return op
    
    def salir(self):
        return len(self.__opciones)