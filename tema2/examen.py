class Examen:
    def venta(self):
        while True:
            self.dep = float(input(f"Ingrese el precio de la venta del mes n° {self.i}: "))
            if self.dep > 0:
                break
            else:
                print('El precio debe ser positivo')
                
    def calcular(self):
        self.may = 0.0
        self.mes = 0
        for self.i in range(1, 13):
            self.venta()
            if self.dep > self.may:
                self.may = self.dep
                self.mes = self.i

    def mostrar(self):
        print(f"El precio más alto de la venta fue en el mes número {self.mes} con un precio de {self.may}")