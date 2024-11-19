from fp.lib import Datos
import random

class ProductoMatriz:
    def tamaño(self):
        print('Tamaño de la matriz')
        ren = 0
        while ren < 2:
            ren = Datos().entero('No. de renglones: ')
        col = 0
        while col < 2:
            col = Datos().entero('No. de columnas: ')
        return ren, col
    
    def rango(self, ren, col):
        print('Rango de números')
        ini = 0
        fin = -1
        while ini > fin:
            ini = Datos().entero('Inicio: ')
            fin = Datos().entero('Fin: ')
        return [[random.randint(ini, fin) for _ in range(col)] for _ in range(ren)]
    
    def mostrar(self, mat):
        print('Contenido de la matriz')
        for ren in mat:
            for col in ren:
                print(f"{col}\t", end='')
            print()
            
    def ordenar(self, mat):
        elementos = [elemento for fila in mat for elemento in fila]
        
        for _ in range(len(elementos)):
            ban = True
            for i in range(len(elementos) - 1):
                if elementos[i] > elementos[i + 1]:
                    elementos[i], elementos[i + 1] = elementos[i + 1], elementos[i]
                    ban = False
            if ban:
                break
    
    def producto(self, mat1, mat2, mat3):
        for ren in range(len(mat3)):
            for col in range(len(mat3[0])):
                for i in range(len(mat2)):
                    mat3[ren][col] += mat1[ren][i] * mat2[i][col]