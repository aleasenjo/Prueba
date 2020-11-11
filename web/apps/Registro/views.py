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

def mantenedor(request):
    lista= Mensaje.objects.all()
    rut = request.GET.get('rut-mensajes')
    nombre_gato = request.GET.get('nombre-gato')

    if 'btn-buscarRutMensajes' in request.GET:
       if rut: 
           lista= Mensaje.objects.filter(rut__icontains=rut)
    elif 'btn-nombre-gato' in request.GET:
        if nombre_gato:
            lista= Mensaje.objects.filter(gato__icontains=nombre_gato)
      
    data = {
        'object_list': lista
    }
    return render(request, 'Registro/list_mensajes.html', data)
