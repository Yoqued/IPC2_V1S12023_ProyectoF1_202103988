from Clases.DatosUsuario import *
from ArchivosXML.xml_Lectura import *
from Clases.DatosUsuario import *
from Menus.Menu_Admin import *
from Menus.Menu_Cliente import *
import os

def limpiar():
    os.system('cls')


datos = datos_usuario('administrador', 'Raúl', 'Yoque', '31914079', 'yoque6@gmail.com', 'hola')
lista_Usuarios.agregar_al_final(datos)

opciones = 0

while opciones != 4:
    print('--------------Menu Principal--------------')
    print('1. Iniciar Sesión')
    print('2. Registro Usuario')
    print('3. Ver listado de peliculas')
    print('4. Para Salir')
    print('------------------------------------------')
    try:
        opciones = int(input("Ingrese su opción: "))
        if opciones == 1:
            limpiar()
            print('------------------------------------------')
            correoA = input('Correo: ')
            contraA = input('Contraseña: ')
            estadoC, nombreC, rolC = lista_Usuarios.Acceso(correoA, contraA)
            if estadoC == True and rolC == 'cliente':
                limpiar()
                menuCliente = menu_cliente()
                menu_cliente.Principal_Cliente(nombreC)
            elif estadoC == True and rolC == 'administrador':
                limpiar()
                menuAdmin = menu_admin()
                menuAdmin.Principal_Admin(nombreC)
            else:
                limpiar()
                print('------------------------------------------')
                print('"USUARIO NO ENCONTRADO"')

        elif opciones == 2:
            limpiar()
            print('------------------------------------------')
            nombre_user = input('Ingrese su NOMBRE: ')
            apellido_user = input('Ingrese su APELLIDO: ')
            telefono_user = input('Ingrese su TELEFONO: ')
            correo_user = input('Ingres su CORREO: ')
            contra_user = input('Ingrese un CONTRASEÑA: ')
            User_Cliente = datos_usuario('cliente', nombre_user, apellido_user, telefono_user, correo_user, contra_user)
            lista_Usuarios.agregar_al_final(User_Cliente)
            limpiar()
            print('------------------------------------------')
            print('"USUARIO AGREGADO"')
        elif opciones == 3:
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
                    print('------------------------------------------')
                    lista_Categoria.imprimir_peli1(genero)
        elif opciones == 4:
            limpiar()
            print('------------------------------------------')
            print('"QUE PASE FELIZ DÍA"')
            print('------------------------------------------')
        else:
            limpiar()
            print('------------------------------------------')
            print('Ingrese Valores dentro del "RANGO"')
    except:
        limpiar()
        print('------------------------------------------')
        print('Ingrese valores "VALIDOS"')
        print('"Muy buenas noches"')
        print('------------------------------------------')