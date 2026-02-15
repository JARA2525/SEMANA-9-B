# Archivo inventario.py del sistema de inventarios
from MODELOS.producto import Producto

class Inventario:
    def __init__(self):
        self.productos = []

    def agregar(self, p):
        if any(x.get_id() == p.get_id() for x in self.productos):
            print("ID repetido")
        else:
            self.productos.append(p)

    def eliminar(self, idp):
        self.productos = [p for p in self.productos if p.get_id() != idp]

    def actualizar(self, idp, c=None, pr=None):
        for p in self.productos:
            if p.get_id() == idp:
                if c: p.set_cantidad(c)
                if pr: p.set_precio(pr)

    def buscar(self, nombre):
        return [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]

    def listar(self):
        for p in self.productos:
            print(p)
