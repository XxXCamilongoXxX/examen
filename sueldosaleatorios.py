import random, csv, msvcrt, os
from funciones import *

gachapon=[]

trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]

while True:
    print("\nMenu de opciones")
    print("1. Asignar sueldos aleatorios")
    print("2. Clasificar sueldos")
    print("3. Ver estadisticas")
    print("4. Reporte de sueldos")
    print("5. Salir del programa")
    opc = int(input("Seleccione una opción: "))
    if opc==1:
        Sueldoaleatorio()
    elif opc==2:
        clasificarsueldos()
    elif opc==3:
        estadisticas()
    elif opc==4:
        reportsueldos()
    elif opc==5:
        salir()
    else:
        print("Ingrese una opción valida")
