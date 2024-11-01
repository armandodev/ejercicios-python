from tema4.fecha_hora import FechaHora

def main():
    obf = FechaHora()
    print(obf.fechal())
    print(obf.fechas())
    print(obf.fechasm())
    print(obf.hora())
    print(obf.horam())
    print(f"La edad es {obf.edad(1, 11, 2006)} años")
    
if __name__ == '__main__':
    main()