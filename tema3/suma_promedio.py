class SumaPromedio:
    def cantidad(self):
        self.__cant = 0
        while self.__cant < 1:
            self.__cant = int(input('Ingresa la cantidad de números que se van a leer: '))
            
    def __número(self):
        self.__a = int(input(f"{self.__i}.- Escribe un número: "))
        
    def calcular(self):
        self.__i = 1
        self.__suma = 0
        self.__media = 0
        con = 0
        
        while self.__i <= self.__cant:
            self.__número()
            if self.__a >= 0:
                self.__suma += self.__a
            else:
                self.__media += self.__a
                con += 1
            self.__i += 1
        
        if con != 0:
            self.__media /= con
            
    def mostrar(self):
        print(f"La suma de los números positivos fue: {self.__suma}", f"La media de los números negativos fue: {self.__media:.2f}", sep='\n')