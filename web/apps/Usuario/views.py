from django.shortcuts import render
from .forms import RegistroForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

# Create your views here.
class RegistroUsuario(CreateView):
    model = User
    template_name = "Usuario/registrar.html"
    form_class = RegistroForm
    success_url = reverse_lazy('list_user')
 
 
class UserList(ListView):
    model = User
    template_name = 'Usuario/list_user.html'
