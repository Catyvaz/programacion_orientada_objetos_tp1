from producto import *

class Electronico(Productos):
    def get_marca(self, marca):
        self.marca = marca
        return self.marca
    
    def get_modelo(self, modelo):
        self.modelo = modelo
        return self.modelo

    def mostrar_informacion(self):
        super().__init__(self.nombre, self.precio, self.cantidad)
        super().mostrar_informacion()
        return f"Marca: {self.marca} \nModelo: {self.modelo}\n "