from django.shortcuts import render, redirect
from django.contrib.auth.mixins import UserPassesTestMixin, AccessMixin, LoginRequiredMixin
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Gato
from .forms import GatoForm


# Create your views here.

class GatoList (ListView):                    
    model = Gato
    template_name = 'Gato/gato_list.html'
    
class GatoList2 (ListView):                    
    model = Gato
    template_name = 'Gato/contenido.html'
    
class GatoList3 (ListView):                    
    model = Gato
    template_name = 'Gato/cuidados.html'

class GatoCreate (CreateView):
    model = Gato
    form_class = GatoForm
    template_name = 'Gato/gato_form.html'
    success_url = reverse_lazy('gatos_list')

class GatoUpdate(UpdateView):
    model = Gato
    form_class = GatoForm
    template_name = 'Gato/gato_form.html'
    success_url = reverse_lazy('gatos_list')

class GatoDelete(DeleteView):
    model = Gato
    template_name = 'Gato/gato_borrar.html'
    success_url = reverse_lazy('gatos_list')
