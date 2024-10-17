from tema3.impuestos import Impuestos

def main():
    obi = Impuestos()
    obi.precio()
    obi.horas()
    obi.calcular()
    obi.mostrar()
    
if __name__ == '__main__':
    main()