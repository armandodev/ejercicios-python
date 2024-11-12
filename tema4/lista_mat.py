from fp.lib import Datos
from tema4.materia import Materia

class ListaMat:
    def __init__(self):
        self.__obd = Datos()
        
        tam = 0
        while tam < 1:
            tam = self.__obd.entero('Tamaño de la lista de materias: ')
        self.__lista = [None for _ in range(tam)]
        self.__pos = -1
        
    def nueva(self):
        if self.__pos + 1 < len(self.__lista):
            mat = Materia()
            self.__pos += 1
            self.__lista[self.__pos] = mat
        else:
            print('No hay espacio para otra materia...')
            
    def lista(self):
        if self.__pos != -1:
            print('\nLista de materias...')
            self.__lista[0].titulos()
            for i in range(self.__pos + 1):
                self.__lista[i].mostrar()
            print('Fin de la lista...')
        else:
            print('No hay materias registradas...')
            
    def buscar(self):
        if self.__pos != -1:
            clv = self.__obd.cadena('Clave de la materia a buscar: ').upper()
            ban = True
            
            for i in range(self.__pos + 1):
                if self.__lista[i].clave() == clv:
                    print('Materia encontrada...')
                    self.__lista[i].titulos()
                    self.__lista[i].mostrar()
                    ban = False
                    break
            if ban:
                print(f"La materia con clave {clv}, no existe...")
        else:
            print('No hay materias registradas...')
            
    def buscar_nom(self):
        if self.__pos != -1:
            nom = self.__obd.cadena('Nombre de la materia a buscar: ').upper()
            ban = True
            
            for i in range(self.__pos + 1):
                if nom in self.__lista[i].nombre():
                    if ban:
                        print('Materias encontradas...')
                        self.__lista[i].titulos()
                        ban = False
                    self.__lista[i].mostrar()
            if ban:
                print(f"La materia con nombre \"{nom}\", no existe...")
        else:
            print('No hay materias registradas...')