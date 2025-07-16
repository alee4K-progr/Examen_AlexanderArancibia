productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
                      '2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
                      'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
                     'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
                     'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
                     '123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
                     '342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
                     'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
                           }
#productos = {modelo: [marca, pantalla, RAM, disco, GB de DD, procesador, video],}

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
              'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
              'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0],
                 }
#stock = {modelo: [precio, stock],}


def stock_marca():
    marca = input("Ingrese marca a consultar: ")
    encontrada = False

    for clave, valor in productos.items():
        if marca == valor[0]:
            clave_prod = clave
            for clave, valor in stock.items():
                if clave_prod == clave:
                    encontrada = True
                    print(f"El stock es: {valor[1]}")

    if not encontrada:
        print("Marca no encontrada")
        return
    
def busqueda_por_precio():
    while True:
        try:
            p_min = int(input("Ingrese precio minimo: "))
            p_max = int(input("Ingrese precio maximo: "))
        except:
            print("Debe ingresar valores enteros!!")
            break
        if p_min < 249990 and p_max > 749990:
            print("No hay notebooks en ese rango de precios.")
        for clave, valor in stock.items():
            if valor[0] > p_min and valor[0] < p_max:
                clave_prod = clave
                for clave, valor in productos.items():
                    if clave_prod == clave:
                        print(f"Los notebooks entre los precios consultas son: {valor}")
            


def ordenar_productos():
    print("------ Listado de Notebooks Ordenados ------")
    for clave, valor in productos.items():
        print(valor)
        print("-----------------------------------------")


            