from ArchivosXML.xml_Lectura import *
import os

def limpiar():
    os.system('cls')

class menu_cliente:
    def opcion1(correo):
        limpiar()
        print('------------------------------------------')
        print('Listado de "CATEGORIAS DE PELICULAS"')
        acceso = lista_Categoria.imprimir_Categorias()
        if acceso is True:
            print('------------------------------------------')
            genero = input('Ingrese categoria para ver pelíuculas "DISPONIBLES": ')
            if lista_Categoria.chec_Categoria_Eliminar(genero) is True:
                    limpiar()
                    print('------------------------------------------')
                    print('"CATERGORIA NO EXISTE"')
            else:
                lista_Categoria.imprimir_peli1(genero)
                print('------------------------------------------')
                desicion = input('Escriba "SI" para agregar pelicula\n favoritas "NO" para salir: ')
                if desicion.upper() == "SI":
                    print('------------------------------------------')
                    pelicula = input('Ingrese nombre de su Película "FAVORITA": ')

                    if lista_Categoria.cate_Fav(genero, pelicula) == True:
                        data = peliculasFavorita(correo, pelicula)
                        peliculas_Favoritas.agregar_al_final(data)
                        limpiar()
                        print('------------------------------------------')
                        print('"PELÍCULA FAVORITA AGREGADA"')
                    else:
                        limpiar()
                        print('------------------------------------------')
                        print('"NO SE ENCONTRO LA PELÍCULA"')
                else:
                    limpiar()

    def opcion2(correo):
        limpiar()
        check = peliculas_Favoritas.checkear(correo)
        if check == True:
            limpiar()
            print('------------------------------------------')
            print('"NO TIENE PELICULAS FAVORITAS"')
        else:
            peliculas_Favoritas.imprimir_PelisFavoritas(correo)

    def opcion3():
        pass

    def opcion4():
        pass

    def Principal_Cliente(self, name, correo):
        print('------------------------------------------')
        print('Bienvenido '+'"'+name+'"')
        opc = 0
        while opc != 5:
            print('------------------------------------------')
            print('1. Ver listado de "PELÍCULAS"')
            print('2. Listado de películas "FAVORITAS"')
            print('3. compra de "BOLETOS"')
            print('4. "HISTORIAL" de boletos comprados')
            print('5. para "REGRESAR"')
            print('------------------------------------------')
            try:
                opc = int(input('"Ingrese su opción": '))
                if opc == 1:
                    menu_cliente.opcion1(correo)
                elif opc == 2:
                    menu_cliente.opcion2(correo)
                elif opc == 3:
                    menu_cliente.opcion3()
                elif opc == 4:
                    menu_cliente.opcion4()
                elif opc == 5:
                    limpiar()
                else:
                    limpiar()
                    print('------------------------------------------')
                    print('Ingrese Valores dentro del "RANGO"')
            except:
                limpiar()
                print('------------------------------------------')
                print('Ingrese valores "VALIDOS"')
                print('------------------------------------------')
