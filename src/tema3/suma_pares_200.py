class SumaPares:
    def calcular(self):
        self.__suma = 0
        for i in range(2, 202, + 2):
            self.__suma += i
    
    def mostrar(self):
        print(f"La suma de los pares de 2 a 200 es: {self.__suma}")