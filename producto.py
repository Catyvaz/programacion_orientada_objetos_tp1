class Productos:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def mostrar_informacion(self):
        print(f"Producto: {self.nombre} \nPrecio: $ {str(self.precio)} \nCantidad: {str(self.cantidad)}")