archivo=open("archivo.txt","r") #con esto se puede leer el archivo sin la necesidad de escribir 
texto=archivo.read()
print(texto)
archivo.close()