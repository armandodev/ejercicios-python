from fp.lib import Menú
from tema4.lista_alu import ListaAlu

def main():
    obl = ListaAlu()
    obm = Menú('CONTROL DE MATERIAS', ['NUEVO', 'MOSTRAR', 'BUSCAR', 'MODIFICAR'])
    op = 0
    
    while op != obm.salir():
        match op := obm.opción():
            case 1:
                obl.nueva()
            case 2:
                obl.mostrar()
            case 3:
                obl.buscar()
            case 4:
                obl.modificar()
    
if __name__ == '__main__':
    main()