from django.test import TestCase
from apps.Registro.models import Mensaje
from apps.Registro.forms import MensajeForm

class MensajeFormCase(TestCase):
        
    def test_valid_form(self):
        # fields = ['nombre', 'rut', 'email', 'gato', 'telefono']
        mensaje = Mensaje.objects.create(nombre="juan",rut="4",email="AAA" ,gato="asd",telefono="10000")
        data = {'nombre': mensaje.nombre, 'rut': mensaje.rut,'email': mensaje.email,'gato': mensaje.gato,'telefono': mensaje.telefono, }
        form = MensajeForm(data=data)
        self.assertTrue(form.is_valid())
        
    def test_invalid_form(self):
        mensaje = Mensaje.objects.create(nombre=0,rut="4",email="AAA" ,gato="asd",telefono="10000")
        data = {'nombre': mensaje.nombre, 'rut': mensaje.rut,'email': mensaje.email,'gato': mensaje.gato,'telefono': mensaje.telefono, }
        form = MensajeForm(data=data)
        self.assertTrue(form.is_valid())