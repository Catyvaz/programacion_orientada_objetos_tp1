from producto import *

class Alimentos(Productos):
    def get_expiracion(self, fecha_expiracion):
        self.fecha_expiracion = fecha_expiracion
        return self.fecha_expiracion

    def mostrar_informacion(self):
        super().__init__(self.nombre, self.precio, self.cantidad)
        super().mostrar_informacion()
        return f"Fecha de expiración: {str(self.fecha_expiracion)}\n "