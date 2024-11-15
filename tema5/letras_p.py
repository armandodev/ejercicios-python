from tema5.letras import Letras

def main():
    obl = Letras()
    mat = obl.tamaño()
    obl.mostrar(mat)
    voc = obl.vocales(mat)
    obl.mostrar(voc)
    
if __name__ == '__main__':
    main()