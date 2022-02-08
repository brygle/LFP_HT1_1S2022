from io import open

archivo = open("archivo.data", "r")

texto = archivo.read()

archivo.close()

print(texto)