class Trabajadores():
    def cantidad(self):
        self.__cant = 0
        while self.__cant < 1:
            self.__cant = int(input('Ingresa la cantidad de trabajadores: '))
            
    def __nombre(self):
        print('-' * 20)
        self.__nom = ''
        while len(self.__nom) == 0:
            self.__nom = input(f"Ingresa el nombre del trabajador {self.__i + 1}: ").upper()
            
    def __horas(self):
        self.__hrs = 0
        while self.__hrs < 1:
            self.__hrs = int(input('Ingresa la cantidad de horas trabajadas: '))
            
    def __precio(self):
        self.__pre = 0
        while self.__pre < 1:
            self.__pre = float(input('Ingresa el precio por hora: '))
            
    def calcular(self):
        self.__tsb = 0
        self.__tret = 0
        self.__tnet = 0
        
        for self.__i in range(self.__cant):
            self.__nombre()
            print(f"-----{self.__nom}-----")
            self.__horas()
            self.__precio()
            
            self.__sb = self.__hrs * self.__pre
            self.__fa = self.__sb * 0.06
            self.__seg = self.__sb * 0.08
            self.__isr = self.__sb * 0.15
            self.__ret = self.__fa + self.__seg + self.__isr
            self.__net = self.__sb - self.__ret
            
            self.__tsb += self.__sb
            self.__tret += self.__ret
            self.__tnet += self.__net
            
            self.__mostrar()
        
    def __mostrar(self):
        print(f"Sueldo base:  ${self.__sb:,.2f}", f"Retenciones: -${self.__ret:,.2f}", f"  - Fondo de ahorro: -${self.__fa:,.2f}", f"  - Seguro de vida: -${self.__seg:,.2f}", f"  - ISR: -${self.__isr:,.2f}", f"Sueldo neto:  ${self.__net:,.2f}", sep='\n')
        
    def totales(self):
        print('-----Totales-----', f"Sueldo base:  ${self.__tsb:,.2f}", f"Retenciones: -${self.__tret:,.2f}", f"Sueldo neto:  ${self.__tnet:,.2f}", sep='\n')