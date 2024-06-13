from producto import *

class Alimento(Productos):
    #Se define la fecha de expiración del producto alimento
    def get_expiracion(self, fecha_expiracion):
        self.fecha_expiracion = fecha_expiracion
        return self.fecha_expiracion

    #Se llama a la clase Padre para que traiga los datos
    #Se imprimen los datos de la clase Padre
    #Se imprimen los datos fecha de expiracion de la clase hija "Alimento"
    def mostrar_informacion(self):
        super().__init__(self.nombre, self.precio, self.cantidad)
        super().mostrar_informacion()
        return f"Fecha de expiración: {str(self.fecha_expiracion)}\n "