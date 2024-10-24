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
        
    def tamaño_3(self):
        print('-----Tamaño de las matrizes-----')
        ren = 0
        col = 0
        while ren < 2 or col < 2:
            ren = int(input('Ingresa la cantidad de renglones: '))
            col = int(input('Ingresa la cantidad de columnas: '))
        self.__mat_1 = [[random.randint(1, 10) for _ in range(col)] for _ in range(ren)]
        self.__mat_2 = [[random.randint(1, 10) for _ in range(col)] for _ in range(ren)]
        self.__mat_3 = [[0 for _ in range(col)] for _ in range(ren)]
                
    def aleatorios_3(self):
        for ren in range(len(self.__mat_1)):
            for col in range(len(self.__mat_1[0])):
                self.__mat_1[ren][col] = random.randint(1, 10)
                self.__mat_2[ren][col] = random.randint(1, 10)
                
    def suma_3(self):
        for ren in range(len(self.__mat_1)):
            for col in range(len(self.__mat_1[0])):
                self.__mat_3[ren][col] = self.__mat_1[ren][col] + self.__mat_2[ren][col]
                
    def multiplicación_3(self):
        for ren in range(len(self.__mat_1)):
            for col in range(len(self.__mat_1[0])):
                for k in range(len(self.__mat_1)):
                    self.__mat_3[ren][col] += self.__mat_1[ren][k] * self.__mat_2[k][col]
                
    def mostrar_3(self):
        print('-----Matriz 1-----')
        for ren in range(len(self.__mat_1)):
            for col in range(len(self.__mat_1[0])):
                print(f"{self.__mat_1[ren][col]}\t", end='')
            print()
            
        print('-----Matriz 2-----')
        for ren in range(len(self.__mat_2)):
            for col in range(len(self.__mat_2[0])):
                print(f"{self.__mat_2[ren][col]}\t", end='')
            print()
            
        print('-----Matriz 3-----')
        for ren in range(len(self.__mat_3)):
            for col in range(len(self.__mat_3[0])):
                print(f"{self.__mat_3[ren][col]}\t", end='')
            print()

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
        ma = 0
        me = self.__mat[0][0]
        for ren in range(len(self.__mat)):
            for col in range(len(self.__mat[0])):
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
        
    def cantidad(self):
        can = 1
        while can < 2:
            can = int(input('Ingresa la cantidad de alumnos: '))
        self.__mat = [[0 for _ in range(3)] for _ in range(can)]
            
    def alumnos(self):
        for i in self.__mat:
            i[0] = input('Número de control: ')
            i[1] = input('Nombre: ').upper()
            i[2] = input('Promedio: ')