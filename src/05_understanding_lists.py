"""
Las listas nos permiten almacenar informacion en un lugar
la cantidad que queremos: ya sean pocos elementos o 
miles de elementos
"""
#En python los corchetes indican una lista, sus elemtnos 
#se separa por comas, ejemplo
bycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bycles) 
#Imprimiendo el primer elemento de la lista
print(bycles[0])
#Imprimiendo un metodo del primer elemento de la lista
print(bycles[0].upper())

print(bycles[3])
print(bycles[2])
#Imprimiendo el ultimo elemento de la lista
print(bycles[-1])
#Imprimiendo ultimos dos numeros de la lista
print(bycles[-1], bycles[-2])

#Concatenacion
message = "Mi primer bicicleta fue una " + bycles[0]
print(message)

#Fstrings
message1 = f"mi primer bicicleta fue una {bycles[-3]}"
print(message1)

"""
EJERCICIO
1_Almacena de tus algunos de tus amigos en 
una lista llamada names
Imprime el nombre de tus amigos de uno por uno
accediendo al elemento de la lista
2_Utilizando la lista anterior imprime el nombre 
de la persona agregandole un mensaje
El texto del mensaje debe ser el mismo, 
pero cada mensaje debe estar personalizado con el nombre de la persona
3_Crea una lista con tus metodos de transporte.uTliza la lista para 
imprimir una seria de mansajes sobre cada elemento de la lista, ejemplo
'Me gustaria tener un auto tesla
"""
print("EJERCICIO 1")
print("---------------------------------------")
names = ['Ezequiel', 'Jose', 'Derik','Orly', 'Uvaldo']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])

print("EJERCICIO 2")
print("---------------------------------------")

names1 = f"A {names[0]} le aburre la clase de tirado"
names2 = f"A {names[1]} le aburre la clase de tirado"
names3 = f"A {names[2]} le aburre la clase de tirado"
names4 = f"A {names[3]} le aburre la clase de tirado"
names5 = f"A {names[4]} le aburre la clase de tirado"
print(names1)
print(names2)
print(names3)
print(names4)
print(names5)

print("EJERCICIO 3")
print("---------------------------------------")
cars =['Tesla','camaro','gtr','mustang']
car1 = f"{cars [0]} son carros electricos"
car2 = f"El {cars [1]} es un buen carro"
car3 = f"El {cars [2]} es un carro japones"
car4 = f"El {cars [3]} es un carro americano"
print(car1)
print(car2)
print(car3)
print(car4)

print("CLASE")
print("---------------------------------------")
motorcycles = ['honda','ducati']
print(motorcycles)
motorcycles.append("Kawasaki")
motorcycles.append("Yamaha")
print(motorcycles)

motorcycles.insert(2, "ktm")
print(motorcycles)
 
"""
Metodo 
del -> Eliminar elementos de una lista so 
conocemos el indice de elemento que deseamos borrar
"""
del motorcycles[0]
print(motorcycles)
"""
Metodo pop
-Elimina el ultimo de la lista
pero tambien me permite utilizar el elemento despues de utiliarlo
"""
deleted_motorcycles = motorcycles.pop()
print(motorcycles)
print (f"Oye eliminaste {deleted_motorcycles}")

motorcycles.pop(0)
print ("ELIMINA LA POSICION QUE SE PONE")
print(motorcycles)
motorcycles.remove("ktm")
print ("ELIMINA LA VARIBALE CON ESE NOMBRE")
print(motorcycles)

"""

    Ordernar Listas
    
    El método sort ordena la lista permanentemente
    
"""
cars = ['bmw', 'audi', 'toyotta']
cars.sort()
print(cars)

# ordenar la lista de manera ordenada en reversa
cars.sort(reverse=True)
print(cars)

"""
    Función built-in sorted
    
    Ordena la lista de manera temporal 

"""
cars = ['bmw', 'audi', 'toyotta']
print("Lista Original")
print(cars)
print("Lista Ordenada")
print(sorted(cars))
print("Lista Original")
print(cars)

"""
    Método reverse
    
    El método reverse de las listas
    invierte la lista de manera permanente

"""
cars.reverse()
print(cars)

"""

    Función built-in len

    Longitud de las listas
    
    El método len nos dice la cantidad
    de elementos que hay en una lista
    
"""

print(len(cars))