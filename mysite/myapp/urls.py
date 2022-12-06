from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name="index"), -> Llama a la FUNCION
    # path('', views.Index.as_view(), name="index"), # -> llama a la Clase, la funcion as_view() traducira lo que tenga la clase ponerlo como una vista
    path('', views.Index.as_view(), name="index"),
    path('crear/', views.CreatePerson.as_view(), name="crear")
]