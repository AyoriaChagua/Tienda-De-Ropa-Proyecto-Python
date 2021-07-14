from tabulate import tabulate

tabla_tienda = []


def print_table_tienda(data):
    print(tabulate(data, headers="keys", tablefmt="grid"))


def inventarioTi():
    print("=" * 66)
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


def agregarProducto(data, codigo, producto, precio, cant):
    data.append({
        "Codigo": codigo,
        "Tipo de prenda": producto,
        "Precio por menor": precio,
        "Cantidad": cant
    })
    codigo_t = open("codigo_tienda.txt", "a")
    tipo_t = open("tipo_tienda.txt", "a")
    precio_t = open("precio_tienda.txt", "a")
    cantidad_t = open("cantidad_tienda.txt", "a")
    codigo_t.write("\n"+str(codigo))
    tipo_t.write("\n"+str(producto))
    precio_t.write("\n"+str(precio))
    cantidad_t.write("\n"+str(cant))

    return data


def retornar_tabla_tienda():
    return tabla_tienda


def split_input(cls, user_inp):
    vals = user_inp.split(" ")
    print(vals)
    cls.item_code = vals[0]
    cls.item_quantity = int(vals[1])


venta = []
compra_tienda = []
list_compra = []


def print_table(data):
    print(tabulate(data, headers="keys", tablefmt="grid"))


def eliminar_prenda_tienda():
    print("Quitando prenda...")
    cod = int(input("Ingrese el codigo(numero del array) de la prenda a eliminar: "))
    tabla_tienda.pop(cod)
    print_table_tienda(tabla_tienda)
