from django.shortcuts import render, redirect
from .models import Person
from django.views.generic import View, TemplateView, CreateView , FormView# Solo se usa para clases NO para funciones.
from .forms import PersonForm
# from django.http import HttpResponse

# Create your views here.


class CreatePerson(FormView):
    model = Person
    form_class = PersonForm
    template_name = 'form.html'

    def form_valid(self, form):
        Person.objects.create(**form.cleaned_data)
        return redirect('index')

    def form_invalid(self, form):
        print(form)
        return redirect('index')


# Se crea la clase CreatePerson para validar y probar el choiceField -> Gender (Masculino, Femenino, Otros)
# class CreatePerson(View):
#     def get(self, request):
#         context = {"form": PersonForm}
#         return render (request, "form.html", context)  # Creando la vista

#     def post(self, request):
#         form = PersonForm(request.POST)
#         # Vamos a poder acceder a la informacion
#         if form.is_valid():
#             # Como acceso a la info de los inputs
#             Person.objects.create(**form.cleaned_data)
#             return redirect('index')
#         else:
#             return redirect('index')



# class TemplateIndexView(TemplateView):
#     template_name = 'index.html'
#     extra_context = { "people": Person.objects.all() }

class TemplateIndexView(CreateView):
    template_name = "index.html"
    model = Person
    fields = ['name', 'address', 'email']
    extra_context = { "people": Person.objects.all() }



class Index(View):
    # Cuando la clase hereda de View tiene los metodos predefinidos (get/post)
    def get(self, request):
        people = Person.objects.all()
        context = { "people": people }
        return render (request, "index.html", context)

#     def post(self, request):
#         # Logica para crear una persona
#         Person.objects.create(name = request.POST["name"])
#         return redirect("index")




# # Siempre las funciones reciben request

# def index(request):
#     # return HttpResponse("Hello, world. from Django")
#     people = Person.objects.all()
#     context = {
#         "people": people
#     }

#     if request.method == "POST":
#         pass

#     # context es una palabra reservada
#     # Si usamos context al momento de pasar nuestro diccionario de datos
#     # Unicamente hay que usar el keys
#     return render (request, "index.html", context)