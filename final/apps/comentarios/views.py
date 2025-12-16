from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import View, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Comentario
from .forms import ComentarioForm
from apps.articulos.models import Articulo


def ComentariosView(request):
    if request.method == 'POST':
        contenido = request.POST.get('contenido')
        articulo_id = request.POST.get('articulo_id')
        
        if request.user.is_authenticated and contenido and articulo_id:
            articulo = get_object_or_404(Articulo, pk=articulo_id)
            Comentario.objects.create(usuario=request.user, texto=contenido, articulo=articulo)
            messages.success(request, 'Comentario agregado exitosamente.')
            return redirect('apps.articulos:articulo_individual', id=articulo_id)
    
    comentarios = Comentario.objects.all()
    return redirect('/articulos/')


@login_required  
def eliminar_comentario(request, pk): 
    comentario = get_object_or_404(Comentario, pk=pk)
    articulo_id = comentario.articulo.pk
    
    if comentario.usuario == request.user or request.user.is_staff:
        if request.method == 'POST':
            comentario.delete()
            messages.success(request, 'Comentario eliminado exitosamente.')
            return redirect('apps.articulos:articulo_individual', id=articulo_id)
    else:
        messages.error(request, 'No tienes permiso para eliminar este comentario.')
        return redirect('apps.articulos:articulo_individual', id=articulo_id)
    
    return render(request, 'comentarios/eliminar_comentarios.html', {'comentario': comentario})


@login_required
def editar_comentario(request, pk):
    comentario = get_object_or_404(Comentario, pk=pk)
    articulo_id = comentario.articulo.pk
    
    if comentario.usuario != request.user:
        messages.error(request, 'No tienes permiso para editar este comentario.')
        return redirect('apps.articulos:articulo_individual', id=articulo_id)
    
    if request.method == 'POST':
        contenido = request.POST.get('contenido')
        if contenido:
            comentario.texto = contenido
            comentario.save()
            messages.success(request, 'Comentario actualizado exitosamente.')
            return redirect('apps.articulos:articulo_individual', id=articulo_id)
    
    return render(request, 'comentarios/comentarios_editar.html', {'comentario': comentario})


class ListadoComentarioView(View):
    def get(self, request):
        comentarios = Comentario.objects.all()
        usuario = request.user.id
        context = {
            'comentarios': comentarios,
            'usuario': usuario,
        }
        return render(request, 'comentario/listadoComentario.html', context)