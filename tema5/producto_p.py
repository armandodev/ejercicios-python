from tema5.producto import Producto

def main():
    obp = Producto()
    a, b = obp.números()
    res = obp.multiplicar(a, b)
    obp.mostrar(res)

if __name__ == '__main__':
    main()