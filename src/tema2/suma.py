class Suma:
    def leer(self):
        self.a = input('Ingrese el primer número: ')
        self.b = input('Ingrese el segundo número: ')
        
    def calcular(self):
        self.res = int(self.a) + int(self.b)
        
    def mostrar(self):
        print(f"El resultado es: {self.res}")