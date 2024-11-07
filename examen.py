"""
1-Ejercicio tipo entrevista
Desifra el mensaje oculto
Se tiene la siguiente lista:
mensaje = ["u","n","e","m","i"," ","t","o"," ","Q","o","a","d","A","R"]

Crea un programa que reemplace:
La latra a/A por la e
La letra e/E por la i 
La tetra i/I por la o 
La letra o/O por la u 
La letra u/U por la a
La letra q/Q por la p
La letra r/R por la s
Muestra al ifnal el mensaje en consola con la funcion print.
Imprime el mensaje que un cucle for por la salda, utiliza el argumento end="" para que no imprima un salto de linea en cada print
"""
mensaje = ["u","n","e","m","i"," ","t","o"," ","Q","o","a","d","A","R"]
for letra in mensaje:
    if letra == "a" or letra  == "A":
        print("e",end="")
    elif letra == "e" or letra == "E":
        print("i",end="")
    elif letra == "i" or letra == "I":
        print("o",end="")
    elif letra == "o" or letra == "O":
        print("u",end="")
    elif letra == "u" or letra == "U":
        print("a",end="")
    elif letra == "q" or letra == "Q":
        print("p",end="")
    elif letra == "r" or letra == "R":
        print("s",end="")
    elif letra == "n" or letra == "N":
        print("n",end="")
    elif letra == "m" or letra == "M":
        print("m",end="")
    elif letra == "t" or letra == "T":
        print("t",end="")
    elif letra == "d" or letra == "D":
        print("d",end="")
    else:
        print(letra, end="")


