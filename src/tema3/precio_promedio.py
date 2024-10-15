class PrecioPromedio:
    def __precio(self):
        self.__pre = 0
        while self.__pre < 1:
            self.__pre = float(input('Ingresa el precio: '))
            
    def calcular(self):
        self.__pro = 0
        con = 1
        
        while con <= 6:
            self.__precio()
            self.__pro += self.__pre
            con += 1
            
        self.__pro /= 6
        
    def mostrar(self):
        print(f"El precio promedio es: {self.__pro:.2f}")