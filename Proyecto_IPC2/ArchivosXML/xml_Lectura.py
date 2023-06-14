import xml.etree.ElementTree as ET
from Clases.DatosUsuario import * 
from Clases.DatosPelicula import *
from Clases.DatosCategoria import *
from Listas.ListaEnlazada import *
from Listas.ListaCircular import *
lista_Usuarios = listaEnlazada()
lista_Categoria = ListaDobleCircular()
lista_Pelicula = ListaDobleCircular()

class Xlectura:
    def leerUsuarios(self, ruta):
        self.tree = ET.parse(ruta)
        self.root = self.tree.getroot()

        rol, nombre, apellido, telefono, correo, contraseña = "","","","","",""
        for user in self.root.findall('usuario'):
            rol =  user.find('rol').text
            nombre =  user.find('nombre').text
            apellido =  user.find('apellido').text
            telefono =  user.find('telefono').text
            correo =  user.find('correo').text
            contraseña =  user.find('contrasena').text
            
            datos = datos_usuario(rol, nombre, apellido, telefono, correo, contraseña)
            lista_Usuarios.agregar_al_final(datos)
    
    def leerCateyPeli(self, ruta):

        self.tree = ET.parse(ruta)
        self.root = self.tree.getroot()

        global lista_Pelicula

        nombreCat = ""
        titulo, director, anio, fecha, hora = "","","","",""

        for cate in self.root.findall('categoria'):
            nombreCat = cate.find('nombre').text

            self.movies = cate.find('peliculas')

            for peli in self.movies.findall('pelicula'):
                titulo = peli.find('titulo').text
                director = peli.find('director').text
                anio = peli.find('anio').text
                fecha = peli.find('fecha').text
                hora = peli.find('hora').text

                datos = peliculas(titulo, director, anio, fecha, hora)
                lista_Pelicula.insertar_al_final(datos)

            datosCat = categorias(nombreCat, lista_Pelicula)
            lista_Categoria.insertar_al_final(datosCat)

            lista_Pelicula = ListaDobleCircular()