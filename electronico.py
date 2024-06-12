from producto import *

class Electronico(Productos):
    def getMarca(self, marca):
        self.marca = marca
        return self.marca
    def getModelo(self, modelo):
        self.modelo = modelo
        return self.modelo

    def mostrarDatos(self):
        print(f"El producto ¨{self.nombre}¨, marca ¨{self.marca}¨ y modelo ¨{self.modelo}¨") 
        print(f"Tiene un precio de ${str(self.precio)} y hay una cantidad de {str(self.cantidad)}")