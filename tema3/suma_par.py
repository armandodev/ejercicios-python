class SumaPar:
    def calcular(self):
        self.__suma = 0
        i = 2
        while i <= 50:
            self.__suma += i
            i += 2
    
    def mostrar(self):
        print(f"La suma de los primeros 50 números pares es: {self.__suma}")