
productos = []
print("Cargando sistema...")
print("Bienvenid@")
bienvenida = input("Favor de presionar enter.")
def bienvenida():
    while True:
        print("Seleccione una opcion:")
        print("1- Menu principal")
        print("2- Salir")
        opcion = input(":")
        if opcion == "1" or opcion.lower() == "menu principal" or opcion.lower() == "menu":
            menu()
        elif opcion == "2" or opcion.lower() == "exit" or opcion.lower() == "quit" or opcion.lower() == "salir":
            print("         ¿Seguro que deseas salir?")
            print("  !ꜱᴇ ᴘᴇʀᴅᴇʀᴀɴ ᴛᴏᴅᴏꜱ ʟᴏꜱ ᴅᴀᴛᴏꜱ ᴀʟᴍᴀᴄᴇɴᴀᴅᴏꜱ.!")
            print("     !ᴇꜱᴛᴀ ᴀᴄᴄɪᴏɴ ɴᴏ ꜱᴇ ᴘᴜᴇᴅᴇ ʀᴇᴠᴇʀᴛɪʀ!  ")
            print("1-Si")
            print("2-No")
            opcion= input(":")
            if opcion == "1" or opcion.lower() == "si":
                print("Saliendo...")
                print("Gracias,cerrando sistema")
                break
            elif opcion == "2" or opcion.lower() == "no":
                menu()
        else:
            print("Error, intente nuevamente.")
def menu():
    while True:
        print("Opciones:")
        print("1-Registrar ")
        print("2-Consultar ")
        print("3-Actualizar")
        print("4-Resumen")
        print("5-Salir Del Menu Principal")        
        opcion = input("Seleccione una opcion: ")
        if opcion == "1" or opcion.lower() == "registrar":
            registrar()
        elif opcion == "2" or opcion.lower() == "consultar":
            consultar()
        elif opcion == "3" or opcion.lower() == "actualizar":
            actualizar()
        elif opcion == "4" or opcion.lower() == "resumen":
            resumen()
        elif opcion == "5" or opcion.lower() == "exit" or opcion.lower() == "quit" or opcion.lower() == "salir" or opcion.lower() == "salir del menu principal":
            print("         ¿Seguro que deseas salir?")
            print("  !ꜱᴇ ᴘᴇʀᴅᴇʀᴀɴ ᴛᴏᴅᴏꜱ ʟᴏꜱ ᴅᴀᴛᴏꜱ ᴀʟᴍᴀᴄᴇɴᴀᴅᴏꜱ.!")
            print("     !ᴇꜱᴛᴀ ᴀᴄᴄɪᴏɴ ɴᴏ ꜱᴇ ᴘᴜᴇᴅᴇ ʀᴇᴠᴇʀᴛɪʀ!  ")
            print("1-Si")
            print("2-No")            
            opcion= input(":")
            if opcion == "1" or opcion.lower() == "si":
                print("Saliendo...")
                return
            elif opcion == "2" or opcion.lower() == "no":
                menu()            
        else:
            print("Error, intente nuevamente.")
def registrar():
    while True:
        print("Ingrese el nombre del producto, si quiere regresar al menu escriba menu")
        nombre = input(":").lstrip().strip()
        if nombre.lower() == 'menu':
            break
        try:
            precio = int(input(f"Ingrese el precio de '{nombre.title()}': "))
            productos.append({"nombre": nombre.lower(), "precio": precio})
            print(f"El producto '{nombre.title()}' cuesta ${precio} pesos y se registro en la base de datos.\n")
        except ValueError:
            print("Precio invalido.")
def consultar():
    try:
        print("Ingrese el precio limite")
        limite = int(input(":"))
        productos_en_rango = [producto for producto in productos if producto["precio"] <= limite]
        if productos_en_rango:
            print("Productos:")
            for producto in productos_en_rango:
                print(f"-{producto['nombre'].title()}  Precio: ${producto['precio']}-")
        else:
            print("No hay productos, en este rango de precio")
    except ValueError:
        print("Precio invalido.")

def resumen():
    while True:
        print("Opciones:")
        print("1. Todos")
        print("2. Menor a mayor")
        print("3. Mayor a menor")
        print("4. Menú principal")
        opcion = input("Seleccione una opcion:")
        if opcion == "4" or opcion.lower() == "menu" or opcion.lower() == "menu principal":
            break
        elif opcion == "1" or opcion.lower() == "todos":
            if productos:
                print("Lista de productos:")
                for producto in productos:
                    print(f"Producto: {producto['nombre'].title()}, Precio: ${producto['precio']} pesos.")
        elif opcion == "2" or opcion.lower() == "menor a mayor":
            try:
                limite = int(input("Ingresa el limite: "))
                lista_ordenada = sorted([producto for producto in productos if producto["precio"] <= limite],key=lambda x: x["precio"])
                if lista_ordenada:
                    print("Productos de menor a mayor :")
                    for producto in lista_ordenada:
                        print(f"Producto: {producto['nombre'].title()}, Precio: ${producto['precio']} pesos.")
                else:
                    print("No hay productos ")
            except ValueError:
                print("Valor invalido.")
        elif opcion == "3" or opcion.lower() == "mayor a menor":
            try:
                limite = int(input("Ingresa el limite: "))
                lista_ordenada = sorted([producto for producto in productos if producto["precio"] >= limite],key=lambda x: x["precio"],reverse=True)
                if lista_ordenada:
                    print("Productos de mayor a menor:")
                    for producto in lista_ordenada:
                        print(f"Producto: {producto['nombre'].title()}, Precio: ${producto['precio']} pesos.")
                else:
                    print("No hay productos ")
            except ValueError:
                print("Valor invalido.")
def actualizar():
    while True:
        print("Ingrese el nombre del producto a actualizar o si quiere ingresar al menu escriba MENU")
        dato = input(": ")
        if dato.lower() == 'menu':
            break
        p_actualizar = next((productos for productos in productos if productos["nombre"]== dato.lower()), None)
        if p_actualizar:
            try:
                nuevo = int(input("Introduce el nuevo precio: "))
                p_actualizar["precio"] = nuevo
                print(f"El precio del producto ha sido actualizado a {nuevo} pesos.")
            except ValueError:
                print("Dato invalido")
        else:
            print(f"No se encontro ningun producto con el nombre de '{dato.title()}'.")
bienvenida()