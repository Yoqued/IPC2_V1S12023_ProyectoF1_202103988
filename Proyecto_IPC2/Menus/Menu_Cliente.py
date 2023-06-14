import os

def limpiar():
    os.system('cls')

class menu_cliente:
    def opcion1(self):
        print('Buenas noches maestro')

    def opcion2(self):
        pass

    def opcion3(self):
        pass

    def opcion4(self):
        pass

    def Principal_Cliente(self, name):
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
                    menu_cliente.opcion1()
                elif opc == 2:
                    menu_cliente.opcion2()
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
