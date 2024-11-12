from fp.lib import Menú
from tema4.lista_mat import ListaMat

def main():
    obl = ListaMat()
    obm = Menú('CONTROL DE MATERIAS', ['NUEVA', 'LISTA', 'BUSCAR'])
    op = 0
    
    while op != obm.salir():
        match op := obm.opción():
            case 1:
                obl.nueva()
            case 2:
                obl.lista()
            case 3:
                os = 0
                obs = Menú('Busquedas', ['CLAVE', 'NOMBRE'])
                while os != obs.salir():
                    match os := obs.opción():
                        case 1:
                            obl.buscar()
                        case 2:
                            obl.buscar_nom()
    
if __name__ == '__main__':
    main()