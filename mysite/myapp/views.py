from django.shortcuts import render
from .models import Person
# from django.http import HttpResponse

# Create your views here.
# Siempre las funciones reciben request

def index(request):
    # return HttpResponse("Hello, world. from Django")
    people = Person.objects.all()
    context = {
        "people": people
    }

    # context es una palabra reservada
    # Si usamos context al momento de pasar nuestro diccionario de datos
    # Unicamente hay que usar el keys
    return render (request, "index.html", context)