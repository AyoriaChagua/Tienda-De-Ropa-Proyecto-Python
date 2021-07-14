from tabulate import tabulate
from datetime import datetime
import matplotlib.pyplot as plt

now = datetime.now()
fecha_actual = now.strftime("%Y-%m-%d")
hora_actual = now.strftime("%H:%M:%S")


def graficar():
    plt.pie(lineas_regisV, labels=lineas_regisF, autopct="%0.1f %%")
    plt.show()


regis_Fe = open("regisF.txt", "a")
regis_Ve = open("regisV.txt", "a")

carrito_de_compras = []
catalogo = []
tabla_tienda = []

registro_de_ventas = open("registro_estadistico.txt", "r")
codigo_t = open("codigo_tienda.txt", "r")
tipo_t = open("tipo_tienda.txt", "r")
precio_t = open("precio_tienda.txt", "r")
cantidad_t = open("cantidad_tienda.txt", "r")
lineas_codigo_t = codigo_t.readlines()
lineas_tipo_t = tipo_t.readlines()
lineas_precio_t = precio_t.readlines()
lineas_cantidad_t = cantidad_t.readlines()
contar_elementos_t = int(len(lineas_codigo_t))
for iterador in range(contar_elementos_t):
    codigo_tienda = lineas_codigo_t[iterador].strip()
    tipo_tienda = lineas_tipo_t[iterador].strip()
    precio_tienda = lineas_precio_t[iterador].strip()
    cantidad_tienda = lineas_cantidad_t[iterador].strip()
    tabla_tienda.append({"Codigo": codigo_tienda, "Tipo de prenda": tipo_tienda, "Precio por menor": precio_tienda,
                         "Cantidad": cantidad_tienda})

# Circulo estadistico de las ventas realizadas--------------------------------------------------

leer_regisV = open("regisV.txt", "r")
leer_regisF = open("regisF.txt", "r")
lineas_regisV = leer_regisV.readlines()
lineas_regisF = leer_regisF.readlines()
contar_elementos = int(len(lineas_regisV))
for iterador_2 in range(contar_elementos):
    registro_F = lineas_regisF[iterador_2].strip()
    registro_V = lineas_regisV[iterador_2].strip()
# ----------------------------------------------------------------------------------------------


def print_table_data(data):
    print(tabulate(data, headers="keys", tablefmt="grid"))


def mostrar_catalogo():
    return catalogo


def updatprice_tienda(index, nuevo_precio):
    precio_actual = lineas_precio_t
    precio_actual[index] = str(nuevo_precio) + "\n"
    new_file_price = open("precio_tienda.txt", "w")
    new_file_price.writelines(precio_actual)
    tabla_tienda[index]["Precio por menor"] = nuevo_precio


def actualizar():
    codigo_id = int(input("\nIngrese el codigo de la prenda: "))
    nuevo_precio = int(input("\nIngrese el nuevo precio: "))
    updatprice_tienda(codigo_id, nuevo_precio)


def updatestock_tienda(indice, nuevo_stock):
    cantidades_actuales = lineas_cantidad_t
    cantidades_actuales[indice] = str(nuevo_stock) + "\n"
    nuevo_file_stock = open("cantidad_tienda.txt", "w")
    nuevo_file_stock.writelines(cantidades_actuales)
    tabla_tienda[indice]["Cantidad"] = nuevo_stock


def comprarProducto_de_tienda():
    codigo_id = int(input('\nIngrese el codigo de la prenda: '))
    cantidad_compra = int(input('\nIngrese la cantidad: '))
    tipo_comp = tabla_tienda[codigo_id]
    new_stock = int(tipo_comp['Cantidad']) - cantidad_compra
    pago = float(tipo_comp['Precio por menor']) * cantidad_compra
    updatestock_tienda(codigo_id, new_stock)
    carrito_de_compras.append({"Codigo": codigo_id, "Cantidad": cantidad_compra, "Monto": pago})
    sumaTotal = 0
    for j in carrito_de_compras:
        suma1 = j["Monto"]
        sumaTotal = sumaTotal + suma1
    subtotal = sumaTotal
    IGV = subtotal * 0.18
    ganancia = subtotal - IGV
    fecha = str(fecha_actual)
    hora = str(hora_actual)
    # Escrbir en el registro de venta(no boleta)-------------------------------------------------
    regis_Fe = open("regisF.txt", "a")
    regis_Ve = open("regisV.txt", "a")
    regis_Fe.write(str(fecha) + "\n")
    regis_Ve.write(str(ganancia) + "\n")
    # Factura------------------------------------------------------------------------------------

    mi_archivo = open("factura.txt", "w")
    mi_archivo.write(str("-" * 44) + "\n")
    mi_archivo.write("----------------| De MODA |----------------")
    mi_archivo.write("\n          Av. Los Chancas\n")
    mi_archivo.write("       Sta Anita - Lima -Peru\n")
    mi_archivo.write("                          Hora: " + str(hora) + "\n")
    mi_archivo.write("\nDNI del cliente:   3277472")
    mi_archivo.write("\nNombre del cliente: Cuellar, Andrew")
    mi_archivo.write("\nFecha: " + str(fecha) + "\n" + "\n")
    mi_archivo.write("\nSubtotal : " + "S/" + str(subtotal) + "\n")
    mi_archivo.write("IGV(18%) : " + "S/" + str(round(IGV, 1)) + "\n")
    mi_archivo.write("Pago Total : " + "S/" + str(ganancia) + "\n")
    mi_archivo.write("--------------------------------------------")
    mi_archivo.write("\nEstimado cliente, encaso de cualquier tipo\n"
                     "de reclamos acercarse a la tienda con su \n"
                     "comprobante de compra y se le atendera con\n"
                     "mucho gusto")

    return


def quitar_del_carrito():
    print("Quitando prenda...")
    cod = int(input("Ingrese el codigo de la prenda a eliminar: "))
    carrito_de_compras.pop(cod)


def imprimir_compra():
    print_table_data(carrito_de_compras)
