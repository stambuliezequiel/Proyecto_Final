from django.urls import path
from . import views

app_name = 'apps.comentarios'

urlpatterns = [
    path('comentarios/', views.ComentariosView, name='comentarios'),
    path('comentarios/eliminar/<int:pk>/', views.eliminar_comentario, name='eliminar_comentario'),
    path('comentarios/editar/<int:pk>/', views.editar_comentario, name='editar_comentario'),
    path('listado_comentario/', views.ListadoComentarioView.as_view(), name='listado_comentario'),
]