from fp.lib import FechaHora, Datos, Formato, Menú

class Cliente:
    def __init__(self, nc):
        self.__obfh = FechaHora()
        self.__obf = Formato()
        self.__obd = Datos()

        print('-----Ingresa los datos del cliente-----')
        self.__nc = nc
        print(f"No. de cuenta: {self.__nc}")
        self.__nom = self.__obd.cadena('Ingresa el nombre del cliente: ').upper()
        self.__fa = self.__obfh.fecha()
        print(f"Fecha de apertura: {self.__fa}")
        self.__sal = -1
        while self.__sal < 0:
            self.__sal = self.__obd.real('Saldo inicial: $')
    
    def títulos(self):
        print(f"| {self.__obf.der('NO. CUENTA', 10)}", end=' | ')
        print(f"{self.__obf.izq('NOMBRE', 30)}", end=' | ')
        print(f"{self.__obf.cen('APERTURA', 10)}", end=' | ')
        print(f"{self.__obf.der('SALDO', 15)} |", sep=' | ')
    
    def mostrar(self):
        print(f"| {self.__obf.der(self.__nc, 10)}", end=' | ')
        print(f"{self.__obf.izq(self.__nom, 30)}", end=' | ')
        print(f"{self.__obf.cen(self.__fa, 10)}", end=' | ')
        print(f"{self.__obf.der(self.__obf.mon(self.__sal), 15)} |")
    
    def no_cuenta(self):
        return self.__nc
    
    def nombre(self):
        return self.__nom
    
    def saldo(self):
        return self.__sal
    
    def modificar(self):
        obm = Menú('MODIFICACIONES', ['NOMBRE', 'FECHA DE APERTURA', 'SALDO'])
        op = 0
        
        while op != obm.salir():
            match op := obm.opción():
                case 1:
                    print(f"Nombre actual: {self.__nom}")
                    self.__nom = self.__obd.cadena('Nuevo nombre del cliente: ').upper()
                case 2:
                    print(f"Fecha de apertura actual: {self.__fa}")
                    self.__fa = self.__obfh.fecha()
                    print(f"Fecha de apertura actualizada: {self.__fa}")
                case 3:
                    print(f"Saldo actual: {self.__obf.mon(self.__sal)}")
                    self.__sal = -1
                    while self.__sal < 0:
                        self.__sal = self.__obd.real('Nuevo saldo: ')
            
    def movimiento(self, monto):
        self.__sal += monto