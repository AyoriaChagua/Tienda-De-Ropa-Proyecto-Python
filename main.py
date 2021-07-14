import Funciones_tienda as funcion_tienda
import Funciones_clientes as funcion_clientes


funcion_tienda.inventarioTi()


while True:
    elecciones = (print("\n|======================|...BIENVENIDO!!!...|=====================|\n"))
    print("<<<<<<<<<<<<|Elija una de las siguientes modalidades|>>>>>>>>>>>>>")
    print(" ")
    print("a)------>Tienda de ropa\n"
          "b)------>Cliente\n"
          "c)------>Salir")
    print("=" * 66)
    eleccion = input("\n  Elija==> ")
    if eleccion == "a":
        minorista = str(input("\nIngrese la contraseña de la tienda==> "))
        while True:
            if minorista == "contraseña":
                print("\nQue desea hacer hoy?\n")
                print(
                    "(1)==> Ver el inventario\n(2)==> Actualizar el precio\n"
                    "(3)==> Eliminar tipo de prenda\n(4)==> Agregar nuevas prendas\n"
                    "(5)==> Abrir grafico estadistico de las ventas registradas diariamente\n"
                    "(6)==> Salir")

                eleccion_m = input("\nElija que hacer==>  ")
                if eleccion_m == "1":
                    tabla_m = funcion_tienda.retornar_tabla_tienda()
                    funcion_tienda.print_table_tienda(tabla_m)
                    continuar = input("presione ENTER para continuar: ")

                elif eleccion_m == "2":
                    funcion_clientes.actualizar()

                    continuar = input("presione ENTER para continuar: ")

                elif eleccion_m == "3":
                    funcion_tienda.eliminar_prenda_tienda()
                    continuar = input("presione ENTER para continuar: ")

                elif eleccion_m == "4":
                    cod = int(input("Ingrese el codigo: "))
                    nom = input("Ingrese el nombre: ")
                    pre = float(input("Ingrese el precio: "))
                    can = int(input("Ingrese la cantidad: "))
                    tabla = funcion_tienda.retornar_tabla_tienda()
                    funcion_tienda.agregarProducto(tabla, cod, nom, pre, can)
                    continuar = input("presione ENTER para continuar: ")

                elif eleccion_m == "5":
                    funcion_clientes.graficar()
                    continuar = input("presione ENTER para continuar: ")

                elif eleccion_m == "6":
                    print("\n SESION CERRADA HASTA LUEGO :)")
                    break
                else:
                    print("\nOpcion invalida vuelva a intentarlo")
            else:
                print("\nContraseña incorrecta..\n")
                continuar = input("presione ENTER para continuar: ")
                break
    if eleccion == "b":
        while True:
            print("==============>>>>¡BIENVENIDO ESTIMADO CLIENTE!<<<<<==============\n"
                  "                     ¿Como podemos ayudarlo?")
            print("")
            print(
                "(1) ==> Mostrar catalogo\n(2) ==> Añadir ropa al carrito\n(3) ==> Quitar prenda del carrito\n(4) ==> Ver compra\n"
                "(5) ==> Salir")

            eleccion_c = input("\nElija que hacer==>  ")
            if eleccion_c == "1":
                print("=" * 65)
                print("             ESTAS SON LAS PRENDAS QUE TENEMOS DISPONIBLES\n"
                      "                          EN NUESTRA TIENDA:")

                catalogo_1 = funcion_tienda.retornar_tabla_tienda()
                funcion_tienda.print_table_tienda(catalogo_1)
                continuar = input("presione ENTER para continuar: ")

            elif eleccion_c == "2":
                while True:
                    funcion_clientes.comprarProducto_de_tienda()
                    continuar_comprando = input("\nDesea seguir comprando SI/NO: ")
                    if continuar_comprando.upper() == "NO":
                        volver = input("Presione ENTER para continuar: ")
                        break
                    elif continuar_comprando.upper() == "SI":
                        print("\nComprando productos")
                    else:
                        print("\nOpcion Invalida :(\n")
                        salir = input("\nPresione ENTER para salir: ")
                        break
            elif eleccion_c == "3":
                funcion_clientes.quitar_del_carrito()
                continuar = input("presione ENTER para continuar: ")

            elif eleccion_c == "4":
                funcion_clientes.imprimir_compra()
                continuar = input("Presione ENTER para continuar: ")

            elif eleccion_c == "5":
                print("\nGracias por su preferencia estimado cliente...\n")
                continuar = input("presione ENTER para continuar: ")
                break
            else:
                print("\nOpcion invalida")
                continuar = input("\npresione ENTER para continuar y volver a intentarlo: ")
    elif eleccion == "c":
        print("\nHASTA LUEGO! vuelva pronto ☻")
        break
