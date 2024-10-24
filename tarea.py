import random

class Aproximado:
    def tamaño(self):
        self.__tam = 0
        while self.__tam < 1:
            self.__tam = int(input('Ingresa el tamaño del vector: '))
        
    def vector(self):
        self.__vec = [random.randint(1, 100) for _ in range(self.__tam)]
        
    def promedio(self):
        self.__pro = 0
        for i in self.__vec:
            self.__pro += i
        self.__pro //= self.__tam
        
    def aproximado(self):
        for i in range(len(self.__vec)):
            if i == 0:
                self.__aprox = f"{self.__vec[i]} "
                num = self.__vec[i]
                res_acu = (self.__pro - num)
                if res_acu < 0:
                    res_acu *= -1
            else:
                res = (self.__pro - self.__vec[i])
                if res < 0:
                    res = res * -1
                if res < res_acu:
                    self.__aprox = f"{self.__vec[i]} "
                    num = self.__vec[i]
                    res_acu = res
                elif num == self.__vec[i] or res == res_acu:
                    self.__aprox += f"{self.__vec[i]} "
    
    def mostrar(self):
        print('El tamaño del vector es:', self.__tam)
        print('El vector es:', self.__vec)
        print('El promedio es:', self.__pro)
        print('Los números más aproximados al promedio son:', self.__aprox)
                    
def main():
    oba = Aproximado()
    oba.tamaño()
    oba.vector()
    oba.promedio()
    oba.aproximado()
    oba.mostrar()

if __name__ == "__main__":
    main()