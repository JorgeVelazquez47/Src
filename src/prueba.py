class Perfil:
    def __init__(self, nombre_completo, edad):
        self.nombre_completo = nombre_completo
        self.edad = edad

    def __str__(self):
        return f"Nombre: {self.nombre_completo}, Edad: {self.edad}"

def main():
    perfiles = []

    while True:
        nombre_completo = input("Ingrese el nombre completo (o escriba 'salir' para terminar): ")
        if nombre_completo.lower() == 'salir':
            break

        try:
            edad = int(input("Ingrese la edad: "))
            perfiles.append(Perfil(nombre_completo, edad))
            print("Perfil agregado exitosamente.\n")
        except ValueError:
            print("Edad no válida. Intente de nuevo.\n")

    print("\nLista de Perfiles:")
    for perfil in perfiles:
        print(perfil)

if __name__ == "__main__":
    main()