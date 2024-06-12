from producto import *

class Electronico(Productos):
    def getMarca(self, marca):
        self.marca = marca
        return self.marca
    def getModelo(self, modelo):
        self.modelo = modelo
        return self.modelo

    def mostrarDatos(self):
        print(f"El producto ¨{self.nombre}¨, marca ¨{self.getMarca}¨ y modelo ¨{self.getModelo}¨") 
        print(f"Tiene precio ${str(self.precio)} y hay una cantidad de {str(self.cantidad)}")