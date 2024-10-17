class Trabajador:
    def horas(self):
        self.hrs = int(input('Ingresa el número de horas trabajadas: '))
        
    def precio(self):
        self.pre = float(input('Ingresa el precio de cada hora trabajadas: '))
        
    def calcular(self):
        self.sub = self.pre * self.hrs
        self.seg = self.pre * .03
        self.fon = self.pre * .02
        self.tot = self.pre - self.seg - self.fon
        
    def mostrar(self):
        print(f"El sueldo base es: ${self.sub}", f"El pago al seguro de vida es: ${self.seg}", f"El pago al fondo de ahorro es: ${self.fon}", f"El sueldo total es: ${self.tot}", sep='\n')