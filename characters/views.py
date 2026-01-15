from django.shortcuts import render

# Diccionario con 5 personajes
PERSONATGES = {
    "goku": {
        "nom": "Goku",
        "imatge": "characters/goku.jpg",
        "frase": "Kamehameha!"
    },
    "eren": {
        "nom": "Eren Jaeger",
        "imatge": "characters/eren.jpg",
        "frase": "TatakaE!"
    },
    "naruto": {
        "nom": "Naruto Uzumaki",
        "imatge": "characters/naruto.jpg",
        "frase": "Dattebayo!"
    },
    "luffy": {
        "nom": "Monkey D. Luffy",
        "imatge": "characters/luffy.jpg",
        "frase": "Voy a ser el Rey de los Piratas."
    },
    "mikasa": {
        "nom": "Mikasa Ackerman",
        "imatge": "characters/mikasa.jpg",
        "frase": "Eren..."
    },
}


def home(request):
    """
    Página principal: listado de personajes y opciones de URL.
    """
    context = {
        "mode": "home",
        "personatges": PERSONATGES,
    }
    return render(request, "characters/personatges.html", context)


def personatge(request, opcio):
    """
    /home -> vuelve a la home
    /nombre_personaje -> ficha
    /cosa_incorrecta -> error con meme
    """
    if opcio == "home":
        return home(request)

    if opcio in PERSONATGES:
        context = {
            "mode": "informacio",
            "personatge": PERSONATGES[opcio],
        }
    else:
        context = {
            "mode": "error",
            "missatge": f"El personatge «{opcio}» no existeix ",
        }

    return render(request, "characters/personatges.html", context)
