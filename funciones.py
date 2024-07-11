import random, csv, msvcrt, os

gachapon=[]

trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]

def Sueldoaleatorio():
    print("\nGachapon")
    for g in range(10):    
        sueldos = random.randint(300000,2500000)
        gachapon.append(sueldos)
        #necesito ordenarlo de menor a mayor
    print(trabajadores[0],gachapon[0])
    print(trabajadores[1],gachapon[1])
    print(trabajadores[2],gachapon[2])
    print(trabajadores[3],gachapon[3])
    print(trabajadores[4],gachapon[4])
    print(trabajadores[5],gachapon[5])
    print(trabajadores[6],gachapon[6])
    print(trabajadores[7],gachapon[7])
    print(trabajadores[8],gachapon[8])
    print(trabajadores[9],gachapon[9])
def clasificarsueldos():
        #no se como hacer esto illo
        print("Sueldos menores a $800.000 TOTAL: ")

def estadisticas():
        print("Estadísticas")
        print("Sueldo más alto: ",{int(max(gachapon))})
        print("Sueldo más bajo: ",{int(min(gachapon))})
        print("Promedio de sueldos: ",promediosueldo())
        print("Media geométrica: ",mediageometrica())
def reportsueldos():
        print("Nombre empleado\tSueldo Base\tDescuento Salud\tDescuento AFP\tSueldo líquido")
        print(f"{trabajadores[0]," ",gachapon[0]}")
def salir():
        print("Finalizando programa...")
        print("Desarrollado por José Quezada")
        print("RUT 21.644.916-9")
        exit()
def promediosueldo():
       {int(gachapon)/10}
def mediageometrica():
       {int(gachapon[0]*gachapon[1]*gachapon[2]*gachapon[3]*gachapon[4]*gachapon[5]*gachapon[6]*gachapon[7]*gachapon[8]*gachapon[9])/10}
    
    