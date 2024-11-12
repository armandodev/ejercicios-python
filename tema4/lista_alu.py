from fp.lib import Datos
from tema4.alumno import Alumno

class ListaAlu:
    def __init__(self):
        self.__obd = Datos()
        
        tam = 0
        while tam < 1:
            tam = self.__obd.entero('Cantidad de alumnos: ')
        self.__nt = 0
        while self.__nt < 1 or self.__nt > 7:
            self.__nt = self.__obd.entero('No. de temas: ')
        self.__lista = [None for _ in range(tam)]
        self.__pos = -1
        
    def nueva(self):
        if self.__pos + 1 < len(self.__lista):
            self.__pos += 1
            self.__lista[self.__pos] = Alumno(self.__nt)
        else:
            print('No hay espacio para otro alumno...')
            
    def mostrar(self):
        if self.__pos != -1:
            print('\nLista de alumnos...')
            self.__lista[0].titulos()
            for i in range(self.__pos + 1):
                self.__lista[i].mostrar()
            print('Fin de la lista...')
        else:
            print('No hay alumnos registrados...')
            
    def buscar(self):
        if self.__pos != -1:
            nom = self.__obd.cadena('Nombre o apellido del alumno a buscar: ').upper()
            ban = True
            
            for i in range(self.__pos + 1):
                if nom in self.__lista[i].nombre():
                    if ban:
                        print('Alumno encontrado...')
                        self.__lista[i].titulos()
                        ban = False
                    self.__lista[i].mostrar()
            if ban:
                print(f"El alumno con nombre o apellido \"{nom}\", no existe...")
        else:
            print('No hay alumnos registrados...')
            
    def modificar(self):
        if self.__pos != -1:
            nc = self.__obd.cadena('No. de control del alumno: ')
            ban = True
            
            for i in range(self.__pos + 1):
                if self.__lista[i].no_control() == nc:
                    self.__lista[i].modificar()
                    ban = False
                    break
            if ban:
                print(f"El alumno con no. control {nc}, no existe...")
        else:
            print('No hay alumnos registrados...')