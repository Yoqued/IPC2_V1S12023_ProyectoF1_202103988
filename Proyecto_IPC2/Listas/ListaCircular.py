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

    def eliminarCategoria(self, categoria):
        if self.esta_vacia():
            return

        nodo_actual = self.primero
        nodo_anterior = None

        while nodo_actual.dato.categoria != categoria:
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
            print('------------------------------------------')
            print('-', nodo_actual.dato.titulo)
            print('-', nodo_actual.dato.director)
            print('-', nodo_actual.dato.anio)
            print('-', nodo_actual.dato.fecha)
            print('-', nodo_actual.dato.hora)
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
    
    def agregar_Peli_a_Cate(self, categoria, titulo, director, anio, fecha, hora):
        if self.esta_vacia():
            return

        nodo_actual = self.primero

        while True:
            if categoria == nodo_actual.dato.categoria:
                datos = peliculas(titulo, director, anio, fecha, hora)
                nodo_actual.dato.nombrepeli.insertar_al_final(datos)
            nodo_actual = nodo_actual.siguiente
            if nodo_actual == self.primero:
                break
    
    def busc_cate_para_Eliminar(self, categoria, titulo):
        if self.esta_vacia():
            return

        nodo_actual = self.primero

        while True:
            if categoria == nodo_actual.dato.categoria:
                return nodo_actual.dato.nombrepeli.eliminarPeli(titulo)
            nodo_actual = nodo_actual.siguiente
            if nodo_actual == self.primero:
                break
    
    def eliminarPeli(self, titulo):
        if self.esta_vacia():
            return

        nodo_actual = self.primero
        nodo_anterior = None

        while nodo_actual.dato.titulo != titulo:
            if nodo_actual.siguiente == self.primero:
                return 'No se encontro la "PELÍCULA"'
            nodo_anterior = nodo_actual
            nodo_actual = nodo_actual.siguiente

        if nodo_actual == self.primero and nodo_actual == self.ultimo:
            self.primero = None
            self.ultimo = None
            return 'Película "ELIMINADA"'
        elif nodo_actual == self.primero:
            self.primero = nodo_actual.siguiente
            self.ultimo.siguiente = self.primero
            self.primero.anterior = self.ultimo
            return 'Película "ELIMINADA"'
        elif nodo_actual == self.ultimo:
            self.ultimo = nodo_anterior
            self.primero.anterior = self.ultimo
            self.ultimo.siguiente = self.primero
            return 'Película "ELIMINADA"'
        else:
            nodo_anterior.siguiente = nodo_actual.siguiente
            nodo_actual.siguiente.anterior = nodo_anterior
            return 'Película "ELIMINADA"'

    def chec_Categoria(self, categoria):
        if self.esta_vacia():
            return
        Estado = False
        nodo_actual = self.primero

        while True:
            if categoria == nodo_actual.dato.categoria:
                Estado = True
            nodo_actual = nodo_actual.siguiente
            if nodo_actual == self.primero:
                break
        return Estado
    
    def chec_Categoria_Eliminar(self, categoria):
        if self.esta_vacia():
            return
        Estado = True
        nodo_actual = self.primero

        while True:
            if categoria == nodo_actual.dato.categoria:
                Estado = False
            nodo_actual = nodo_actual.siguiente
            if nodo_actual == self.primero:
                break
        return Estado
    
    def modificar_categoria(self, categoria_antigua, categoria_nueva):
        if self.esta_vacia():
            return

        nodo_actual = self.primero

        while nodo_actual.dato.categoria != categoria_antigua:
            nodo_actual = nodo_actual.siguiente
            if nodo_actual == self.primero:
                return

        nodo_actual.dato.categoria = categoria_nueva

    def buscar_categoria_pelicula(self, categoria, titulo, director, anio, fecha, hora, titulo_new):
        if self.esta_vacia():
            return

        nodo_actual = self.primero

        while True:
            if categoria == nodo_actual.dato.categoria:
                nodo_actual.dato.nombrepeli.modificar_pelicula(titulo, director, anio, fecha, hora, titulo_new)
            nodo_actual = nodo_actual.siguiente
            if nodo_actual == self.primero:
                break
    
    def modificar_pelicula(self, titulo, director, anio, fecha, hora, titulo_new):
        if self.esta_vacia():
            return

        nodo_actual = self.primero

        while nodo_actual.dato.titulo != titulo:
            nodo_actual = nodo_actual.siguiente
            if nodo_actual == self.primero:
                return
        if director is None and anio is None and fecha is None and hora is None:
            print("cagate")
            nodo_actual.dato.titulo = titulo_new
        elif anio is None and fecha is None and hora is None and titulo_new is None:
            nodo_actual.dato.director = director
        elif director is None and fecha is None and hora is None and titulo_new is None:
            nodo_actual.dato.anio = anio
        elif director is None and anio is None and hora is None and titulo_new is None:
            nodo_actual.dato.fecha = fecha
        elif director is None and anio is None and fecha is None and titulo_new is None:
            nodo_actual.dato.hora = hora