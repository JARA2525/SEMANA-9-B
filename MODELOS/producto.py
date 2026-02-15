# Archivo producto.py del sistema de inventarios
class Producto:
    def __init__(self, idp, nombre, cantidad, precio):
        self.__id = idp
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio

    def get_id(self): return self.__id
    def get_nombre(self): return self.__nombre
    def get_cantidad(self): return self.__cantidad
    def get_precio(self): return self.__precio

    def set_cantidad(self, c): self.__cantidad = c
    def set_precio(self, p): self.__precio = p

    def __str__(self):
        return f"{self.__id} | {self.__nombre} | {self.__cantidad} | ${self.__precio}"
