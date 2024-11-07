cars=['Supra','Skyline','Eclipse','Rx7']
for car in cars:
    print(car)
    print(car.upper()+ " Este es un carro japones. \n")
    print(f"No puedo esperar para ir al siguiente evento donde este el {car.lower()} \n")
print("Son unos hermosos carros.")  


"""
Crear una lista con tus pizzas favoritas.
(Que contenga al menos 3 elementos)
1-Imprime un mensaje para cada elemento de la lista
2-Agrega un elemento al final de la lista
    Imprime cada elemento de la lista con un for

"""
print("--------------------------------------------------------------------")
print("EJERCICIO")
pizzas=['Hawaiana', 'Peperoni','3 carnes']
for pizza in pizzas:
    print(f"La pizza {pizza} es mi favorita \n.")
pizzas.append("Mexicana")
print(pizzas)
for pizza in pizzas:
    print(pizza.title())


"""
Metodo range para generar facilmente seriE de numeros
"""
for value in range(1,5):
    print(value)

numbers = list(range(1,6))
print(numbers)
numbers_ev = list(range(2,11,2))
print(numbers_ev)

squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)

squares = [value**2 for value in range(1,11)]
print(squares)
"""

    Una list comprehension combina el for loop, la creación
    de nuevos elementos en una sola línea y automáticamente 
    agrega cada nuevo elemento a la lista, es decir, sin
    utilizar el append.

"""
squares_2 = [number**2 for number in range(1,11)]
print(squares_2)
## SLICING O SLICE
players = ['charly', 'doria', 'jose maria', 'valente', 'puga']
print(players[0:3]) 
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])

## Slicing en un for
players = ['charly', 'doria', 'jose maria', 'valente', 'puga']
print("Aquí se presentan los primeros 3 alumnos")
for player in players[0:3]:
    print(player)

## Copia de listas
my_food = ['chilaquiles', 'flatuas de desebrada', 'enfrijoladas']
dorias_favorite_food = my_food[:]
dorias_favorite_food_2 = list(my_food)
dorias_favorite_food_3 = my_food.copy()
my_food.append('sopes')
print(my_food)
print(dorias_favorite_food)


## TUPLAS
# Las tuplas son listas de elemntos que no cambian de tamaños. 
# Las tuplas son listas inmutables
# Se utilizan los () para definir una tupla.
dimensions = (200, 500)

print(dimensions)

print(dimensions[0])
print(dimensions[1])

for dimension in dimensions:
    print(dimension)
    
dimensions = (250, 500)
print(dimensions)

"""

    Ejercicios: 

        1. Utiliza el for loop para imprimir los números del 1 al 20.
        2. Construye una lista de números del 1 al 1000000 y utiliza
            un for para imprimir los números. (En caso de ser necesario 
            utiliza ctrl+c para parar el progra).
        3. Utiliza la lista anterior para saber cual es el mínimo y el 
            máximo de una lista. Suma los números utilizando sum.
        4. Utiliza el tercer argumento de range() para hacer una lista
            que contenga los números pares del 1 al 20. Utiliza un for 
            para imprimir los valores de la lista.
        5. Crea una lista que contenga múltiplos de 3 del 3 al 30. 
            Utiliza un for para imprimir los valores de la lista.
        6. Un número elevado a la tercera potencia es llamado un cubo.
            Por ejemplo, el cubo de 2 se escribe en Python 2**3. Crea
            una lista con los primeros 10 cubos (1^3, 2^3, 3^3, ... , 10^3).
            Utiliza un for para imprimir los valores de la lista.
        7. Utiliza una list comprehension para generar una lista de los 
            primeros 20 cubos. Utiliza un for para imprimir los valores de 
            la lista.
"""
print("---------------EJERCICIO---------------")
for value in range(1,21):
    print(value)
print("---------------EJERCICIO 2---------------")
for value in range(1,101):
    print(value)
print("---------------EJERCICIO 3---------------")
numeros = list(range(1, 101))
minimo = min(numeros)
maximo = max(numeros)
lista=[]
lista.append(minimo)
lista.append(maximo)
suma_total = sum(lista)
print(f"El valor mínimo: {minimo}")
print(f"El valor máximo: {maximo}")
print(f"La suma de todos: {suma_total}")
print("---------------EJERCICIO 4---------------")
numbers_ev = list(range(2,21,2))
for numbers in numbers_ev:
    print(numbers)
print("---------------EJERCICIO 5---------------")
numbers_ev = list(range(3,31,3))
for numbers in numbers_ev:
    print(numbers)
print("---------------EJERCICIO 6---------------")
squares = [value**3 for value in range(1,11)]
print(squares)
print("---------------EJERCICIO 7---------------")
squares = [value**2 for value in range(1,21)]
print(squares)
print("---------------FIN---------------")
"""
    Ejercicios: 
    
        1. Slice: Usa uno de los programas que escribiste en el ejercicio
            anterior, agrega varias líneas al final del programa que hagan lo
            siguiente:
            
            - Imprime el mensaje: Los primeros tres elementos en la lista
                son: Luego usa una rebanada (slice) para imprimir los primeros
                tres elementos de la lista de ese programa.
            - Imprime el mensaje: Tres elementos del medio de la lista son:
                Usa una rebanada para imprimir tres elementos del medio de
                la lista.
            - Imprime el mensaje: Los últimos tres elementos de la lista son:
                Usa una rebanada para imprimir los últimos tres elementos de
                la lista.
        
        2. Mis Pizzas, Tus Pizzas: Comienza con tu programa del Ejercicio de
            las pizzas. Haz una copia de la lista de pizzas y llámala
            friend_pizzas. Luego, haz lo siguiente:

            - Agrega una nueva pizza a la lista original.
            - Agrega una pizza diferente a la lista friend_pizzas.
            - Demuestra que tienes dos listas separadas.
                - Imprime el mensaje: Mis pizzas favoritas son:, y luego usa
                    un bucle for para imprimir la primera lista.
                - Imprime el mensaje: Las pizzas favoritas de mi amigo son:
                    y luego usa un bucle for para imprimir la segunda lista.
                    Asegúrate de que cada nueva pizza esté almacenada en la
                    lista correspondiente.

"""
print("--------------------------------------------------------------------")
print("EJERCICIO")
pizzas=['Hawaiana', 'Peperoni','3 carnes']
for pizza in pizzas:
    print(f"La pizza {pizza} es mi favorita \n.")
pizzas.append("Mexicana")
print(pizzas)
for pizza in pizzas:
    print(pizza.title())
print("---------------EJERCICIO---------------")
juegos = ['Fortnite', 'Warzone', 'Valorant', 'Forza', 'Minecraft']
for juego in juegos[0:3]:
    print(juego)
print("---------------")
for juego in juegos[1:4]:
    print(juego)
print("---------------")
for juego in juegos[2:5]:
    print(juego)
print("---------------EJERCICIO 2---------------")

friend_pizzas = pizzas.copy()
pizzas.append("Pastor")
print("---------------")
print("Lista 1")
for pizza in pizzas:
    print(pizza)
friend_pizzas.append("Orilla de queso")
print("---------------")
print("Lista 2")
for pizza in friend_pizzas:
    print(pizza)
print("---------------")
for pizza in pizzas:
    print(f"Mi pizza favorita son: {pizza}")
print("---------------")
for pizza in friend_pizzas:
    print(f"Las pizzas favoritas de mi amigo son: {pizza}")
"""

    Buffet: Un restaurante "estilo buffet" ofrece solo cinco alimentos 
        básicos. Piensa en cinco alimentos simples y guárdalos en una 
        tupla.

    - Usa un bucle for para imprimir cada alimento que el restaurante 
        ofrece.
    - Intenta modificar uno de los elementos y asegúrate de que Python 
        rechace el cambio.
    - El restaurante cambia su menú, reemplazando dos de los elementos 
        con alimentos diferentes. Agrega un bloque de código que reescriba
        la tupla, y luego usa un bucle for para imprimir cada uno de los 
        elementos del menú revisado.

"""
Buffet = ("Arroz","Espaguetti","Pollo Agridulce","Camarones empanizados","Carne con verduras")
print("Ofrecemos ")
print("---------------")
for comida in Buffet:
    print(f"-{comida}")
Buffet = ("Crema","Sushi","Pollo Agridulce","Camarones empanizados","Carne con verduras")
print("Ofrecemos ")
print("---------------")
for comida in Buffet:
    print(f"-{comida}")