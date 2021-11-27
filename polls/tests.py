from django.test import TestCase

# Create your tests here.
from .models import Pregunta, Opciones

class EncuestaTestCase(TestCase):

    def setUp(self):
        pregunta=Pregunta.objects.create(pregunta_texto='Pregunta Testeo')
        Opciones.objects.create(pregunta=pregunta, opcion_texto='opción test')

    def test_modelo_pregunta(self):
        pregunta=Pregunta.objects.get(id=1)
        self.assertEqual(Pregunta.objects.get(id=1).pregunta_texto, 'Pregunta Testeo')
        self.assertTrue(len(pregunta.opciones_set.all())==1)
