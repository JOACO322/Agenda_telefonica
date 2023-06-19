import os
import msvcrt

AGENDA_FILE = "Agenda.txt"

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def imprimir_menu():
    print("Agenda telefónica:")
    print("1. Agregar usuario")
    print("2. Ver usuarios")
    print("3. Buscar usuario")
    print("4. Salir")

def obtener_opcion():
    opcion = input("Ingrese una opción: ")
    while opcion not in ["1", "2", "3", "4"]:
        opcion = input("Opción inválida. Ingrese una opción nuevamente: ")
    return opcion

def agregar_nombre():
    nombre = input("Ingrese nombre: ")
    contador=0
    with open(AGENDA_FILE, "r") as archivo:
        for linea in archivo.readlines():
            if nombre in linea:
                contador=contador+1
            if contador>0:
               print("El usuario ya existe en la agenda. Ingrese otro nombre:")
               agregar_nombre()
            else:
                with open(AGENDA_FILE, "a") as archivo:
                    telefono = input("Ingrese teléfono: ")
                    archivo.write(f"{nombre} {telefono}\n")
                print("Usuario agregado exitosamente.")

def ver_usuarios():
    with open(AGENDA_FILE, "r") as archivo:
        print(archivo.read())

def buscar_usuario():
    nombre = input("Ingrese nombre a buscar: ")
    with open(AGENDA_FILE, "r") as archivo:
        for linea in archivo:
            if nombre in linea:
                print(linea)
                break
        else:
            print(f"No se encontró ningún usuario con el nombre {nombre}.")

import os
import msvcrt

AGENDA_FILE = "Agenda.txt"

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def imprimir_menu():
    print("Agenda telefónica:")
    print("1. Agregar usuario")
    print("2. Ver usuarios")
    print("3. Buscar usuario")
    print("4. Salir")

def obtener_opcion():
    opcion = input("Ingrese una opción: ")
    while opcion not in ["1", "2", "3", "4"]:
        opcion = input("Opción inválida. Ingrese una opción nuevamente: ")
    return opcion

def agregar_nombre():
    nombre = input("Ingrese nombre: ")
    nombre= nombre+" "
    coincidencias=0
    with open(AGENDA_FILE, "r") as archivo:
        for linea in archivo:
            if nombre in linea:
                coincidencias=1
        if coincidencias==1:
            print("Nombre ya existente")
            
            agregar_nombre()
        else:
            agregar_numero(nombre)
            
def agregar_numero(a):
    numero=input("Ingrese número: ")
    numero=numero+" "
    coincidencias=0
    archivo=open(AGENDA_FILE, "r") 
    for linea in archivo:
        if numero in linea:
            coincidencias=1
    if coincidencias==1:
        print("número ya existente:")
        
        agregar_numero(a)

    else:
        archivo.close()
        archivo=open(AGENDA_FILE,"a")
        archivo.write(f"{a}  {numero}\n")
        archivo.close()
        
            
            

def ver_usuarios():
    with open(AGENDA_FILE, "r") as archivo:
        print(archivo.read())

def buscar_usuario():
    nombre = input("Ingrese nombre a buscar: ")
    coincidencias=0
    with open(AGENDA_FILE, "r") as archivo:
        for linea in archivo:
            if nombre in linea:
                print(linea)
                coincidencias=1
        if coincidencias==0:
            print(f"No se encontró ningún usuario con el nombre {nombre}.")
        

with open(AGENDA_FILE, "a"):
    

    while True:
        imprimir_menu()
        opcion = obtener_opcion()
        if opcion == "1":
            agregar_nombre()
        elif opcion == "2":
            ver_usuarios()
        elif opcion == "3":
            buscar_usuario()
        elif opcion == "4":
            break

        input("Presione Enter para continuar...")
        limpiar_pantalla()

   