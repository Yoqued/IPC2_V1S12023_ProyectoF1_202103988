from Nodos.NodoPeliCat import *
from Clases.DatosCategoria import *
from Clases.DatosPelicula import *
class ListaDobleCircular:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def esta_vacia(self):
        return self.primero is None

    def insertar_al_final(self, dato):
        nuevo_nodo = nodoPeliCat(dato)
        if self.esta_vacia():
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
            nuevo_nodo.siguiente = nuevo_nodo
            nuevo_nodo.anterior = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.ultimo
            nuevo_nodo.siguiente = self.primero
            self.primero.anterior = nuevo_nodo
            self.ultimo.siguiente = nuevo_nodo
            self.ultimo = nuevo_nodo

    def insertar_al_inicio(self, dato):
        nuevo_nodo = nodoPeliCat(dato)
        if self.esta_vacia():
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
            nuevo_nodo.siguiente = nuevo_nodo
            nuevo_nodo.anterior = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.primero
            nuevo_nodo.anterior = self.ultimo
            self.primero.anterior = nuevo_nodo
            self.ultimo.siguiente = nuevo_nodo
            self.primero = nuevo_nodo

    def eliminar(self, dato):
        if self.esta_vacia():
            return

        nodo_actual = self.primero
        nodo_anterior = None

        while nodo_actual.dato != dato:
            if nodo_actual.siguiente == self.primero:
                return
            nodo_anterior = nodo_actual
            nodo_actual = nodo_actual.siguiente

        if nodo_actual == self.primero and nodo_actual == self.ultimo:
            self.primero = None
            self.ultimo = None
        elif nodo_actual == self.primero:
            self.primero = nodo_actual.siguiente
            self.ultimo.siguiente = self.primero
            self.primero.anterior = self.ultimo
        elif nodo_actual == self.ultimo:
            self.ultimo = nodo_anterior
            self.primero.anterior = self.ultimo
            self.ultimo.siguiente = self.primero
        else:
            nodo_anterior.siguiente = nodo_actual.siguiente
            nodo_actual.siguiente.anterior = nodo_anterior

    def imprimir_peli1(self, categoria):
        if self.esta_vacia():
            return

        nodo_actual = self.primero

        while True:
            if categoria == nodo_actual.dato.categoria:
                nodo_actual.dato.nombrepeli.imprimir_peli2()
            nodo_actual = nodo_actual.siguiente
            if nodo_actual == self.primero:
                break

    def imprimir_peli2(self):
        if self.esta_vacia():
            return

        nodo_actual = self.primero

        while True:
            print(nodo_actual.dato.titulo)
            nodo_actual = nodo_actual.siguiente
            if nodo_actual == self.primero:
                break
        return ''
    
    def imprimir_Categorias(self):
        if self.esta_vacia():
            print('"NO HAY PELÍCULAS CARGADAS"')
            return False

        nodo_actual = self.primero

        while True:
            print('-',nodo_actual.dato.categoria)
            nodo_actual = nodo_actual.siguiente
            if nodo_actual == self.primero:
                break
        return True
    
    def agregar_Peli_a_Cate(self, titulo, director, anio, fecha, hora):
        if self.esta_vacia():
            return

        nodo_actual = self.primero

        while True:
            if 'Comedia' == nodo_actual.dato.categoria:
                datos = peliculas(titulo, director, anio, fecha, hora)
                nodo_actual.dato.nombrepeli.insertar_al_final(datos)
            nodo_actual = nodo_actual.siguiente
            if nodo_actual == self.primero:
                break