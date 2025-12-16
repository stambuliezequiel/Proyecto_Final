from .models import Articulo, Categoria
from apps.comentarios.models import Comentario
from .forms import ArticuloForm, NuevaCategoriaForm
from django.views.generic import ListView, DetailView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse_lazy, reverse
from django.contrib import messages


class ArticuloListView(ListView):
    model = Articulo
    template_name = 'articulos/articulos.html'
    context_object_name = 'articulos'

    def get_queryset(self):
        queryset = super().get_queryset()
        orden = self.request.GET.get('orden')
        if orden == 'reciente':
            queryset = queryset.order_by('-fecha_publicacion')
        elif orden == 'mas antiguo':
            queryset = queryset.order_by('fecha_publicacion')
        elif orden == 'alfabetico':
            queryset = queryset.order_by('titulo')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orden'] = self.request.GET.get('orden', 'reciente')
        return context


class ArticuloDetailView(DetailView):
    model = Articulo
    template_name = 'articulos/articulo_individual.html'
    context_object_name = 'articulos'
    pk_url_kwarg = 'id'
    queryset = Articulo.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comentarios'] = Comentario.objects.filter(articulo=self.object)
        return context



class ArticuloCreateView(LoginRequiredMixin, CreateView):
    model = Articulo
    template_name = 'articulos/articulos_form.html'
    fields = ['titulo', 'contenido', 'imagen', 'resumen', 'categoria']
    success_url = reverse_lazy('articulos')

    def get_success_url(self):
        messages.success(self.request, '¡Artículo creado con éxito!')
        return reverse_lazy('apps.articulos:articulos')


class ArticuloUpdateView(LoginRequiredMixin, UpdateView):
    model = Articulo
    form_class = ArticuloForm
    template_name = 'articulos/articulos_form.html'

    def get_success_url(self):
        messages.success(self.request, '¡Artículo modificado con éxito!')
        return reverse_lazy('apps.articulos:articulos')


class ArticuloDeleteView(DeleteView):
    model = Articulo
    template_name = 'articulos/articulos_eliminar.html'

    def get_success_url(self):
        messages.success(self.request, '¡Borrado con éxito!')
        return reverse_lazy('apps.articulos:articulos')


class ArticuloPorCategoriaView(ListView):
    model = Articulo
    template_name = 'articulos/articulos_por_categoria.html'
    context_object_name = 'articulos'

    def get_queryset(self):
        return Articulo.objects.filter(categoria_id=self.kwargs['pk'])


class CategoriaCreateView(LoginRequiredMixin, CreateView):
    model = Categoria
    form_class = NuevaCategoriaForm
    template_name = 'articulos/crear_categoria.html'

    def get_success_url(self):
        messages.success(self.request, '¡Categoría creada con éxito!')
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        else:
            return reverse_lazy('apps.articulos:articulos_form')


class CategoriaListView(ListView):
    model = Categoria
    template_name = 'articulos/categoria_lista.html'
    context_object_name = 'categorias'


class CategoriaDeleteView(LoginRequiredMixin, DeleteView):
    model = Categoria
    template_name = 'articulos/categoria_eliminar.html'
    success_url = reverse_lazy('apps.articulos:categoria_lista')