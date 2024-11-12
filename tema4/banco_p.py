from fp.lib import Menú
from tema4.banco import Banco

def main():
    op = 0
    obb = Banco()
    obm = Menú('CLIENTES DEL BANCO', ['NUEVO', 'LISTA', 'BUSCAR', 'MODIFICAR', 'BORRAR', 'MOVIMIENTO'])
    
    while op != obm.salir():
        match op := obm.opción():
            case 1:
                obb.nueva()
            case 2:
                obb.mostrar()
            case 3:
                bop = 0
                obmb = Menú('BÚSQUEDA DE CLIENTES', ['NO. CUENTA', 'NOMBRE O APELLIDO', 'RANGO DE SALDOS'])
                
                while bop != obmb.salir():
                    match bop := obmb.opción():
                        case 1:
                            obb.buscar_nc()
                        case 2:
                            obb.buscar_na()
                        case 3:
                            obb.buscar_sal()
            case 4:
                obb.modificar()
            case 5:
                obb.borrar()
            case 6:
                mop = 0
                obmm = Menú('MOVIMIENTOS', ['DEPOSITO', 'RETIRO'])
                
                while mop != obmm.salir():
                    match mop := obmm.opción():
                        case 1:
                            obb.depositar()
                        case 2:
                            obb.retirar()
    
if __name__ == '__main__':
    main()