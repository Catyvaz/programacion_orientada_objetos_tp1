from producto import *
from electronico import *
from alimento import *

info = input("¿Que tipo de producto es? A = alimento o E = electronico. \n ==>")
if info.lower() == "a":
    nombre = input("Nombre del producto = ")
    precio = input("Precio del producto = ")
    cantidad = input("Cantidad del producto = ")

    datos = Productos(nombre, precio, cantidad)
    datos.mostrarDatos()

if info.lower() == "e":
    datos = Electronico("Bujia", 780, 36)
    datos.mostrarDatos()

