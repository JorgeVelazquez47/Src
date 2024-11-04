personas = {}

while True:
    nombre = input("Introduce tu nombre completo: ")
    
    if nombre.lower() == "datos":
        break
    
    edad = input(f"Introduce tu edad {nombre.title()}: ")
    
    personas[nombre.lower()] = edad
    print(f"Se agregaron los datos a la lista con el nombre de {nombre.title()}.\n")

while True:
    consulta = input("Escribe el nombre de quien deseas buscar: ")
    
    if consulta.lower() == "exit":
        print("Lista cerrada.")
        break
    
    elif consulta in personas:
        print(f"La edad de {consulta} es {personas[consulta.upper()]} años.\n")
    else:
        print("Nombre no encontrado. Asegúrate de ingresarlo correctamente.\n")
