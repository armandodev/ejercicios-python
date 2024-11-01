# Construir un arreglo asignarle valores, presentarlo y mostrar
# los elementos de la diagonal principal o el mensaje que indique
# que la matriz no tiene diagonal
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
            
    def tamañop(self):
        print('-----Tamaño de las matrizes-----')
        ren_1 = 0
        col_1 = 0
        ren_2 = 0
        col_2 = 0
        while ren_1 < 2 or col_1 < 2 or ren_2 < 2 or col_2 < 2:
            print('-----Primera Matriz-----')
            ren_1 = int(input('Ingresa la cantidad de renglones: '))
            col_1 = int(input('Ingresa la cantidad de columnas: '))
            print('-----Segunda Matriz-----')
            ren_2 = int(input('Ingresa la cantidad de renglones: '))
            col_2 = int(input('Ingresa la cantidad de columnas: '))
        self.__mat_1 = [[0 for _ in range(col_1)] for _ in range(ren_1)]
        self.__mat_2 = [[0 for _ in range(col_2)] for _ in range(ren_2)]
        self.__mat_3 = [[0 for _ in range(col_2)] for _ in range(ren_1)]
                
    def aleatoriosp(self):
        for ren in range(len(self.__mat_1)):
            for col in range(len(self.__mat_1[0])):
                self.__mat_1[ren][col] = random.randint(1, 10)
        for ren in range(len(self.__mat_2)):
            for col in range(len(self.__mat_2[0])):
                self.__mat_2[ren][col] = random.randint(1, 10)
                
    def multiplicación_3(self):
        for ren in range(len(self.__mat_3)):
            for col in range(len(self.__mat_3[0])):
                for i in range(len(self.__mat_2)):
                    self.__mat_3[ren][col] += self.__mat_1[ren][i] * self.__mat_2[i][col]
                
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
            
    def diagonal(self):
        print('-----Diagonal-----')
        if len(self.__mat) == len(self.__mat[0]):
            for ren in range(len(self.__mat)):
                print(f"{self.__mat[ren][ren]}", end=' ')
        else:
            print("La matriz no tiene diagonal")
            
    def par_impar(self):
        con = 0
        for ren in self.__mat:
            for col in ren:
                if col % 2 == 0:
                    con += 1
        self.__par = [0 for _ in range(con)]
        self.__imp = [0 for _ in range(len(self.__mat) * len(self.__mat[0]) - con)]
        
        pos_p = 0
        pos_i = 0
        for ren in self.__mat:
            for col in ren:
                if col % 2 == 0:
                    self.__par[pos_p] = col
                    pos_p += 1
                else:
                    self.__imp[pos_i] = col
                    pos_i += 1
                    # Construir una matriz y llenarlo de elementos aleatorios en donde
                    # ningun elemento puede estar repetido, posteriormente ordenelo y presentelo
        
    def mostrarv(self):
        print('-----Números pares-----')
        print(self.__par)
        print('-----Números impares-----')
        print(self.__imp)
        
    def aleatorios_nr(self):
        fin = 25
        
        for ren in range(len(self.__mat)):
            for col in range(len(self.__mat[ren])):
                ban = True
                while ban:
                    num = random.randint(1, fin)
                    
                    banRep = False
                    for i in range(ren + 1):
                        for j in range(len(self.__mat[0])):
                            if self.__mat[i][j] == num:
                                banRep = True
                                break
                        if banRep:
                            break
                    
                    if not banRep:
                        self.__mat[ren][col] = num
                        ban = False
    def ordenar(self):
        elementos = [elemento for fila in self.__mat for elemento in fila]
        
        n = len(elementos)
        for _ in range(n):
            cambio = False
            for i in range(n - 1):
                if elementos[i] > elementos[i + 1]:
                    elementos[i], elementos[i + 1] = elementos[i + 1], elementos[i]
                    cambio = True
            if not cambio:
                break
        
        filas = len(self.__mat)
        columnas = len(self.__mat[0])
        for i in range(filas):
            for j in range(columnas):
                self.__mat[i][j] = elementos[i * columnas + j]