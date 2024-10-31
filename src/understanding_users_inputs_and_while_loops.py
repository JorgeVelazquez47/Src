"""
User Inputs
El metodo buil-in input permite obtener informacion 
del ususario
input(argumento)-> string
"""

inicio = input("Presiona enter: ")
if inicio == "":
    print(inicio)

else:
    inicio = input("Presiona enter: ")
prompt = "Introduce tu nombre:"
name = input(prompt)
print(f"¡Bienvenid@! {name.title().lstrip()}")

while True:
        try:
            edad = int(input("Por favor, ingresa tu edad: "))
            
            if edad >= 18:
                print("Eres mayor de edad.")
                ciudad = "Introduce tu ciudad:"
                city = input(ciudad)
                print(f"Ciudad de origen {city.title().lstrip()}")

            else:
                print("Eres menor de edad.")
            break  # Salir del bucle si la entrada es válida y se ha dado una respuesta
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número entero.")
gustos="Que te gusta hacer en tu tiempo libre?"
pasatiempo = input(gustos)
print(f"En mis tiempos libres me gusta {pasatiempo.lower().lstrip()}")
estudios = input("Estudias actualmente?")
if estudios.lower() == 'si':
     print ("Excelente")
     where= input("Donde estudias actualmente?:")
     print(f"Muy bien actualmente estudias en {where}")
else:
     print("Pongase a estudiar ")