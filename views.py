from django.shortcuts import render
from django.http import HttpResponse
from . import data  # Importamos nuestros datos

def Hola(request):
    return HttpResponse("Hola mundo...!")

def datos_personales(request):
    context = {
        'datos_personales': data.DATOS_PERSONALES,
        'info_items': data.INFO_ITEMS
    }
    return render(request, 'datos_personales.html', context)

def preferencias(request):
    context = {
        'generos_musicales': data.GENEROS_MUSICALES,
        'artistas_favoritos': data.ARTISTAS_FAVORITOS,
        'canciones_favoritas': data.CANCIONES_FAVORITAS,
        'peliculas_series': data.PELICULAS_SERIES
    }
    return render(request, 'preferencias.html', context)

def gustos(request):
    context = {
        'mis_gustos': data.MIS_GUSTOS,
        'titulos_gustos': data.TITULOS_GUSTOS
    }
    return render(request, 'gustos.html', context)

def habilidades(request):
    context = {
        'habilidades': data.HABILIDADES,
        'titulos_habilidades': data.TITULOS_HABILIDADES
    }
    return render(request, 'habilidades.html', context)

def familia(request):
    context = {
        'entorno_social': data.ENTORNO_SOCIAL,
        'titulos_familia': data.TITULOS_FAMILIA
    }
    return render(request, 'familia.html', context)