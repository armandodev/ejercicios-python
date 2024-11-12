from fp.lib import Datos, Formato
from tema4.cliente import Cliente

class Banco:
    def __init__(self):
        self.__obd = Datos()
        self.__obf = Formato()
        
        tam = 0
        while tam < 1:
            tam = self.__obd.entero('Cantidad total de cuentas: ')
        self.__lista = [None for _ in range(tam)]
        self.__cc = -1
        
    def __no_cuenta(self):
        nc = 0
        if self.__cc != -1:
            nc = self.__lista[self.__cc].no_cuenta()
        return nc + 1
    
    def nueva(self):
        print('-----Nueva cuenta-----')
        if self.__cc + 1 < len(self.__lista):
            cue = Cliente(self.__no_cuenta())
            self.__cc += 1
            self.__lista[self.__cc] = cue
        else:
            print('No hay espacio para otra cuenta...')
            
    def mostrar(self):
        if self.__cc != -1:
            print('-----Lista de cuentas-----')
            self.__lista[0].títulos()
            for i in range(self.__cc + 1):
                self.__lista[i].mostrar()
            print('Fin de la lista...')
        else:
            print('No hay cuentas registradas...')
            
    def buscar_nc(self):
        if self.__cc != -1:
            print('-----Buscar por no. de cuenta-----')
            ban = True
            nc = 0
            while nc < 1:
                nc = self.__obd.entero('No. de cuenta a buscar: ')
            for i in range(self.__cc + 1):
                if nc == self.__lista[i].no_cuenta():
                    ban = False
                    self.__lista[i].títulos()
                    self.__lista[i].mostrar()
                    break
            if ban:
                print(f"No se ha encontrado ninguna cuenta con el no. de cuenta: {nc}")
        else:
            print('No hay cuentas registradas...')
            
    def buscar_na(self):
        if self.__cc != -1:
            ban = True
            print('-----Buscar por nombre o apellido-----')
            na = self.__obd.cadena('Ingresa el nombre/apellido: ').upper()
            for i in self.__lista:
                if na in i.nombre():
                    if ban:
                        ban = False
                        i.títulos()
                    i.mostrar()
            if ban:
                print(f"No se ha encontrado ninguna cuenta con el nombre/apellido \"{na}\"")
        else:
            print('No hay cuentas registradas...')
            
    def buscar_sal(self):
        if self.__cc != -1:
            ban = True
            print('-----Buscar por rango de saldo-----')
            ini = 0
            fin = -1
            while ini > fin and ini < 1:
                ini = self.__obd.real('Desde: $')
                fin = self.__obd.real('Hasta: $')
            for i in self.__lista:
                if ini <= i.saldo() and fin >= i.saldo():
                    if ban:
                        ban = False
                        i.títulos()
                    i.mostrar()
            if ban:
                print(f"No se ha encontrado ninguna cuenta con el rango de ${self.__obf.mon(ini)} - ${self.__obf.mon(fin)}")
        else:
            print('No hay cuentas registradas...')
            
    def modificar(self):
        if self.__cc != -1:
            ban = True
            print('-----Modificar cliente-----')
            nc = 0
            while nc < 1:
                nc = self.__obd.entero('No. de cuenta a modificar: ')
            for i in self.__lista:
                if nc == i.no_cuenta():
                    ban = False
                    i.modificar()
                    break
                
            if ban:
                print(f"No se ha encontrado ninguna cuenta con el no. de control \"{nc}\"")
        else:
            print('No hay cuentas registradas...')
            
    def borrar(self):
        if self.__cc != -1:
            ban = True
            print('-----Borrar cliente-----')
            nc = 0
            while nc < 1:
                nc = self.__obd.entero('No. de cuenta a borrar: ')
            for i in range(len(self.__lista)):
                if nc == self.__lista[i].no_cuenta():
                    print('Datos de la cuenta: ')
                    self.__lista[i].títulos()
                    self.__lista[i].mostrar()
                    if self.__lista[i].saldo() == 0:
                        sn = 0
                        while sn < 1 or sn > 2:
                            sn = self.__obd.entero('¿Estas seguro(a) de que deseas eliminar este cliente? (1 - SI) (2 - NO): ')
                        if sn == 1:
                            for j in range(i, self.__cc):
                                self.__lista[j] = self.__lista[j + 1]
                            self.__cc -= 1
                            print('Cuenta eliminada...')
                        else:
                            print('La cuenta no se eliminó...')
                    else:
                        print('La cuenta tiene saldo por lo que no se puede eliminar')
                    ban = False
                    break
                
            if ban:
                print(f"No se ha encontrado ninguna cuenta con el no. de control \"{nc}\"")
        else:
            print('No hay cuentas registradas...')
            
    def depositar(self):
        if self.__cc != -1:
            ban = True
            print('-----Deposito a cuenta-----')
            nc = 0
            while nc < 1:
                nc = self.__obd.entero('No. de cuenta a depositar: $')
            for i in self.__lista:
                if nc == i.no_cuenta():
                    ban = False
                    print(f"Saldo actual: {self.__obf.mon(i.saldo())}")
                    monto = 0
                    while monto <= 0:
                        monto = self.__obd.real('Ingresa la cantidad a depositar: $')
                    i.movimiento(monto)
                
            if ban:
                print(f"No se ha encontrado ninguna cuenta con el no. de control \"{nc}\"")
        else:
            print('No hay cuentas registradas...')
    
    def retirar(self):
        if self.__cc != -1:
            ban = True
            print('-----Retiro a cuenta-----')
            nc = 0
            while nc < 1:
                nc = self.__obd.entero('No. de cuenta a retirar: $')
            for i in self.__lista:
                if nc == i.no_cuenta():
                    if i.saldo() != 0:
                        print(f"Saldo actual: {self.__obf.mon(i.saldo())}")
                        monto = 0
                        while monto <= 0 or monto > i.saldo():
                            monto = self.__obd.real('Ingresa la cantidad a retirar: $')
                        i.movimiento(monto * -1)
                    else:
                        print('La cuenta no tiene saldo...')
                    ban = False
                    break
                
            if ban:
                print(f"No se ha encontrado ninguna cuenta con el no. de control \"{nc}\"")
        else:
            print('No hay cuentas registradas...')