#STRINGS
name = "Jorge Velazquez"
print("Declaramos name = Jorge Velazquez")
print(f"Se imrprime el nombre original {name}")
print(f"Se imprime el nombre original en minusculas {name.lower()}")
print(f"Se imrpime el nombre original en mayusculas {name.upper()}")
print(f"Se imprime el nombre original con la inicial en mayuscula {name.title()}")
print("Declaramos el first name y last name")
first_name = "jorge"
last_name = "velazquez"
full_name = first_name + " " + last_name
print(full_name.title())
print(first_name.title() + " " + last_name.title())
print(full_name.title())
print("hola, " + full_name.title() + "!")
"""
    Eliminacion de espacios en blanco
"""
print("******************************************************************")
programming_language = "  JORGE  "
print(programming_language)
print(programming_language.lstrip())
print(programming_language.rstrip())
print(programming_language.strip())

#NUMBERS
age = 18
message = "Jorge tiene " + str(age) + " años"
message_f_strings = f"Jorge tiene {age} años"
print(message)
print(message_f_strings)

#LIST
carros = ['Tesla','Audi','Cadillac','Ford','Nissan']
print(carros)
carros.append('Chevrolet')
print(carros)
print(carros[0])
carros.insert(0, 'Pagani')
print(carros)

"""
Metodo 
del -> Eliminar elementos de una lista so 
conocemos el indice de elemento que deseamos borrar
"""
del carros[0]
print(carros)
"""
Metodo pop
-Elimina el ultimo de la lista
pero tambien me permite utilizar el elemento despues de utiliarlo
"""
deleted_carros = carros.pop()
print(carros)
print (f"Oye eliminaste {deleted_carros}")

carros.pop(0)
print ("ELIMINA LA POSICION QUE SE PONE")
print(carros)
carros.remove("Nissan")
print ("ELIMINA LA VARIBALE CON ESE NOMBRE")
print(carros)

"""
Ordenamiento de elementos en una lista
"""
print("---Nombres---")
names = ["Orlando","Jose", "Uvaldo", "Derik"]
print(names)
elementos_ordenados = sorted(names)
print(elementos_ordenados)
print(names)
 
 #IF STATEMENT
cars = ['bocho', 'lambo', 'ferrari','mustang']
for car in cars:
    if car =='mustang':
     print(car.upper())
    else:
      print(f"No esta en la lista")

cars=['Supra','Skyline','Eclipse','Rx7']
for car in cars:
    print(car)
    print(car.upper()+ " Este es un carro japones. \n")
    print(f"No puedo esperar para ir al siguiente evento donde este el {car.lower()} \n")
print("Son unos hermosos carros.")  

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