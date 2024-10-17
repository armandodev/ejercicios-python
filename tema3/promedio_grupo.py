class PromedioGrupo:
    def unidades(self):
        self.__cant_u = 0
        while self.__cant_u < 1 or self.__cant_u > 8:
            self.__cant_u = int(input('Ingresa la cantidad de unidades evaluadas: '))
            
    def alumnos(self):
        self.__cant_a = 0
        while self.__cant_a < 1:
            self.__cant_a = int(input('Ingresa la cantidad de alumnos del salón: '))
            
    def __calificación(self):
        self.__cal = -1
        while self.__cal < 0 or self.__cal > 100:
            self.__cal = int(input(f"{self.__con + 1}/{self.__cant_u} Ingresa la calificación: "))
            
    def calcular(self):
        self.__pro_g = 0
        
        for i in range (0, self.__cant_a):
            print(f"-----Alumno {i + 1}-----")
            self.__pro = 0
            
            for self.__con in range (0, self.__cant_u):
                self.__calificación()
                self.__pro += self.__cal
                
            self.__pro /= self.__cant_u
            self.__pro_g += self.__pro
            self.__promedio()
            
        self.__pro_g /= self.__cant_a
        
    def __promedio(self):
        print(f"Tu promedio es: {self.__pro}")
        
    def general(self):
        print(f"-----El promedio general es de: {self.__pro_g}-----")