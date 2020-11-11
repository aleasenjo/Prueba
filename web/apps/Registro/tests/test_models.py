from django.test import TestCase
from django.template.defaultfilters import slugify
from apps.Registro.models import Mensaje

class MensajeTestCase(TestCase):
    def setUp(self):
        Mensaje.objects.create(email="AAA",rut="4",nombre="juan" ,telefono="10000",gato="asd")
        Mensaje.objects.create(email="BBB",rut="6",nombre="rosa" ,telefono="23232",gato="asdf")

    def test_ingresar_mensajes(self):
        """Los mensajes se registran correctamente en la BD"""
        mensaje_1 = Mensaje.objects.get(nombre="juan")
        mensaje_2 = Mensaje.objects.get(nombre="rosa")
        self.assertEqual(mensaje_1.rut, "4")
        self.assertEqual(mensaje_2.rut, "6")
