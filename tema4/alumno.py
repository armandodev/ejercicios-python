from fp.lib import Datos, Formato, Menú

class Alumno:
    def __init__(self, nt):
        obd = Datos()
        self.__cal = [-1 for _ in range(nt)]
        print('Escribe los datos del alumno')
        self.__nc = obd.cadena('No. Control: ')
        self.__nom = obd.cadena('Nombre: ').upper()
        self.__pro = 0
        for i in range(len(self.__cal)):
            while self.__cal[i] < 0 or self.__cal[i] > 100:
                self.__cal[i] = obd.entero(f"Calificación del tema {i + 1}: ")
            self.__pro += self.__cal[i]
        self.__pro //= nt
        
    def mostrar(self):
        obf = Formato()
        print(f"| {obf.der(self.__nc, 11)}", end=' | ')
        print(f"{obf.izq(self.__nom, 30)}", end=' | ')
        for cal in self.__cal:
            print(f"{obf.cen(cal, 5)}", end=' | ')
        print(f"{obf.der(self.__pro, 8)} |")
        
    def titulos(self):
        obf = Formato()
        print(f"| {obf.der('NO. CONTROL', 11)}", end=' | ')
        print(f"{obf.izq('NOMBRE', 30)}", end=' | ')
        for i in range(len(self.__cal)):
            print(f"{obf.cen(f'CAL {i + 1}', 5)}",  end=' | ')
        print(f"{obf.der('PROMEDIO', 8)} |")
        
    def modificar(self):
        op = 0
        obm = Menú('MODIFICACIONES', ['NOMBRE', 'CALIFICACIONES'])
        while op != obm.salir():
            match op := obm.opción():
                case 1:
                    print(f"Nombre actual: {self.__nom}")
                    self.__nom = obm.obd.cadena(f"Nuevo nombre: ").upper()
                case 2:
                    print(f"Calificaciones actuales: {self.__cal}")
                    for i in range(len(self.__cal)):
                        self.__cal[i] = -1
                        while self.__cal[i] < 0 or self.__cal[i] > 100:
                            self.__cal[i] = obm.obd.entero(f"Nueva calificación del tema {i + 1}: ")
                        self.__pro += self.__cal[i]
                    self.__pro /= len(self.__cal)
                    
    def no_control(self):
        return self.__nc
    
    def nombre(self):
        return self.__nom