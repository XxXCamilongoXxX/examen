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
            for x in range(10):
                menor800={int(gachapon[x])<800000}
                if False:
                    print(gachapon[x])
                else:
                    pass
            print("Sueldos menores a $800.000")
            print(menor800)
        

        

def estadisticas():
        print("Estadísticas")
        print("Sueldo más alto: ",{int(max(gachapon))})
        print("Sueldo más bajo: ",{int(min(gachapon))})
        print("Promedio de sueldos: ",{int(sum(gachapon))/10})
        print("Media geométrica: ",{int(sum(gachapon[0]*gachapon[1]*gachapon[2]*gachapon[3]*gachapon[4]*gachapon[5]*gachapon[6]*gachapon[7]*gachapon[8]*gachapon[9])**1/10)})
def reportsueldos():
        print("Nombre empleado\tSueldo Base\tDescuento Salud\tDescuento AFP\t\tSueldo líquido")
        print(f"{trabajadores[0],"  ",gachapon[0],"  ",{int(gachapon[0]*0.7)},"  ",{int(gachapon[0]*0.12)},"  ",{int(gachapon[0])-(gachapon[0]*0.12+gachapon[0]*0.7)}}")
        print(f"{trabajadores[1],"  ",gachapon[1],"  ",{int(gachapon[1]*0.7)},"  ",{int(gachapon[1]*0.12)},"  ",{int(gachapon[1])-(gachapon[1]*0.12+gachapon[1]*0.7)}}")
        print(f"{trabajadores[2],"  ",gachapon[2],"  ",{int(gachapon[2]*0.7)},"  ",{int(gachapon[2]*0.12)},"  ",{int(gachapon[2])-(gachapon[2]*0.12+gachapon[2]*0.7)}}")
        print(f"{trabajadores[3],"  ",gachapon[3],"  ",{int(gachapon[3]*0.7)},"  ",{int(gachapon[3]*0.12)},"  ",{int(gachapon[3])-(gachapon[3]*0.12+gachapon[3]*0.7)}}")
        print(f"{trabajadores[4],"  ",gachapon[4],"  ",{int(gachapon[4]*0.7)},"  ",{int(gachapon[4]*0.12)},"  ",{int(gachapon[4])-(gachapon[4]*0.12+gachapon[4]*0.7)}}")
        print(f"{trabajadores[5],"  ",gachapon[5],"  ",{int(gachapon[5]*0.7)},"  ",{int(gachapon[5]*0.12)},"  ",{int(gachapon[5])-(gachapon[5]*0.12+gachapon[5]*0.7)}}")
        print(f"{trabajadores[6],"  ",gachapon[6],"  ",{int(gachapon[6]*0.7)},"  ",{int(gachapon[6]*0.12)},"  ",{int(gachapon[6])-(gachapon[6]*0.12+gachapon[6]*0.7)}}")
        print(f"{trabajadores[7],"  ",gachapon[7],"  ",{int(gachapon[7]*0.7)},"  ",{int(gachapon[7]*0.12)},"  ",{int(gachapon[7])-(gachapon[7]*0.12+gachapon[7]*0.7)}}")
        print(f"{trabajadores[8],"  ",gachapon[8],"  ",{int(gachapon[8]*0.7)},"  ",{int(gachapon[8]*0.12)},"  ",{int(gachapon[8])-(gachapon[8]*0.12+gachapon[8]*0.7)}}")
        print(f"{trabajadores[9],"  ",gachapon[9],"  ",{int(gachapon[9]*0.7)},"  ",{int(gachapon[9]*0.12)},"  ",{int(gachapon[9])-(gachapon[9]*0.12+gachapon[9]*0.7)}}")
def salir():
        print("Finalizando programa...")
        print("Desarrollado por José Quezada")
        print("RUT 21.644.916-9")
        exit()
    
    