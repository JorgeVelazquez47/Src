"""

    Diccionarios
    
"""
# How to access to a dictionary element / Como hacer el acceso al dicionario con elementos
covenant_elite = {'color': "blue", 'points': 10}
print(covenant_elite['color'])
print(covenant_elite['points'])

print(covenant_elite)

# How to add elements to a dictionary / como añadir elementos al dicionario
covenant_elite['x-position'] = 0
covenant_elite['y-position'] = 25
covenant_elite['weapon'] = "sword"
print(covenant_elite)

# Empty Dictionary /diccionario vacio

covenant_grunt = {}
print(type(covenant_grunt))

covenant_grunt['color'] = 'orange'
covenant_grunt['points'] = 1

print(covenant_grunt)
covenant_grunt['points'] = 5

print(covenant_grunt)

del covenant_grunt['points']

covenant_grunt['x-position'] = 5
covenant_grunt['y-position'] = 25
covenant_grunt['speed'] = 'slow'

print(covenant_grunt)

if covenant_grunt['speed'] == 'slow':
    x_increment = 1
elif covenant_grunt['speed'] == 'medium':
    x_increment = 10
else:
    x_increment = 20

covenant_grunt['x-position'] = covenant_grunt['x-position'] + x_increment

print(covenant_grunt)


programming_lenguages = {
    'alan': 'python',
    'valente': 'c++',
    'ariel': 'c',
    'yepez': 'Python',
}
print(programming_lenguages['valente'].title())

for nombre, lenguage in programming_lenguages.items():
    print(f"{nombre.title()} le gusta el lenguage: ", lenguage)

"""
    Keys
"""
friends = ['ariel', 'yepez', 'alan', 'valente']
for name in programming_lenguages.keys():
    if name in friends:
        print(f" {name} Hola es un gusto saber que te gusta: {programming_lenguages[name]}" )

if 'charly' not in programming_lenguages.keys():
    print("A charly no le gusta programar")
    
print(programming_lenguages.keys())

for key in programming_lenguages.keys():
    print(key)

for key in sorted(programming_lenguages.keys()):
    print(key)

print()    

for lenguaje in programming_lenguages.values():
    print(lenguaje)
    
print()


for lenguaje in set(programming_lenguages.values()):
    print(lenguaje)


"""
Nesting - Diccionaries in list
"""
chevy_silverado= {'color':'blue','puntos':10}
chevy_camaro = {'color':'rojo','puntos':10}
chevy_corvette = {'color':'blanco', 'puntos':10}
chevys = [chevy_silverado, chevy_camaro, chevy_corvette]
print("Chevys:")
print(chevys)

for chevy in chevys:
    print(chevy)
cheys_fleet= []
for _ in range (30):
    new_chevys={'color':'negro','puntos':10}
    
tacos = {
    "tortillas": ['harina','maiz'],
    "guisos":['bistek','tripa','pastor']
}
print(f"Tu has ordenado unos tacos de {tacos['guisos'][2]} con tortilla de {tacos['tortillas'][0]}")

print("-------------------------------------")
users= {
    "Eltortas":{
        "firstname": "Uvaldo",
        "lastname":"Martinez",
        "age":18,
        "altura": 170,
    }
}
for user, user_info in users.items():
    print(user)
    full_name = user_info["firstname"]+ " " + user_info["lastname"]
    print("\t",full_name,"tiene", f"{user_info['age']}años","y mide: " + f"{user_info['altura']} cm")