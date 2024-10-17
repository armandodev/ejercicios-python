class Tablas:
    def calcular(self):
        for self.__tabla in range (1, 11):
            print(f"\n-----Tabla del {self.__tabla}-----")
            for self.__i in range (1, 11):
                self.__mostrar()
    
    def __mostrar(self):
        print(f"{self.__tabla} * {self.__i} = {self.__i * self.__tabla}")