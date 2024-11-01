class Formato:
    def izq (self, dato, tam):
        return str(dato)[:tam].ljust(tam)
    
    def cen(self, dato, tam):
        return str(dato)[:tam].center(tam)
    
    def der(self, dato, tam):
        return str(dato)[:tam].rjust(tam)
    
    def mon(self, dato):
        return f"$ {dato:,.2f}"