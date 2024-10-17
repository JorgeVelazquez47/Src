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
Metodo range para generar facilmente seria de numeros
"""
for value in range(1,5):
    print(value)

numbers = list(range(1,6))
print(numbers)
numbers_ev = list(range(2,11,2))
print(numbers_ev)