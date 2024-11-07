"""
STRINGS
Un string es de manera sencilla una seria de caracteres
En python todo lo que se encuentre dentro de comillas simples ""
o comillas dobles "" es considerdo un string
    "Esto es un string"
    'Esto tabien es un string'
    'Le dije a un amigo, "Python es mi lenguage favorito"
    "El lenguage 'PYTHON' lleva el nombre por Monty Python, no por la serpiente"
"""
name = "clase de programacion"
print (name)   
""" SE IMPRIME NOMBRE"""
print(name.title())     
"""SE IMPRIME NOMBRE CADA INICAL DE LA PALABRA EN MAYUSCULA"""

"""
Un metodo es una accion que python puede realizar
en un fragmento de datos  sobre una variable 

El punto . despues de la variable 
seguido del metodo () dice que se tiene 
que ejecutar el metodo title de la variable name

Todos los metodos van seguidos de parentesis
por que en ocasiones necesitan informacion adicional
para funcionar, locual iria dentro de los parentesis.
En esta ocasion el metodo .title() no se requiere informacion 
adicional para funcionar
"""
print (name.upper())
"""
SE IMPRIME NAME EN MAYUSCULAS
"""
print (name.lower())
"""
SE IMPRIME NAME EN MINUSCULAS
"""

print("----------------------------")
print("Clase 104 o 75011")
"""
Concatenacion de caracteres
"""
first_name = "jorge"
last_name = "velazquez"
full_name = first_name + " " + last_name
print(full_name)
print(first_name + " " + last_name)
print(full_name)
print("hola, " + full_name.title() + "!")

"""
    Whitespaces - Se refiere a cualquier caracter que no se imprime,
    es decir, un espacio, un tabulador y final de linea. Los whitespaces 
    se utilizan comunmente para organizar las salidas, de tal manera que 
    sea mas amigable de leer o ver para los usuarios
"""
print("\t\t\tPython")
"""
SE IMPRIME PYTHON CON CIERTA CANTIDAD DE TAB
"""
print("Lenguajes: \nPython\nC\nJavascript")
"""
SE IMPRIME PYTHON,C,JAVASCRIPT EN FORMATO DE LISTA
"""

"""
    Eliminacion de espacios en blanco
"""
print("******************************************************************")
programming_language = "  PYTHON  "
print(programming_language)
print(programming_language.lstrip())
print(programming_language.rstrip())
print(programming_language.strip())


message = "Una fortaleza de Python es su comunidd y sus alumnos de la upv"
message = "Una fortaleza de 'Python' es su comunidad y sus alumnos de la upv"
print(message)

"""
Ejercicio
Guarda el nombre de una persona en una veriable e imprime un mensaje de bienvenida a esa persona

Guarda el nombre de una persona en una variable e imprime 
su nombre en minusculas, mayusculas y utilizando el metodo title

Encuentra una cita de alguna persona famosa. Imprime la cita
el nombre del autor por ejemplo:
"Charly Mercury una vez dijo, 'Python is love"

Repite el ejercicio anterior, pero ahora almacerna el nombre
de la persona famosa en una variable famous_person. Ahora
eres crea la variable para la cita e imprime el mensaje

Guarda el nombre de la persona en una variable, agrega espacios
 tabuladores, saltos de linea, imprime el nombre, despues
 el nombre varias veces utilizando los metodos rstrip, strip, strip

"""
"""1er Ejercicio"""
print("---------------EJERCICIO---------------")
print("EJERCICIO 1")
full_name1 = "jorge velazquez"
print("Hola!, " + full_name1 +  " " + "Bienvenid@")

"""2do Ejercicio"""
print("------------------------------")

print("EJERCICIO 2")
print(full_name1.lower())
print(full_name1.upper())
print(full_name1.title())

"""3ro Ejercicio"""
print("------------------------------")

print("EJERCICIO 3")
phrase = "Harrison Ford alguna vez dijo 'Que la fuerza te acompañe'"
print(phrase)

"""4to Ejercicio"""
print("------------------------------")

print("EJERCICIO 4")
famous_person = "Harrison Ford alguna vez dijo"
phrase1 = "'Que la fuerza te acompañe'"
print(famous_person + " " + phrase1)
print("------------------------------------------------")
message3 = f"{famous_person}  {phrase1}"
print(message3)

"""5to Ejercicio"""
print("------------------------------")

print("EJERCICIO 5")
full_name2 = "  isis lopez     "
print(full_name2)
print(full_name2.rstrip())
print(full_name2.lstrip())
print(full_name2.strip())