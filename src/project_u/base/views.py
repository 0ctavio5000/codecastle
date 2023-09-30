from django.shortcuts import render
from django.views.generic.list import ListView
from . models import tarea
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

class lista_p(ListView):
    model= tarea
    context_object_name='tareas'

class detalle_t(DetailView):
    model= tarea
    context_object_name='tarea'
    template_name='base/tarea.html'
    

class login(LoginView):
    template_name='base/login.html'
    field='__all__'
    redirect_authenticated_user=True

    def get_success_url(self):
        return reverse_lazy ('tareas')
