from producto import *
from electronico import *
from alimento import *

#Defino las variables para mas facilidad 
nombreA = "Fideos"
nombreE = "Televisor" 
precio = 1500 
cantidad = 56
expiracion = "15/8/25"
marca = "Samsung"
modelo = "Smart tv 2020"

#Solo muestra datos de un producto
datos = Productos(nombreA, precio, cantidad)
print(">> Producto <<")
datos.mostrar_informacion()

print("")
print("#######################################")
print("")

#Muestra los datos de un alimento
datos = Alimento(nombreA, precio, cantidad)
datos.get_expiracion(expiracion)
print(">> Producto Alimento <<")
print(datos.mostrar_informacion())

print("#######################################")
print("")

#Muestra los datos de un electronico
datos = Electronico(nombreE, precio, cantidad)
datos.get_marca(marca)
datos.get_modelo(modelo)
print(">> Producto Electronico <<")
print(datos.mostrar_informacion())