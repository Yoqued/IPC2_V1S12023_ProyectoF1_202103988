from Nodos.NodoUsuario import *
from Clases.DatosUsuario import *
class listaEnlazada:
    def __init__(self):
        self.cabeza = None
        
    def esta_vacia(self):
        return self.cabeza is None

    def agregar_al_final(self, dato):
        nuevo_nodo = nodoUsuario(dato)

        if self.esta_vacia():
            self.cabeza = nuevo_nodo
        else:
            nodo_actual = self.cabeza
            while nodo_actual.siguiente is not None:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nuevo_nodo

    def imprimir_lista(self):
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            print(nodo_actual.dato.nombre)
            print(nodo_actual.dato.apellido)
            print(nodo_actual.dato.telefono)
            print(nodo_actual.dato.correo)
            print(nodo_actual.dato.contraseña)
            print(nodo_actual.dato.rol)
            nodo_actual = nodo_actual.siguiente

    def Acceso(self, correo_cliente, contrasena):
        temporal = self.cabeza
        while temporal is not None:
            if temporal.dato.correo == correo_cliente and temporal.dato.contraseña == contrasena:
                if temporal.dato.rol == "cliente":
                    return True, temporal.dato.nombre, 'cliente'
                elif temporal.dato.rol == "administrador":
                    return True, temporal.dato.nombre, 'administrador'
            temporal = temporal.siguiente
        return False, None, None

    def eliminar(self, correo):
        if self.esta_vacia():
            return

        if self.cabeza.dato.correo == correo:
            self.cabeza = self.cabeza.siguiente
            return 'Se ha borado el "Usuario"'

        nodo_actual = self.cabeza
        while nodo_actual.siguiente is not None:
            if nodo_actual.siguiente.dato.correo == correo:
                nodo_actual.siguiente = nodo_actual.siguiente.siguiente
                return 'Se ha borado el "Usuario"'
            nodo_actual = nodo_actual.siguiente

        return 'El Usuario del correo:', correo, 'no se encontró'  

    def modificar_dato(self, rol, nombre, apellido, telefono, correo, contraseña):
        if self.esta_vacia():
            return

        nodo_actual = self.cabeza
        while nodo_actual is not None:
            if nodo_actual.dato.correo == correo and apellido is None and telefono is None and contraseña is None and rol is None:
                nodo_actual.dato.nombre = nombre
                return 'Modificación "REALIZADA"'
            elif nodo_actual.dato.correo == correo and nombre is None and telefono is None and contraseña is None and rol is None:
                nodo_actual.dato.apellido = apellido
                return 'Modificación "REALIZADA"'
            elif nodo_actual.dato.correo == correo and nombre is None and apellido is None and contraseña is None and rol is None:
                nodo_actual.dato.telefono = telefono
                return 'Modificación "REALIZADA"'
            elif nodo_actual.dato.correo == correo and nombre is None and apellido is None and telefono is None and rol is None:
                nodo_actual.dato.contraseña = contraseña
                return 'Modificación "REALIZADA"'
            elif nodo_actual.dato.correo == correo and nombre is None and apellido is None and telefono is None and contraseña is None:
                nodo_actual.dato.rol = rol
                return 'Modificación "REALIZADA"'
            nodo_actual = nodo_actual.siguiente
        return 'El Usuario del correo:', correo, 'no se encontró'         

    def imprimir_PelisFavoritas(self,correo):
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            if nodo_actual.dato.correo == correo:
                print('------------------------------------------')
                print(nodo_actual.dato.titulo)
            nodo_actual = nodo_actual.siguiente

    def checkear(self, correo):
        if self.esta_vacia():
            return True
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            if nodo_actual.dato.correo == correo:
                return False
            nodo_actual = nodo_actual.siguiente
        return True