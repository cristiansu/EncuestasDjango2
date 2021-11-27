from django.db import models

# Create your models here.

class Pregunta(models.Model):
    pregunta_texto=models.CharField(max_length=150)
    fecha=models.DateTimeField(auto_now=True)
    votos_totales=models.IntegerField(default=0)

    def __str__(self):
        return self.pregunta_texto

class Opciones(models.Model):
    pregunta=models.ForeignKey(to=Pregunta, on_delete=models.CASCADE)
    opcion_texto=models.CharField(max_length=150)
    votos=models.IntegerField(default=0)

    def __str__(self):
        return self.opcion_texto
