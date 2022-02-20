from msilib.schema import Class
from producto import Producto

class CRUD_productos:
    def __init__(self):
        self.productos = []

    def crearProductos(self, producto, precio, cantidad):
        nuevoProducto=Producto(producto, float(precio), int(cantidad))
        self.productos.append(nuevoProducto)
    
    def datos(self):
        return self.productos
