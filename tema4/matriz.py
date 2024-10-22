import random

class Matriz:
    def tamaño(self):
        print('-----Tamaño de la matriz-----')
        ren = 0
        col = 0
        while ren < 2 or col < 2:
            ren = int(input('Ingresa la cantidad de renglones: '))
            col = int(input('Ingresa la cantidad de columnas: '))
            self.__mat = [[0 for _ in range(col)] for _ in range(ren)]
        
    def aleatorios(self):
        for ren in range(len(self.__mat)):
            for col in range(len(self.__mat[0])):
                self.__mat[ren][col] = random.randint(1, 59)
                
    def rango(self):
        print('-----Rango-----')
        ini = 0
        fin = -1
        while fin < ini:
            ini = int(input('Desde: '))
            fin = int(input('Hasta: '))
        for ren in range(len(self.__mat)):
            for col in range(len(self.__mat[0])):
                self.__mat[ren][col] = random.randint(ini, fin)
    
    def valores(self):
        self.__mat = [[0 for _ in range(5)] for _ in range(5)]
        print(f"Escribe los {len(self.__mat) * len(self.__mat[0])} valores de la matriz: ")
        
        for ren in range(len(self.__mat)):
            for col in range(len(self.__mat[0])):
                self.__mat[ren][col] = int(input(f"[{ren + 1}][{col + 1}] = "))
                
    def mostrar(self):
        print('-----Matriz-----')
        
        for ren in range(len(self.__mat)):
            for col in range(len(self.__mat[0])):
                print(f"{self.__mat[ren][col]}\t", end='')
            print()
            
    def mayor_menor(self):
        for ren in range(len(self.__mat)):
            for col in range(len(self.__mat[0])):
                if ren == 0 and col == 0:
                    ma = 0
                    me = self.__mat[ren][col]
                if self.__mat[ren][col] < me:
                    me = self.__mat[ren][col]
                if self.__mat[ren][col] > ma:
                    ma = self.__mat[ren][col]

        print('-----Número mayor y menor-----')
        print(f"Mayor: {ma}\nMenor: {me}")
        
    def buscar(self):
        print('-----Buscar-----')
        num = int(input('Ingresa el número que quieras buscar: '))
        ban = True
        for ren in range(len(self.__mat)):
            for col in range(len(self.__mat[0])):
                if self.__mat[ren][col] == num:
                    if ban:
                        print('Número encontrado en las posiciones: ')
                        ban = False
                    print(f"({ren}, {col})")
        if ban:
            print('No se han encontrado coincidencias')
            
    def suma(self):
        suma = 0
        
        for ren in range(len(self.__mat)):
            for col in range(len(self.__mat[0])):
                suma += self.__mat[ren][col]
        
        print('-----Suma-----')
        print(f"La suma de todos los elementos del arreglo es: {suma}")
            
    def promedio(self):
        pro = 0
        
        for ren in range(len(self.__mat)):
            for col in range(len(self.__mat[0])):
                pro += self.__mat[ren][col]
                
        pro /= len(self.__mat) * len(self.__mat[0])
        
        print('-----Promedio-----')
        print(f"El promedio de todos los elementos del arreglo es: {pro:.0f}")