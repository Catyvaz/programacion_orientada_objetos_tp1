from producto import *

class Electronico(Productos):
    #Se define la marca del producto electrónico
    def get_marca(self, marca):
        self.marca = marca
        return self.marca
    
    #Se define el modelo del producto electrónico
    def get_modelo(self, modelo):
        self.modelo = modelo
        return self.modelo

    #Se llama a la clase Padre para que traiga los datos
    #Se imprimen los datos de la clase Padre
    #Se imprimen los datos marca y modelo de la clase hija "Electronico"
    def mostrar_informacion(self):
        super().__init__(self.nombre, self.precio, self.cantidad)
        super().mostrar_informacion()
        return f"Marca: {self.marca} \nModelo: {self.modelo}\n "