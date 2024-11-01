from tema4.lista_pro import ListaPro
from tema4.menu import Menú

def main():
    op = 0
    obl = ListaPro()
    obm = Menú('Control de productos', ['Nuevo', 'Lista'])
    
    while op != obm.salir():
        match op := obm.opcion():
            case 1:
                obl.nuevo()
            case 2:
                obl.mostrar()
            case 3:
                print('El proceso ha finalizado...')
            case _:
                print('Ingresa una opción válida')
    
if __name__ == '__main__':
    main()