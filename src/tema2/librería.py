class Librería:    
    def leer(self):
        print('Ingresa la cantidad de libros de cada categoría')
        self.__cant_1 = int(input(f'Categoría 1: '))
        self.__cant_2 = int(input(f'Categoría 2: '))
        self.__cant_3 = int(input(f'Categoría 3: '))
        self.__cant_4 = int(input(f'Categoría 4: '))
        
    def calcular(self):
        self.__subtotal_1 = self.__cant_1 * 175.59
        self.__descuento_1 = self.__subtotal_1 * 0.05
        self.__total_1 = self.__subtotal_1 - self.__descuento_1
        
        self.__subtotal_2 = self.__cant_2 * 245.25
        self.__descuento_2 = self.__subtotal_2 * 0.07
        self.__total_2 = self.__subtotal_2 - self.__descuento_2
        
        self.__subtotal_3 = self.__cant_3 * 365.80
        self.__descuento_3 = self.__subtotal_3 * 0.10
        self.__total_3 = self.__subtotal_3 - self.__descuento_3
        
        self.__subtotal_4 = self.__cant_4 * 499.95
        self.__descuento_4 = self.__subtotal_4 * 0.15
        self.__total_4 = self.__subtotal_4 - self.__descuento_4
        
    def mostrar(self):
        print(f"Subtotal: {self.__subtotal}", f"Descuento: {self.__descuento}", f"Total: {self.__total}", sep='\n')