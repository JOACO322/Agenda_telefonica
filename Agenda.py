import os
import msvcrt
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')  
def agregarusuario():
    nombre=input("Ingrese nombre:  ")
    usuario=open("primer ejemplo.txt","a")
    usuario.write(nombre+"   ")    
    telefono=input("Ingrese teléfono:  ")
    usuario.write(telefono+"\n")
    usuario.close()
def ver():
    nombre=open("primer ejemplo.txt","r")
    texto=nombre.read()
    print(texto)
    
def buscar():
    n=input("Ingrese nombre a buscar:  ")
    archivo=open("primer ejemplo.txt","r")
    
    for i in archivo.readlines():
        if n in i:
            print(i) 
    
    

respuesta=""
while respuesta!="salir":
    respuesta=input("Ingrese una opción:\nagregar\nver\nsalir\nbuscar\n"   )
    if respuesta=="agregar":
        agregarusuario()
    if respuesta=="ver":
        ver()
    if respuesta=="buscar":
        buscar()
if respuesta!="salir":
    print("Presiona cualquiera para volver al menú.")
    msvcrt.getch()  
    limpiar_pantalla()
