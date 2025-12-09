from django.shortcuts import render

# Datos de 5 personajes (reales o ficticios) con su información
characters_data = {
1: {
"name": "Harry Potter",
"image": "characters/harry.jpg",
"quote": "¡Expelliarmus!"
},
2: {
"name": "Darth Vader",
"image": "characters/vader.jpg",
"quote": "Yo soy tu padre."
},
3: {
"name": "Sherlock Holmes",
"image": "characters/sherlock.jpg",
"quote": "Elemental, mi querido Watson."
},
4: {
"name": "Wonder Woman",
"image": "characters/wonder.jpg",
"quote": "En un mundo de mujeres, miedo no hay."
},
5: {
"name": "Goku",
"image": "characters/goku.jpg",
"quote": "¡Kamehameha!"
}
}
def home(request):
# Pasamos la lista de personajes al contexto para la plantilla
context = {"characters": characters_data}
return render(request, "characters/personajes.html", context)
def personatge(request, id):
# Buscar el personaje por id en nuestro diccionario
if id in characters_data:
context = {"character": characters_data[id]}
else:
# Si el id no existe, preparamos contexto de error con mensaje
context = {
"error": True,
6"message": f"Personaje {id} no encontrado"
}
return render(request, "characters/personajes.html", context)