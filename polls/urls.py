from django.urls import include, path
from .views import (
    index, 
    detail, 
    votar, 
    resultados, 
    PreguntaListView, 
    PreguntaCreate, 
    Pregunta_Update, 
    Pregunta_Delete,
    OpcionListView,
    OpcionCreate,
    Opcion_Update,
    Opcion_Delete
)
from django.contrib.auth.decorators import login_required

app_name="polls"

urlpatterns = [
    path('', index, name='index'),
    path('<int:pregunta_id>/', detail, name='detail'),
    path('<int:pregunta_id>/votar', votar, name='votar'),
    path('<int:pregunta_id>/resultados', resultados, name='resultados'),
    #CRUD Preguntas
    path('lista_preguntas/', PreguntaListView.as_view(), name='lista_preguntas'),
    path('crear_pregunta/', PreguntaCreate.as_view(), name='crear_pregunta'),
    path('actualizar_pregunta/<int:pk>/', Pregunta_Update.as_view(), name='actualizar_pregunta'),
    path('borrar_pregunta/<int:pk>/', Pregunta_Delete.as_view(), name='borrar_pregunta'),
    # CRUD Opciones
    path('lista_opciones/', OpcionListView.as_view(), name='lista_opciones'),
    path('crear_opciones/', OpcionCreate.as_view(), name='crear_opciones'),
    path('actualizar_opcion/<int:pk>/', Opcion_Update.as_view(), name='actualizar_opcion'),
    path('borrar_opcion/<int:pk>/', Opcion_Delete.as_view(), name='borrar_opcion'),
   
]