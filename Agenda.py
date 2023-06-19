import os


def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")


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


def buscar():
    archivo = open("agenda.csv", "r")
    _ = archivo.readline()
    nombre = input("Ingrese elemento a buscar")
    for i in archivo.readlines():
        if nombre.lower() in i.lower():
            print(i)


def agregar():
    variable = []
    archivo = []
    nombre = input("Ingrese nombre: ")
    archivo = open("agenda.csv", "r")
    _ = archivo.readline()
    for i in archivo.readlines():
        if nombre.lower() in i.lower():
            print("Nombre ya existente:")
            agregar()
            break
    else:
        variable.append(nombre)
        agregar_numero(variable)

    archivo.close()


def agregar_numero(a):
    variable = a
    numero = input("Ingrese número: ")
    archivo = open("agenda.csv", "r")
    _ = archivo.readline()
    for i in archivo.readlines():
        if numero in i:
            print("Número ya existente")
            agregar_numero(variable)
            break
    else:
        archivo.close()
        variable.append(numero)
        archivo = open("agenda.csv", "a")
        archivo.write(";".join(variable) + "\n")
        archivo.close()


def ver_usuarios():
    archivo = open("agenda.csv", "r")
    _ = archivo.readline()
    for i in archivo.readlines():
        print(i)


while True:
    imprimir_menu()
    opcion = obtener_opcion()
    if opcion == "1":
        agregar()
    elif opcion == "2":
        ver_usuarios()
    elif opcion == "3":
        buscar()
    elif opcion == "4":
        print("Programa finalizado")
        break
    print("1: Voler al menú \n2: Salir")
    respuesta = input()
    while respuesta not in ["1", "2"]:
        print("Opción no válida, reintente")
        respuesta = input()
    if respuesta == "2":
        print("Programa finalizado")
        break
    limpiar_pantalla()
