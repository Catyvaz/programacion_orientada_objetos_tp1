from producto import *

class Alimentos(Productos):
    def getFechaExpiracion(self, expiracion):
        self.expiracion = expiracion
        return self.expiracion

    def mostrarDatos(self):
        print(f"El producto ¨{self.nombre}¨ tiene un precio de ${str(self.precio)} y hay una cantidad de {str(self.cantidad)}, con fecha de expiración para {self.expiracion}")