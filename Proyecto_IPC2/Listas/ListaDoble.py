from Nodos.NodoEntrada import *
class ListaEnlazadaDoble:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def esta_vacia(self):
        return self.primero is None

    def agregar_inicio(self, dato):
        nuevo_nodo = nodoEntrada(dato)

        if self.esta_vacia():
            self.primero = self.ultimo = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.primero
            self.primero.anterior = nuevo_nodo
            self.primero = nuevo_nodo

    def agregar_final(self, dato):
        nuevo_nodo = nodoEntrada(dato)

        if self.esta_vacia():
            self.primero = self.ultimo = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.ultimo
            self.ultimo.siguiente = nuevo_nodo
            self.ultimo = nuevo_nodo

    def eliminar_inicio(self):
        if self.esta_vacia():
            return None

        dato_eliminado = self.primero.dato
        self.primero = self.primero.siguiente

        if self.primero is None:
            self.ultimo = None
        else:
            self.primero.anterior = None

        return dato_eliminado

    def eliminar_final(self):
        if self.esta_vacia():
            return None

        dato_eliminado = self.ultimo.dato
        self.ultimo = self.ultimo.anterior

        if self.ultimo is None:
            self.primero = None
        else:
            self.ultimo.siguiente = None

        return dato_eliminado