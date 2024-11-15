from fp.lib import Datos
import random

class Letras:
    def tamaño(self):
        print('Tamaño de la matriz')
        ren = 0
        while ren < 2:
            ren = Datos().entero('No. de renglones: ')
        col = 0
        while col < 2:
            col = Datos().entero('No. de columnas: ')
        return [[chr(random.randint(65, 90)) for _ in range(col)] for _ in range(ren)]
    
    def mostrar(self, mat):
        print('Contenido de la matriz')
        for ren in mat:
            for col in ren:
                print(f"{col}\t", end='')
            print()
    
    def vocales(self, mat):
        voc = [['A', 0], ['E', 0], ['I', 0], ['O', 0], ['U', 0]]
        
        for ren in mat:
            for col in ren:
                for i in voc:
                    if i[0] == col:
                        i[1] += 1
        
        return voc