class Impuestos:
    def precio(self):
        self.__pre = float(input('Ingresa el precio por hora: '))
        
    def horas(self):
        self.__hrs = int(input('Ingresa la cantidad de horas trabajadas:'))
        
    def calcular(self):
        self.__sb = self.__pre * self.__hrs
        self.__ret = 0
        
        if self.__sb > 150:
            self.__ret = (200 * 0.07 + (self.__sb - 350) * 0.16) if self.__sb > 350 else ((self.__sb - 150) * 0.07)
        
        self.__net = self.__sb - self.__ret
        
    def mostrar(self):
        print(f"Sueldo base: ${self.__sb:.2f}", f"Retenciones: ${self.__ret:.2f}", f"Sueldo neto: ${self.__net:.2f}", sep='\n')