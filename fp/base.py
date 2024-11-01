import locale
import datetime

class Datos:
    def entero(self, msj):
        try:
            num = int(input(msj).strip())
        except ValueError:
            num = self.entero(msj)
        return num
    
    def real(self, msj):
        try:
            num = float(input(msj).strip())
        except ValueError:
            num = self.real(msj)
        return num
    
    def cadena(self, msj):
        try:
            cad = input(msj).strip()
            if len(cad) == 0:
                raise ValueError
        except ValueError:
            cad = self.cadena(msj)
        return cad
    
    def carácter(self, msj):
        try:
            char = input(msj).strip()[0]
        except IndexError:
            char = self.carácter(msj)
        return char

class FechaHora:
    def __init__(self):
        locale.setlocale(locale.LC_ALL, 'es_MX.UTF-8')
        self.__ofh = datetime.datetime.now()
        
    def fechal(self):
        return self.__ofh.strftime('%A, %d de %B de %Y')
    
    def fechas(self):
        return self.__ofh.strftime('%d-%m-%Y')
    
    def fechasm(self):
        return self.__ofh.strftime('%d-%b-%Y')
    
    def hora(self):
        return self.__ofh.strftime('%I:%M:%S %p')
    
    def horam(self):
        return self.__ofh.strftime('%H:%M:%S hrs.')
    
    def edad(self, dia, mes, año):
        ofn = datetime.datetime(año, mes, dia)
        
        print(ofn.strftime('%A, %d de %B de %Y'))
        edad = self.__ofh.year - ofn.year
            
        if self.__ofh.month < ofn.month:
            edad -= 1
        elif self.__ofh.month == ofn.month:
            if self.__ofh.day < ofn.day:
                edad -= 1
            
        return edad

class Formato:
    def izq (self, dato, tam):
        return str(dato)[:tam].ljust(tam)
    
    def cen(self, dato, tam):
        return str(dato)[:tam].center(tam)
    
    def der(self, dato, tam):
        return str(dato)[:tam].rjust(tam)
    
    def mon(self, dato):
        return f"$ {dato:,.2f}"

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