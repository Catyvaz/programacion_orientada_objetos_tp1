class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def mostrarDatos(self):
        print(f"El producto ¨{self.nombre}¨ tiene precio ${str(self.precio)} y hay una cantidad de {str(self.cantidad)}")

nombre = input("Nombre del producto = ")
precio = input("Precio del producto = ")
cantidad = input("Cantidad del producto = ")

producto = Producto(nombre, precio, cantidad)
producto.mostrarDatos()