class Edad:
    def leer(self):
        self.__año_actual = int(input('Ingresa el años actual: '))
        self.__año_nac = int(input('Ingresa tu año de nacimiento: '))
        
    def calcular(self):
        self.__edad = self.__año_actual - self.__año_nac
        
    def mostrar(self):
        print(f"La edad al terminar el año actual es {self.__edad}")