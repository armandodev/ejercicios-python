import locale
import datetime

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