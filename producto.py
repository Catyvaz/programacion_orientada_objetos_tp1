class Productos:
    #Se definen los datos nombre, precio y cantidad
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    #Se imprimen los datos nombre, precio y cantidad en la terminal
    def mostrar_informacion(self):
        print(f"Producto: {self.nombre} \nPrecio: $ {str(self.precio)} \nCantidad: {str(self.cantidad)}")