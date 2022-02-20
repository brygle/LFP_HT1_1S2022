from os import remove
from tkinter import filedialog
import re

def abrirlfp():
    archivo = filedialog.askopenfilename(title='abrir', filetypes=(('archivos lfp', '*.lfp'), ('archivos txt', '*.txt')))

    datos = []
    dnuevo = []

    with open(archivo) as fname:
        for lineas in fname:
            datos.extend(lineas.split(','))

    
    for d in datos:
        resultado = re.match('(.+"\.*)', d)
        if resultado:
            dnuevo.extend(resultado.groups())


    contador = 0
    for d in dnuevo:
        if re.match('(Nombre:\.*)', d):
            dnuevo[contador] = dnuevo[contador].replace('Nombre: ', '').replace('"', '')
        elif re.match('(Grafica:\.*)', d):
            dnuevo[contador] = dnuevo[contador].replace('Grafica: ', '').replace('"', '')
        elif re.match('(Titulo:\.*)', d):
            dnuevo[contador] = dnuevo[contador].replace('Titulo: ', '').replace('"', '')
        elif re.match('(TituloX:\.*)', d):
            dnuevo[contador] = dnuevo[contador].replace('TituloX: ', '').replace('"','')
        elif re.match('(TituloY:\.*)', d):
            dnuevo[contador] = dnuevo[contador].replace('TituloY: ', '').replace('"', '')

        contador=contador+1
    

    print(dnuevo)

