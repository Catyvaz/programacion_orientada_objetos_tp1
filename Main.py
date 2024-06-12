from producto import *
from electronico import *
from alimento import *

info = input("¿Que tipo de producto es? A = alimento o E = electronico. \n ==>")
if info.lower() == "a":
    nombre = input("Nombre del producto = ")
    precio = input("Precio del producto = ")
    cantidad = input("Cantidad del producto = ")
    expira = input("Fecha de expiración del producto = ")

    datos = Alimentos(nombre, precio, cantidad)
    datos.getFechaExpiracion(expira)
    datos.mostrarDatos()

if info.lower() == "e":
    nombre = input("Nombre del producto = ")
    precio = input("Precio del producto = ")
    cantidad = input("Cantidad del producto = ")
    marca = input("Marca del producto = ")
    modelo = input("Modelo del producto = ")

    datos = Electronico(nombre, precio, cantidad)
    datos.getMarca(marca)
    datos.getModelo(modelo)
    datos.mostrarDatos()

