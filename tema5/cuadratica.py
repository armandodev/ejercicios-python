class Cuadrática:
    def leer(self):
        print('-----Valores a, b y c de la ecuación ax² + bx + c-----')
        a = float(input('Ingrese el valor de a: '))
        while a == 0:
            a = float(input('Ingrese el valor de a: '))
        b = float(input('Ingrese el valor de b: '))
        c = float(input('Ingrese el valor de c: '))
        return a, b, c

    def discriminante(self, a, b, c):
        return (b ** 2) - (4 * a * c)

    def calcular(self, a, b, dis):
        if dis > 0:
            x1 = (-b + (dis ** 0.5)) / (2 * a)
            x2 = (-b - (dis ** 0.5)) / (2 * a)
        else:
            x1 = -b / (2 * a)
            x2 = x1
        return x1, x2

    def mostrar(self, dis, x1, x2):
        if dis > 0:
            print(f"Las soluciones reales son: x₁ = {x1} y x₂ = {x2}")
        elif dis == 0:
            print(f"Solo hay una solución real: x = {x1}")
        else:
            print('No hay solución')

def main():
    obc = Cuadrática()
    a, b, c = obc.leer()
    dis = obc.discriminante(a, b, c)
    x1, x2 = obc.calcular(a, b, dis)
    obc.mostrar(dis, x1, x2)

if __name__ == '__main__':
    main()