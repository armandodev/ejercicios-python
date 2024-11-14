from tema5.producto import Producto

def main():
    obp = Producto()    
    obp.mostrar(obp.multiplicar(obp.números()))

if __name__ == '__main__':
    main()