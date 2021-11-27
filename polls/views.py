from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Pregunta, Opciones
from django.template import context, loader
from django.views.generic.list import ListView
from django.views.generic.edit import (
    CreateView,
    DeleteView,
    UpdateView,
)
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    preguntas=Pregunta.objects.order_by('fecha')[:10]
    template=loader.get_template('index.html')
    context={'preguntas':preguntas}

    return HttpResponse(template.render(context=context))

def detail(request, pregunta_id):
    try:
        pregunta=Pregunta.objects.get(id=pregunta_id)
    except Pregunta.DoesNotExist:
        raise Http404
    context={'pregunta':pregunta}

    return render(request, 'detail.html', context=context)

def votar(request, pregunta_id): #otra forma de hacer idem a funcion detail pero sin Http404, permite ahorrar código
    pregunta=get_object_or_404(Pregunta, id=pregunta_id)

    try:
        eleccion=Opciones.objects.get(id=request.POST['opcion']) #request.POST es un diccionario, por eso se entrega la key, en este caso es el name del input del template detail
    except (KeyError, Opciones.DoesNotExist):
        return render(request, 'detail.html', context={
            'pregunta':pregunta,
            'error_form':'Debes seleccionar una opción'
        })
    else:
        eleccion.votos +=1
        pregunta.votos_totales +=1
        eleccion.save()
        pregunta.save()

    return HttpResponseRedirect(reverse('polls:resultados', args=(pregunta_id,)))

def resultados(request, pregunta_id):
    pregunta=get_object_or_404(Pregunta, id=pregunta_id)
    context={'pregunta':pregunta}

    return render(request, 'resultados.html', context=context)

#------------CRUD Preguntas------------------
#@login_required
class PreguntaListView(ListView):
    model = Pregunta
    template_name = 'lista_preguntas.html'
    context_object_name = 'lista_preguntas'

class PreguntaCreate(CreateView):
    model = Pregunta
    template_name = 'crear-pregunta.html'
    fields = ['pregunta_texto']
    success_url = reverse_lazy('polls:lista_preguntas')

class Pregunta_Update(UpdateView):
    model = Pregunta
    fields = ['pregunta_texto']
    template_name_suffix = '_update_form'
    template_name = 'actualizar_pregunta.html'
    success_url = reverse_lazy('polls:lista_preguntas')

class Pregunta_Delete(DeleteView):
    model = Pregunta
    template_name = 'borrar_pregunta.html'
    success_url = reverse_lazy('polls:lista_preguntas')

#------------CRUD Opciones------------------

class OpcionListView(ListView):
    model = Opciones
    template_name = 'lista_opciones.html'
    context_object_name = 'lista_opciones'

class OpcionCreate(CreateView):
    model = Opciones
    template_name = 'crear-opciones.html'
    fields = ['pregunta', 'opcion_texto']
    success_url = reverse_lazy('polls:lista_opciones')

class Opcion_Update(UpdateView):
    model = Opciones
    fields = ['opcion_texto']
    template_name_suffix = '_update_form'
    template_name = 'actualizar_opcion.html'
    success_url = reverse_lazy('polls:lista_opciones')

class Opcion_Delete(DeleteView):
    model = Opciones
    template_name = 'borrar_opcion.html'
    success_url = reverse_lazy('polls:lista_opciones')
