class Promedio10:
    def __calificación(self):
        self.__cal = 0
        while self.__cal <= 0 or self.__cal > 100:
            self.__cal = int(input(f"{self.__i}/10 Ingresa una calificación: "))
            
    def calcular(self):
        self.__i = 1
        pro = 0
        cant = 0
        
        while self.__i <= 10:
            self.__calificación()
            
            if self.__cal >= 70:
                pro += self.__cal
                cant += 1
            
            self.__i += 1
                
        if pro != 0 and cant != 0:
            pro /= cant
            self.__msj = f"Se tomaron en cuenta {cant} calificaciones y el promedio es: {pro:.0f}"
        else:
            self.__msj = 'No hay calificaciones aprobatorias'
            
        self.__mostrar()
            
    def __mostrar(self):
        print(self.__msj)