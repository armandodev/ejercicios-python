from fp.lib import Datos

class Multiplicación:
    def números(self):
        a = Datos().entero('Ingresa el primer número: ')
        b = Datos().entero('Ingresa el segundo número: ')
        
        return a, b
    
    def multiplicar(self, a, b):
        return a * b
    
    def mostrar(self, res):
        print(f"El resultado del producto es: {res}")