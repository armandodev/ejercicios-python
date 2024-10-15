class Suma50:
    def calcular(self):
        self.__suma = 0
        i = 1
        while i <= 50:
            self.__suma += i
            i += 1

    def mostrar(self):
        print(f"La suma de los primeros 50 números naturales es: {self.__suma}")