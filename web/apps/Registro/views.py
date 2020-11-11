from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Mensaje
from .forms import MensajeForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# Create your views here.
def listar_mensajes(request):
    mensajes = Mensaje.objects.all()
    return render(request, "Registro/listar_mensajes.html", {'mensajes': mensajes})


class MensajeCreate(CreateView):
    model = Mensaje
    form_class = MensajeForm
    template_name = 'Registro/mensaje_form.html'
    success_url = reverse_lazy('list_mensajes')
    
class MensajeList(ListView):
    model = Mensaje
    template_name = 'Registro/list_mensajes.html'
    # paginate_by = 4

class MensajeUpdate(UpdateView):
    model = Mensaje
    form_class = MensajeForm
    template_name = 'Registro/mensaje_form.html'
    success_url = reverse_lazy('list_mensajes')

        

class MensajeDelete(DeleteView):
    model = Mensaje
    template_name = 'Registro/mensaje_delete.html'
    success_url = reverse_lazy('list_mensajes')
