class Tablas:
    def __init__(self):
        for tab in range(1, 11):
            for i in range(1, 11):
                self.__mostrar(tab, i, tab * i)
                
    def __mostrar(self, tab, con, res):
        if con == 1:
            print(f"-----Tabla del {tab}-----")
        print(f"{tab} * {con} = {res}")