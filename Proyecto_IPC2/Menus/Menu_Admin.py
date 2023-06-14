from ArchivosXML.xml_Lectura import *
import os

def limpiar():
    os.system('cls')

class menu_admin:
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
                    nombre_user = input('Ingrese su NOMBRE: ')
                    apellido_user = input('Ingrese su APELLIDO: ')
                    telefono_user = input('Ingrese su TELEFONO: ')
                    correo_user = input('Ingres su CORREO: ')
                    contra_user = input('Ingrese un CONTRASEÑA: ')
                    rol_user = input('Ingrese el ROL: ')
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
        agregar = Xlectura()
        agregar.leerCateyPeli('PelisyCate.xml')

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




