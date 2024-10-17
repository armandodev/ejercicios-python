import random

# Construir un vector de N elementos enteros, genera los valores de sus posiciones de manera aleatoria
# en un rango de 1 a 100 incluyendo los límites, posteriormente calcula y presenta el promedio de todos
# los elementos

class Vector():
    def tamaño(self):
        self.__tam = 0
        while self.__tam < 1:
            self.__tam = int(input("Ingresa la cantidad de datos a guardar: "))
        self.__vec = [0 for _ in range(self.__tam)]
    
    def valores(self):
        self.__vec = [int(input(f"{i + 1}/{self.__tam} Ingresa un número: ")) for i in range(self.__tam)]
        
    def mostrar(self):
        print('-----Vector-----')
        print(f"{self.__vec}")
        
    def rango(self):
        print('-----Rango-----')
        ini = 0
        fin = -1
        while fin < ini:
            ini = int(input('Desde: '))
            fin = int(input('Hasta: '))
        for i in range(self.__tam):
            self.__vec[i] = random.randint(ini, fin)
            
    def mayor(self):
        may = self.__vec[0]
        for i in range(self.__tam):
            if self.__vec[i] > may:
                may = self.__vec[i]
                
        print(f"-----El número mayor es {may}-----")
            
    def menor(self):
        men = self.__vec[0]
        for i in range(self.__tam):
            if self.__vec[i] < men:
                men = self.__vec[i]
                
        print(f"-----El número menor es {men}-----")
        
    def buscar(self):
        num = int(input('Ingresa el número a buscar: '))
        ban = True
        for i in range(len(self.__vec)):
            if self.__vec[i] == num:
                if ban:
                    print('Número encontrado en las posiciones: ')
                ban = False
                print(f"[{i + 1}]", end=' ')
                
        if ban:
            print('Elemento no encontrado')
            
    def suma(self):
        con = 0
        for i in range(len(self.__vec)):
            con += self.__vec[i]
        print('-----Suma-----')
        print(f"La suma de los elementos es igual a: {con}")
        
    def promedio(self):
        prom = 0
        for i in range(len(self.__vec)):
            prom += self.__vec[i]
        prom /= len(self.__vec)
        print('-----Promedio-----')
        print(f"El promedio de los elementos es igual a: {prom:.0f}")