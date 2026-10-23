# Diccionario de la informacion sobre los Notebooks {modelo: [marca, pantalla, RAM, disco, GB de DD, procesador, video], ...]
productos = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i7', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i5', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '12GB', 'DD', '1T', 'Intel Core i5', 'integrada'],
    'GF75HD': ['Asus', 15.6, '12GB', 'DD', '1T', 'Intel Core i3', 'Nvidia GTX1050'],
    '123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 7', 'integrada'],
    '342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 5', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 5', 'Nvidia GTX1050'],
};

# Diccionario del stock de los Notebooks {modelo: [precio, stock], ...]
stock = { 
    '8475HD': [387990, 10], '2175HD': [327990, 4], 'JjfFHD': [424990, 1],
    'fgdxFHD': [664990, 21], '123FHD': [290890, 32], '342FHD': [444990, 7],
    'GF75HD': [749990, 2], 'UWU131HD': [349990, 1], 'FS1230HD': [249990, 0],
};

# Funcion para el stock de marca
def stock_marca(marca):
    total = 0
    for modelo, datos in productos.items():
        if datos[0].lower() == marca.lower():
            if modelo in stock:
                total += stock[modelo][1]
    print(f"El stock total para '{marca}' es: {total}");

# Funcion busqueda por precio
def búsqueda_precio(p_min, p_max):
    resultados = [];
    for modelo, datos in productos.items():
        precio = datos[5];
        if (p_min and p_max) and (productos[modelo][1] > 0):
            resultados.append(modelo + '--' + datos[2]);
    if resultados:
        resultados.sort();
        print("--------------------------------------------------------------------");
        print("Los notebooks entre los precios consultas son:");
        print(resultados);
        print("--------------------------------------------------------------------");
    else:
        print("No hay notebooks en ese rango de precios.");

# Funcion de Listado de productos
def ordenar_productos():
    print("------- Listado de Notebooks Ordenados --------");
    print("HP - 8475HD - 8GB(DD) - 1T ");
    print("Acer - 2175HD - 4GB(SSD) - 512GB");
    print("Asus - JjfFHD - 16GB(SSD) - 256GB");
    print("HP - fgdxFHD - 8GB(DD) - 1T");
    print("Asus - GF75HD - 12GB(DD) - 1T");
    print("Acer - 123FHD - 6GB(DD) - 1T");
    print("Acer - 342FHD - 8GB(DD) - 1T");
    print("Dell - UWU131HD - 8GB(DD) - 1T");
    print("------------------------------------------------")




# Programa principal
def main():
    while True:
        print("\n***MENU PRINCIPAL***");
        print("1. Stock marca.");
        print("2. Búsqueda por precio.");
        print("3. Listado de productos.");
        print("4. Salir.");
        print("----------------------------");

        opc = int(input("Ingrese una opcion: "));

        if opc == 1:
            marca = input("Ingrese marca a consultar: ")
            stock_marca(marca);
        elif(opc == 2):
            try:
                p_min = int(input("Ingrese precio minimo: "));
                p_max = int(input("Ingrese precio maximo: "));
                búsqueda_precio(p_min, p_max);
            except ValueError:
                print("Debe ingresar valores enteros!!")
        elif(opc == 3):
            print("------- Listado de Notebooks Ordenados --------");
            print("HP - 8475HD - 8GB(DD) - 1T ");
            print("Acer - 2175HD - 4GB(SSD) - 512GB");
            print("Asus - JjfFHD - 16GB(SSD) - 256GB");
            print("HP - fgdxFHD - 8GB(DD) - 1T");
            print("Asus - GF75HD - 12GB(DD) - 1T");
            print("Acer - 123FHD - 6GB(DD) - 1T");
            print("Acer - 342FHD - 8GB(DD) - 1T");
            print("Dell - UWU131HD - 8GB(DD) - 1T");
            print("------------------------------------------------")
            ordenar_productos;
        elif(opc == 4):
            print("Programa finalizado.");
            break;
        else:
            print("Opcion no valida!");

# Ejecucion del programa
if __name__ == "__main__":
    main();


# Hecho por Bastian Eduardo Echeverria Andrade