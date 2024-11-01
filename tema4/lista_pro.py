from tema4.producto import Producto

class ListaPro():
    def __init__(self):
        tam = 0
        while tam < 1:
            tam = int(input('Tamaño de la lista: '))
            
        self.__lista = [0 for _ in range(tam)]
        self.__ind = -1
        
    def nuevo(self):
        if self.__ind < len(self.__lista):
            self.__ind += 1
            self.__lista[self.__ind] = Producto()
        else:
            '-----No hay espacio para otro producto-----'
            
    def mostrar(self):
        if self.__ind != -1:
            print('-----Lista de productos-----')
            for i in range(self.__ind + 1):
                self.__lista[i].mostrar()
        else:
            print('-----Lista de productos vacia-----')