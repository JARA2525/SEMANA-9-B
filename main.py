# ==========================================
# Sistema de Gestión de Inventarios
# Autor: John Jara
# Universidad: TICS
# ==========================================

from modelos import Producto
from servicios import Inventario

inv = Inventario()

while True:
    print("\n1 Agregar 2 Eliminar 3 Actualizar 4 Buscar 5 Listar 6 Salir")
    op = input("Opción: ")

    if op == "1":
        idp = int(input("ID: "))
        n = input("Nombre: ")
        c = int(input("Cantidad: "))
        pr = float(input("Precio: "))
        inv.agregar(Producto(idp, n, c, pr))

    elif op == "2":
        inv.eliminar(int(input("ID: ")))

    elif op == "3":
        idp = int(input("ID: "))
        c = int(input("Cantidad nueva: "))
        pr = float(input("Precio nuevo: "))
        inv.actualizar(idp, c, pr)

    elif op == "4":
        n = input("Buscar: ")
        for p in inv.buscar(n): print(p)

    elif op == "5":
        inv.listar()

    elif op == "6":
        break
