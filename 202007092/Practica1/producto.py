
class Producto:
    def __init__(self, nombre: str, precio: float, cantidad: int) -> None:
        self.nombre: str = nombre
        self.precio: float = float(precio)
        self.cantidad: int = int(cantidad)