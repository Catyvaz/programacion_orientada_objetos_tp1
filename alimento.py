from producto import *

class Alimentos(Productos):
    def getFechaExpiracion(self):
        return self.expiracion

    def mostrarDatos(self):
        print(f"Producto ¨{self.nombre}¨ tiene precio $ {str(self.precio)} y hay una cantidad de {str(self.cantidad)}, con expiración el {self.getFechaExpiracion}")