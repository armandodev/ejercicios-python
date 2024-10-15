class Trabajador:
    def horas(self):
        self.__hrs = int(input('Ingresa la cantidad de horas trabajadas: '))
    
    def precio(self):
        self.__pre = int(input('Ingresa el precio por hora trabajada: '))
        
    def calcular(self):
        self.__base = self.__hrs * self.__pre
        self.__seguro = self.__base * 0.03
        self.__afore = self.__base * 0.02
        self.__neto = self.__base - self.__seguro - self.__afore
        
    def mostrar(self):
        print(f"Sueldo base: ${self.__base}", f"Costo del seguro: {self.__seguro}", f"Costo del afore: {self.__afore}", f"Sueldo neto: {self.__neto}", sep='\n')