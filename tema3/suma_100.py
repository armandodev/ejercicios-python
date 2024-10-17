class Suma100:
    def calcular(self):
        self.__suma = 0
        for i in range (1, 101):
            self.__suma += i
            
    def mostrar(self):
        print(f"La suma de los números del 1 al 100 es: {self.__suma}")