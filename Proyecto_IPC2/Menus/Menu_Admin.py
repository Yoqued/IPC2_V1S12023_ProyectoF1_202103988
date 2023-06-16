from ArchivosXML.xml_Lectura import *
import os

def limpiar():
    os.system('cls')

class menu_admin:
    def modificar_Peli():
        print('-----------------------------------------------------')
        cate = input('Ingrese categoria a la que quiere modificar una "PELICULA": ')
        if lista_Categoria.chec_Categoria_Eliminar(cate) is True:
            limpiar()
            print('------------------------------------------')
            print('"CATERGORIA NO EXISTE"')
        else:
            print('------------------------------------------')
            lista_Categoria.imprimir_peli1(cate)
            print('------------------------------------------')
            peli = input('Ingrese pelicula a "MODIFICAR": ')
            limpiar()
            opc = 0
            while opc != 6:
                print('------------------------------------------')
                print('1. Para cambiar "TITULO"')
                print('2. Para cambiar "DIRECTOR"')
                print('3. Para cambiar "AÑO"')
                print('4. Para cambiar "FECHA"')
                print('5. Para cambiar "HORA"')
                print('6. para "REGRESAR"')
                print('------------------------------------------')
                try:
                    opc = int(input('"Ingrese su opción": '))
                    if opc == 1:
                        limpiar()
                        ('------------------------------------------')
                        titulo = input('Ingrese Titulo "MODIFICAR": ')
                        lista_Categoria.buscar_categoria_pelicula(cate, peli, None, None, None, None, titulo)
                        opc = 6
                        limpiar()
                        print('------------------------------------------')
                        print('"TITULO MODIFICADO"')
                        print('Por modifcar TITULO no podra seguir editando \n mas aspectos de la película')
                    elif opc == 2:
                        limpiar()
                        ('------------------------------------------')
                        director = input('Ingrese Director "DIRECTOR": ')
                        lista_Categoria.buscar_categoria_pelicula(cate, peli, director, None, None, None, None)
                        limpiar()
                        print('------------------------------------------')
                        print('"DIRECTOR MODIFICADO"')
                    elif opc == 3:
                        limpiar()
                        ('------------------------------------------')
                        anio = input('Ingrese Año "AÑO": ')
                        lista_Categoria.buscar_categoria_pelicula(cate, peli, None, anio, None, None, None)
                        limpiar()
                        print('------------------------------------------')
                        print('"AÑO MODIFICADO"')
                    elif opc == 4:
                        limpiar()
                        ('------------------------------------------')
                        fecha = input('Ingrese Fecha "FECHA": ')
                        lista_Categoria.buscar_categoria_pelicula(cate, peli, None, None, fecha, None, None)
                        limpiar()
                        print('------------------------------------------')
                        print('"FECHA MODIFICADA"')
                    elif opc == 5:
                        limpiar()
                        ('------------------------------------------')
                        hora = input('Ingrese "HORA": ')
                        lista_Categoria.buscar_categoria_pelicula(cate, peli, None, None, None, hora, None)
                        limpiar()
                        print('------------------------------------------')
                        print('"HORA MODIFICADA"')
                    elif opc == 6:
                        limpiar()
                    else:
                        limpiar()
                except:
                    limpiar()
                    print('------------------------------------------')
                    print('Ingrese valores "VALIDOS"')
                    print('------------------------------------------')

    def modifi_User():
        limpiar()
        option = 0
        while option != 6:
            print('------------------------------------------')
            correo = input('Ingrese el correo del usuario a moodificar: ')
            print('------------------------------------------')
            print('1. Para cambiar "NOMBRE"')
            print('2. Para cambiar "APELLIDO"')
            print('3. Para cambiar "TELEFONO"')
            print('4. Para cambiar "CONTRASEÑA"')
            print('5. Para cambiar "ROL"')
            print('6. para "REGRESAR"')
            print('------------------------------------------')
            try:
                option = int(input('"Ingrese su opción": '))
                if option == 1:
                    limpiar()
                    ('------------------------------------------')
                    name = input('Ingrese Nombe a "Modificar": ')
                    print(lista_Usuarios.modificar_dato(None, name, None, None, correo, None))
                elif option == 2:
                    limpiar()
                    ('------------------------------------------')
                    last_name =  input('Ingrese Apellido a "Modificar": ')
                    print(lista_Usuarios.modificar_dato(None, None, last_name, None, correo, None))
                elif option == 3:
                    limpiar()
                    ('------------------------------------------')
                    cellphone =  input('Ingrese Teléfono a "Modificar": ')
                    print(lista_Usuarios.modificar_dato(None, None, None, cellphone, correo, None))
                elif option == 4:
                    limpiar()
                    ('------------------------------------------')
                    password =  input('Ingrese Contraseña a "Modificar": ')
                    print(lista_Usuarios.modificar_dato(None, None, None, None, correo, password))
                elif option == 5:
                    limpiar()
                    ('------------------------------------------')
                    rol =  input('Ingrese Rol a "Modificar": ')
                    print(lista_Usuarios.modificar_dato(rol, None, None, None, correo, None))
                elif option == 6:
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


    def opcion1():
        opc = 0
        while opc != 5:
            print('------------------------------------------')
            print('1. Crear "USUARIO"')
            print('2. Leer archivo de "USUARIOS"')
            print('3. Modificar "USUARIOS"')
            print('4. Eliminar "USUARIOS"')
            print('5. para "REGRESAR"')
            print('------------------------------------------')
            try:
                opc = int(input('"Ingrese su opción": '))
                if opc == 1:
                    limpiar()
                    print('------------------------------------------')
                    nombre_user = input('Ingrese su "NOMBRE": ')
                    apellido_user = input('Ingrese su "APELLIDO": ')
                    telefono_user = input('Ingrese su "TELEFONO": ')
                    correo_user = input('Ingres su "CORREO": ')
                    contra_user = input('Ingrese un "CONTRASEÑA": ')
                    rol_user = input('Ingrese el "ROL": ')
                    User_ = datos_usuario(rol_user, nombre_user, apellido_user, telefono_user, correo_user, contra_user)
                    lista_Usuarios.agregar_al_final(User_)
                    limpiar()
                    print('------------------------------------------')
                    print('"USUARIO AGREGADO"')
                elif opc == 2:
                    limpiar()
                    print('------------------------------------------')
                    root = input('ingrese "RUTA" de archivo de Usuarios: ')
                    agregar = Xlectura()
                    agregar.leerUsuarios(root)
                    lista_Usuarios.imprimir_lista()
                elif opc == 3:
                    menu_admin.modifi_User()
                elif opc == 4:
                    limpiar()
                    print('------------------------------------------')
                    correoElimiar = input('Ingrese el correo del usuario a "ELIMINAR": ')
                    limpiar()
                    print('------------------------------------------')
                    print(lista_Usuarios.eliminar(correoElimiar))
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

    def opcion2():
        opc = 0
        while opc != 8:
            print('------------------------------------------')
            print('1. Crear "CATEGORIA"')
            print('2. Modificar "CATEGORIA"')
            print('3. Eliminar "CATEGORIA"')
            print('4. Crear "PELÍCULA"')
            print('5. Modificar "PELÍCULA"')
            print('6. Eliminar "PELÍCULA"')
            print('7. Leer archivo de "CATEGORIAS Y PELICULAS"')
            print('8. para "REGRESAR"')
            print('------------------------------------------')
            try:
                opc = int(input('"Ingrese su opción": '))
                if opc == 1:
                    limpiar()
                    print('------------------------------------------')
                    categoria = input('Ingrese nueva "CATEGORIA"')
                    if lista_Categoria.chec_Categoria(categoria) is True:
                        limpiar()
                        print('------------------------------------------')
                        print('"CATERGORIA YA EXISTE"')
                    else:
                        print('------------------------------------------')
                        print('Para crear categoria debe de Crear una "PELICULA"')
                        print('------------------------------------------')
                        titulo = input('Ingrese "TITULO": ')
                        director = input('Ingrese "DIRECTOR": ')
                        anio = input('Ingrese "AÑO": ')
                        fecha = input('Ingrese "FECHA": ')
                        hora = input('Ingrese "HORA": ')
                        global lista_Pelicula
                        datos = peliculas(titulo, director, anio, fecha, hora)
                        lista_Pelicula.insertar_al_final(datos)
                        datosCat = categorias(categoria, lista_Pelicula)
                        lista_Categoria.insertar_al_final(datosCat)
                        lista_Pelicula = ListaDobleCircular()
                        limpiar()
                        print('------------------------------------------')
                        print('"CATEGORIA AGREGADA"')
                elif opc == 2:
                    limpiar()
                    print('------------------------------------------')
                    print('Listado de "CATEGORIAS DE PELICULAS"')
                    check = lista_Categoria.imprimir_Categorias()
                    if check != False:
                        print('------------------------------------------')
                        cate = input('Ingrese categoria a "MODIFICAR": ')
                        if lista_Categoria.chec_Categoria_Eliminar(cate) is True:
                            limpiar()
                            print('------------------------------------------')
                            print('"CATERGORIA NO EXISTE"')
                        else:
                            limpiar()
                            print('------------------------------------------')
                            new_cate = input('Ingrese el nombre "NUEVO" de la Categoria: ')
                            lista_Categoria.modificar_categoria(cate, new_cate)
                            limpiar()
                            print('------------------------------------------')
                            print('"CATEGORIA MODIFICADA"')
                elif opc == 3:
                    limpiar()
                    print('------------------------------------------')
                    print('Listado de "CATEGORIAS DE PELICULAS"')
                    check = lista_Categoria.imprimir_Categorias()
                    if check != False:
                        print('------------------------------------------')
                        cate = input('Ingrese categoria a "ELIMINAR": ')
                        if lista_Categoria.chec_Categoria_Eliminar(cate) is True:
                            limpiar()
                            print('------------------------------------------')
                            print('"CATERGORIA NO EXISTE"')
                        else:
                            lista_Categoria.eliminarCategoria(cate)
                            limpiar()
                            print('------------------------------------------')
                            print('"CATEGORIA ELIMINADA"')
                elif opc == 4:
                    limpiar()
                    print('------------------------------------------')
                    print('Listado de "CATEGORIAS DE PELICULAS"')
                    acceso = lista_Categoria.imprimir_Categorias()
                    if acceso is True:
                        print('-----------------------------------------------------')
                        cate = input('Ingrese categoria a la que quiere agregar una "PELICULA": ')
                        if lista_Categoria.chec_Categoria_Eliminar(cate) is True:
                            limpiar()
                            print('------------------------------------------')
                            print('"CATERGORIA NO EXISTE"')
                        else:
                            print('------------------------------------------')
                            titulo = input('Ingrese "TITULO": ')
                            director = input('Ingrese "DIRECTOR": ')
                            anio = input('Ingrese "AÑO": ')
                            fecha = input('Ingrese "FECHA": ')
                            hora = input('Ingrese "HORA": ')
                            lista_Categoria.agregar_Peli_a_Cate(cate, titulo, director, anio, fecha, hora)
                            limpiar()
                            print('------------------------------------------')
                            print('"PELÍCULA AGREGADA"')
                elif opc == 5:
                    limpiar()
                    print('------------------------------------------')
                    print('Listado de "CATEGORIAS DE PELICULAS"')
                    acceso = lista_Categoria.imprimir_Categorias()
                    if acceso is True:
                        menu_admin.modificar_Peli()
                elif opc == 6:
                    limpiar()
                    print('------------------------------------------')
                    print('Listado de "CATEGORIAS DE PELICULAS"')
                    acceso = lista_Categoria.imprimir_Categorias()
                    if acceso is True:
                        print('-----------------------------------------------------')
                        cate = input('Ingrese categoria para ver las "PELÍCULAS": ')
                        if lista_Categoria.chec_Categoria_Eliminar(cate) is True:
                            limpiar()
                            print('------------------------------------------')
                            print('"CATERGORIA NO EXISTE"')
                        else:
                            print('------------------------------------------')
                            lista_Categoria.imprimir_peli1(cate)
                            print('------------------------------------------')
                            title = input('Ingrese pelicula a "ELIMINAR": ')
                            limpiar()
                            print('------------------------------------------')
                            print(lista_Categoria.busc_cate_para_Eliminar(cate, title))
                elif opc == 7:
                    limpiar()
                    print('------------------------------------------')
                    root = input('ingrese "RUTA" de archivo de Categorias y Películas: ')
                    agregar = Xlectura()
                    agregar.leerCateyPeli(root)
                    lista_Categoria.imprimir_Categorias()
                elif opc == 8:
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

    def opcion3():
        pass

    def Principal_Admin(self, name):
        print('------------------------------------------')
        print('Bienvenido '+'"'+name+'"')
        opciones = 0
        while opciones != 4:
            print('------------------------------------------')
            print('1. Gestionar "USUARIOS"')
            print('2. Gestionar "CATEGORÍAS Y PELÍCULAS"')
            print('3. Gestionar "SALAS"')
            print('4. para "REGRESAR"')
            print('------------------------------------------')
            try:
                opciones = int(input('"Ingrese su opción": '))
                if opciones == 1:
                    limpiar()
                    menu_admin.opcion1()
                elif opciones == 2:
                    limpiar()
                    menu_admin.opcion2()
                elif opciones == 3:
                    menu_admin.opcion3()
                elif opciones == 4:
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