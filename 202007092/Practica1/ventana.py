from importlib.abc import Loader
from math import prod
from msilib.schema import Environment
from os import startfile
from tkinter import filedialog
from unittest import loader, result
import pandas as pd
import numpy as np
from os import remove
from tkinter import filedialog
import re

from jinja2 import FileSystemLoader, select_autoescape
from jinja2 import Environment, select_autoescape
import jinja2
from producto import Producto
from cProfile import label
from matplotlib import pyplot as plt
from matplotlib import pyplot
import numpy as np
#from crud_productos import CRUD_productos
import re

#crudProductos = CRUD_productos()
listaProductos = []
listaInstrucciones = []



#######################################################################

def abrir():
    archivo = filedialog.askopenfilename(title='abrir', filetypes=(('archivos data', '*.data'), ('archivos txt', '*.txt'), ('archivos lfp', '*.lfp')))


    # leer archivo palabra por palabra y convertir a una lista
    datos = []
    datosg = []
    dnuevo = []
    datos_sin_caracter = []
    

    #leemos el data y convertimos a lista
    with open(archivo) as fname:
        for lineas in fname:
            datos.extend(lineas.split('(\[\w+)'))

    #eliminamos caracteres innecesarios
    for da in datos:
        dnuevo.append(da.replace('"', '').replace('\n', ''))

    #buscamos los datos del producto

    for d in dnuevo:
        
        resultado = re.match('(\[\w+\s*\w*[\s,.]*\w*[\s,.]*\w*[\s,.]*\w*)', d)
        if resultado:
            datosg.extend(resultado.groups())
    
    for d in datosg:
        datos_sin_caracter.append(d.replace('[', ''))

    return datos_sin_caracter
    

datos_productos = []


###################################################################################################


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
    

    return dnuevo

#############################################################################################

def convertir(listaProductos):
    listaP = []
    datos = []
    
    for d in listaProductos:
        #listaProductos.append(Producto('hola', 516,12))
        datos = d.split(',')
        #listaP.append(datos)
        pro="none"
        precio=0
        cantidad=0
        for s in range(len(datos)):
            
            if s == 0:
                pro=datos[s]
            elif s==1:
                precio=float(datos[s])
                #print(type(precio))
            elif s==2:
                cantidad=int(datos[s])
        listaP.append(Producto(pro, precio, cantidad))
    
    #print(listaP)    

    return listaP


#######################################################################
        
ds = []        


precios = []
nombres = []
cantidades = []

#print(len(ds))
#print(len(precios))



#######################################################################
#se ordena de mayor a menor



#######################################################################
#se seperan para graficar
produtco=[]


#print(len(precios))
#print(precios)
#print(nombres)
#print(cantidades)




#######################################################################
def graficaLineal(pre):
    plt.plot(pre)
    plt.xlabel(listaInstrucciones[3])
    plt.ylabel(listaInstrucciones[4])
    plt.title(listaInstrucciones[2])
    plt.show()


#######################################################################
def graficaBarras(no, ca):
    plt.bar(no, ca)
    plt.title(listaInstrucciones[2])
    plt.show()


#######################################################################
def graficaCir(ca, no):
    plt.pie(ca, labels=no)
    plt.title(listaInstrucciones[2])
    plt.show()




#######################################################################




#graficaCir()
#graficaLineal()
#graficaBarras()


#######################################################################

def abrirHtml():
    archivo=open('report/datoss.html', 'w')
    with open('report/reports.html') as fname:
        for lineas in fname:
            if lineas == 'edicion':
                lineas = export_report()
            archivo.write(lineas)

#######################################################################



while True:
    print('''
---- Menú ----
1. Cargar Archivo data
2. Cargar archivo lfp
3. Analizar
4. Reportes
5. Salir
---- ---- ----
        ''')

    opt = input('Ingresa una opción: ')

    if opt =='1':
        print('cargar archivos data')
        datos_productos = abrir()
        ds = convertir(datos_productos)

####################################################################################

        for recorrido in range(1, len(ds)):
            for position in range(len(ds)- recorrido):
                if (ds[position].precio*ds[position].cantidad) < (ds[position+1].precio*ds[position+1].cantidad):
                    temp=ds[position]
                    ds[position]=ds[position+1]
                    ds[position+1]=temp

        for i in range(len(ds)):
            precios.append(ds[i].precio)
            nombres.append(ds[i].nombre)
            cantidades.append(ds[i].cantidad)
            produtco.append(ds[i].cantidad*ds[i].precio)
    elif opt =='2':
        print('Cargar archivos lfp')
        listaInstrucciones = abrirlfp()

    elif opt =='3':
        if listaInstrucciones[1]=='Barras':
            graficaBarras(nombres, cantidades)
        elif listaInstrucciones[1]=='Circular':
            graficaCir(cantidades, nombres)
        elif listaInstrucciones[1]=="lineal":
            graficaLineal(precios)
        print('se analizo')
    elif opt == '4':
        print('se crearon reportes')
        def export_report():
            producto = {
                "nombre: ":nombres,
                'Precio: ': precios,
                'Vendidos: ': cantidades,
                'venta: ': produtco
            }

            df = pd.DataFrame(data=producto)
            print(df)
            
            return df.to_html()

        htmnl= export_report()

        archivo = open('reporte.html', 'w')

        archivo.write('<h1 class="text-center">Reporte</h1><h2 class="text-center">JONATAN JOSUE VASQUEZ PASTOR</h2><h2 class="text-center">202007092</h2>')
        archivo.write(htmnl)
        archivo.close()

    elif opt =='5':
        print("saliendo...")
        break
    else: 
        print('no se que paso')
        continue
        


