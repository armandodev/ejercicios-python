class Datos:
    def entero(self, msj):
        try:
            num = int(input(msj).strip())
        except ValueError:
            num = self.entero(msj)
        return num
    
    def real(self, msj):
        try:
            num = float(input(msj).strip())
        except ValueError:
            num = self.real(msj)
        return num
    
    def cadena(self, msj):
        try:
            cad = input(msj).strip()
            if len(cad) == 0:
                raise ValueError
        except ValueError:
            cad = self.cadena(msj)
        return cad
    
    def carácter(self, msj):
        try:
            char = input(msj).strip()[0]
        except IndexError:
            char = self.carácter(msj)
        return char