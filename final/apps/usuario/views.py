from .forms import RegistroUsuarioForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy


class RegistrarUsuario(CreateView):
    template_name = 'registration/registrar.html'
    form_class = RegistroUsuarioForm

    def form_valid(self, form):
        messages.success(self.request, 'Registro exitoso. Por favor inicia sesión.')
        form.save()
        return redirect('apps.usuario:registrar')


class LoginUsuario(LoginView):
    template_name = 'registration/login.html'
    success_url = reverse_lazy('index')

    def get_success_url(self):
        messages.success(self.request, 'Login exitoso')
        return super().get_success_url()


class LogoutUsuario(LogoutView):
    template_name = 'registration/logout.html'
    success_url = reverse_lazy('index')

    def get_success_url(self):
        messages.success(self.request, 'Logout Exitoso!')
        return reverse_lazy('index')