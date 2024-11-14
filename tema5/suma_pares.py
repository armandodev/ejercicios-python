from fp.lib import Datos

class SumaPares:
    def cantidad(self):
        can = 0
        while can < 1:
            can = Datos().entero('Ingresa la cantidad de números: ')
        return can
    
    def __número(self, con, can):
        return Datos().entero(f"{con}/{can} Número: ")
    
    def suma(self, can):
        suma = 0
        for i in range(1, can + 1):
            num = self.__número(i, can)
            if num % 2 == 0:
                suma += num
        return suma
    
    def mostrar(self, suma):
        print(f"La suma es: {suma}")