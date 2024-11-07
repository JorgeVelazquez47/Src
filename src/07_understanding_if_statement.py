
cars = ['bocho', 'mustang', 'sentra', 'honda', 'gtr', 'mustang']

for car in cars:
    if car == 'mustang':
        pass
        # print(car.upper())
    else:
        pass
        # print(car.title())


"""
    Condicionales - Los condicionales
    son el corazón de un if
"""

# Condicional que tiene como resultado True
car = 'bmw'
print(car == 'bmw')

# Condicional que tiene como resultado False
car = 'Audi'
print(car=='audi')

# Condicional que tiene como resultado True
car = 'Audi'
print(car.lower()=='audi')

# Condicional != para determinar desigualdad
tacos = 'bistek'
print(tacos!='pastor')


## 
age = 18
print(age==18)

answer = 17
print(answer!=42)


age = 21
print(age<21)
print(age<=21)
print(age>21)
print(age>=21)
"""
    Multiple Conditions
"""
age_0 = 22
age_1 = 18
print(age_0>=21 or age_1>=21) # -> arroja True
print(age_0>=21 and age_1>=21) # -> arroja False

print("Don Charly")
####
## if -elif - else
"""
    Costo para una persona: 
        <= 4 años -> entrada gratis
        <= 18 -> paga $200
        mayor de 18 -> $500
"""
age = 3
if age <= 4:
    price = 0
elif age<=18:
    price = 200
elif age <65:
    price = 500
elif age >= 65: 
    price = 100

print(f" Tu entrada cuesta ${price} ")

### If statement 

guisos = ['deshebrada', 'salsa verde']
if 'deshebrada' in guisos:
    print("Hay deshebrada")
if 'salsa verde' in guisos:
    print("Hay salsa verde")
if 'picadillo' in guisos:
    print("Hay picadillo")
print("Éstos son los guisos")

## Differences between elif and if



guisos = ['salsa verde', 'deshebrada']
if 'picadillo' in guisos:
    print("Hay Salsa verde")
elif 'picadillo' in guisos:
    print("Hay deshebrada")
elif 'chicharron' in guisos:
    print("Hay chicharron")  
else:
    print("No hay ningún guiso")  
    

# Empty List
guisos = []
if guisos:
    print("Hay elementos")
else:
    print("No hay elementos")
    

# 
guisos_disponibles = ['salsa verde', 'deshebrada', 
                      'picadillo', 'huevo con chorizo']
guisos_a_ordenar = ['chicharron', 'deshebrada', 'huevo con chorizo']
print("¿Qué guiso desea ordenar?")
for guiso in guisos_a_ordenar:
    if guiso in guisos_disponibles:
        print(f"Si tengo ese guiso: {guiso}")
    else:
        print(f"No tengo ese guiso: {guiso}")


"""

    Ejercicios: 
        
        Pruebas Condicionales: Escribe una serie de pruebas condicionales.
        Imprime una declaración que describa cada prueba y tu predicción 
        para el resultado de cada prueba. Tu código debería verse algo así:
        
            car = 'bocho'
            print("¿Es car == 'bocho'? Predigo que es True.")
            print(car == 'bocho')
            print("\n¿Es car == 'audi'? Predigo que es False.")
            print(car == 'audi')
        
        Observa de cerca tus resultados y asegúrate de entender por qué 
        cada línea se evalúa como True o False. Crea al menos 10 pruebas.
        Haz que al menos 5 pruebas se evalúen como True y otras 5 se evalúen 
        como False.
        

        Más Pruebas Condicionales: No tienes que limitar el número de pruebas
        a 10. Si quieres intentar más comparaciones, escribe más pruebas y 
        añádelas a tu script. Asegúrate de tener al menos un 
        resultado True y un resultado False para cada uno de los siguientes 
        casos:

            - Pruebas de igualdad y desigualdad con strings.
            - Pruebas usando la función lower().
            - Pruebas numéricas que involucren igualdad y desigualdad, mayor 
                que y menor que, mayor o igual que y menor o igual que.
            - Pruebas usando la palabra clave and y la palabra clave or.
            - Prueba si un elemento está en una lista.
            - Prueba si un elemento no está en una lista.

"""
print("---------------EJERCICIO---------------")
car = 'bocho'
print("¿Es car == 'bocho'? Predigo que es False.")
print(car == 'bocho')
car = 'Audi'
print("\n¿Es car == 'audi'? Predigo que es True.")
print(car == 'audi')
car = 'mustang'
print("\n¿Es car == 'mustang'? Predigo que es False.")
print(car == 'r8')
car = 'r8'
print("\n¿Es car == 'r8'? Predigo que es True.")
print(car == 'r8')
car = 'ferrari'
print("¿Es car == '488 pista'? Predigo que es False.")
print(car == 'ferrari')
car = 'maseratti'
print("\n¿Es car == 'maseratti'? Predigo que es True.")
print(car == 'maseratti')
car = 'mustang'
print("\n¿Es car == 'mustang'? Predigo que es False.")
print(car == 'r8')
car = 'r8'
print("\n¿Es car == 'r8'? Predigo que es True.")
print(car == 'r8')
car = 'rolls roys'
print("\n¿Es car == 'Huracan'? Predigo que es False.")
print(car == 'evo')
car = 'evo'
print("\n¿Es car == 'lamborghini evo'? Predigo que es True.")
print(car == 'lamborghini')
print("---------------EJERCICIO---------------")
valor = 12
print("Valor = 12")
print("valor es igual a 11?")
print(valor == 11)
print("valor es menor a 20?")
print(valor < 20)
print("valor es mayor a 1?")
print(valor > 11)
print("valor es igual o menor a 20?")
print(valor == 12)
print("---------------EJERCICIO---------------")
car = 'rolls roys'
print("\n¿Es car == 'rolls roys'? Predigo que es False.")
print(car.upper() == 'ROLLS ROYS')
car = 'Lamborghini'
print("\n¿Es car == 'lamborghini evo'? Predigo que es True.")
print(car.upper() == 'Lamborghini')
"""

    Ejercicios: 
    
        1. Colores de Extraterrestres: Imagina que un extraterrestre acaba de
        ser derribado en un juego. Crea una variable llamada color_alien y 
        asígnale un valor de 'verde', 'amarillo' o 'rojo'.

            Escribe una declaración if para comprobar si el color del 
            extraterrestre es verde. Si lo es, imprime un mensaje indicando que 
            el jugador acaba de ganar 5 puntos. Escribe una versión de este 
            programa que pase la prueba if y otra que no la pase. 

        2. Colores de Extraterrestres : Elige un color para un extraterrestre 
        como hiciste en el ejercicio anterior, y escribe una cadena if-else.

            - Si el color del extraterrestre es verde, imprime una declaración
                que indique que el jugador acaba de ganar 5 puntos por 
                dispararle al extraterrestre.
            - Si el color del extraterrestre no es verde, imprime una 
                declaración que indique que el jugador acaba de ganar 10 
                puntos.
            - Escribe una versión de este programa que ejecute el bloque if y
                otra que ejecute el bloque else.

        3. Colores de Extraterrestres : Convierte tu cadena if-else del 
        ejercicio anterior en una cadena if-elif-else.

            - Si el extraterrestre es verde, imprime un mensaje que indique 
                que el jugador ganó 5 puntos.
            - Si el extraterrestre es amarillo, imprime un mensaje que indique
                que el jugador ganó 10 puntos.
            - Si el extraterrestre es rojo, imprime un mensaje que indique 
                que el jugador ganó 15 puntos.
            - Escribe tres versiones de este programa, asegurándote de que 
            cada mensaje se imprima para el color adecuado del extraterrestre.

        4. Etapas de la Vida: Escribe una cadena if-elif-else que determine la
        etapa de la vida de una persona. Asigna un valor a la variable edad 
        y luego:

            - Si la persona tiene menos de 2 años, imprime un mensaje que 
                indique que es un bebé.
            - Si la persona tiene al menos 2 años pero menos de 4, imprime un
                mensaje que indique que es un niño pequeño.
            - Si la persona tiene al menos 4 años pero menos de 13, imprime un
                mensaje que indique que es un niño.
            - Si la persona tiene al menos 13 años pero menos de 20, imprime 
                un mensaje que indique que es un adolescente.
            - Si la persona tiene al menos 20 años pero menos de 65, imprime 
                un mensaje que indique que es un adulto.
            - Si la persona tiene 65 años o más, imprime un mensaje que 
                indique que es un anciano.

        5. Fruta Favorita: Haz una lista de tus frutas favoritas y luego 
        escribe una serie de declaraciones if independientes que verifiquen 
        si ciertas frutas están en tu lista.

            Haz una lista de tus tres frutas favoritas y llámala 
            frutas_favoritas. Escribe cinco declaraciones if. Cada una debe
            comprobar si cierto tipo de fruta está en tu lista. Si la fruta 
            está en tu lista, el bloque if debe imprimir un mensaje, como 
            "¡Realmente te gustan las fresas!"

"""
color_alien = "verde"
print("---------------EJERCICIO---------------")

if color_alien == 'verde':
    print("Mataste un alien verde")
    print("Ganaste 5 puntos")
print("---------------EJERCICIO---------------")
if color_alien == 'rojo':
    print("Mataste un alien verde")
    print("Ganaste 5 puntos")
else:
    print("Mataste un alien ")
    print("Ganaste 10 puntos")
print("---------------EJERCICIO---------------")
if color_alien == 'rojo':
    print("Mataste un alien verde")
    print("Ganaste 5 puntos")
elif color_alien == 'rojo':
    print("Mataste un alien amarillo")
    print("Ganaste 10 puntos")
else:
    print("Mataste un alien rojo")
    print("Ganaste 15 puntos")



print("---------------EJERCICIO---------------")
edad = 18
if edad < 2:
    print("Es un bebe")
elif edad < 4:
    print("Es un niño pequeño.")
elif edad < 13:
    print("Es un niño.")
elif edad < 20:
    print("Es un adolescente.")
elif edad < 65:
    print("Es un adulto.")
else:
    print("Es un anciano.")

print("---------------EJERCICIO---------------")
frutas_favoritas = ['manzana', 'platano', 'sandia']

if 'manzana' in frutas_favoritas:
    print("Me gustan las manzanas")

if 'platano' in frutas_favoritas:
    print("me gustan los platanos!")

if 'sandia' in frutas_favoritas:
    print("me gusta la sandia!")

"""

    Ejercicios.

    1. Hola Administrador: Haz una lista de cinco o más nombres de usuario, 
    incluyendo el nombre 'admin'. Imagina que estás escribiendo un código 
    que imprimirá un saludo a cada usuario después de que inicien sesión en un
    sitio web. Recorre la lista e imprime un saludo para cada usuario:

        -Si el nombre de usuario es 'admin', imprime un saludo especial, como:
            "Hola admin, ¿te gustaría ver un informe de estado?" 
        De lo contrario, imprime un saludo genérico, como: 
            "Hola Eric, gracias por iniciar sesión nuevamente."
    
    2. Sin Usuarios: Agrega una prueba if para asegurarte de que la lista de
    usuarios no esté vacía.

        - Si la lista está vacía, imprime el mensaje 
            "¡Necesitamos encontrar algunos usuarios!".
        - Elimina todos los nombres de usuario de tu lista y asegúrate de que
            se imprima el mensaje correcto.

    3. Comprobando Nombres de Usuario: Haz lo siguiente para crear un programa
    que simule cómo los sitios web aseguran que cada usuario tenga un nombre
    único.

        - Crea una lista de cinco o más nombres de usuario llamada 
            usuarios_actuales.
        - Crea otra lista de cinco nombres de usuario llamada nuevos_usuarios.
            Asegúrate de que uno o dos de los nuevos nombres de usuario 
            también estén en la lista de usuarios_actuales.
        - Recorre la lista de nuevos_usuarios para ver si cada nuevo nombre
            de usuario ya ha sido usado. Si ya ha sido usado, imprime un 
            mensaje indicando que la persona deberá ingresar un nuevo nombre
            de usuario. Si un nombre de usuario no ha sido usado, imprime 
            un mensaje diciendo que el nombre de usuario está disponible.
        - Asegúrate de que la comparación sea insensible a mayúsculas. 
            Si se ha usado 'Juan', no se debe aceptar 'JUAN'.

"""
print("---------------EJERCICIO---------------")

usuarios = ['admin', 'Jorge', 'Uvaldo', 'Jose', 'Orly']
for usuario in usuarios:
    if usuario == 'admin':
        print("Hola admin, ¿Como te encuentras?")
    else:
        print(f"Hola {usuario.title()}, bienvenido")
print("---------------EJERCICIO 2---------------")
usuarios = []
if usuarios:
    for usuario in usuarios:
        if usuario == 'admin':
            print("Hola admin,  ¿Como te encuentras?")
        else:
            print(f"Hola {usuario.title()}, bienvenido")
else:
    print("¡Necesitamos encontrar algunos usuarios!")

print("---------------EJERCICIO 3---------------")
usuarios = ['derik', 'jorge', 'uvaldo', 'jose', 'orly']

nuevos_usuarios = ['charly', 'UVALDO', 'mercury', 'josefa', 'ORLY']

usuario = [usuario.lower() for usuario in usuarios]

for nuevo_usuario in nuevos_usuarios:
    if nuevo_usuario.lower() in usuario:
        print(f"El nombre de usuario '{nuevo_usuario}' esta en uso elige otro nombre.")
    else:
        print(f"El nombre de usuario '{nuevo_usuario}' esta disponible.")
