from unicodedata import name
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User, Group
from django.urls import reverse_lazy
from .forms import UsuarioForm
from django.shortcuts import get_object_or_404

# Create your views here.
class UsuarioCreate(CreateView):
    template_name = "cadastros/formulario.html"
    model = User
    field = ["username", "email", "password"]
    form_class = UsuarioForm
    success_url  = reverse_lazy('login')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Registro de Campus"
        context['botao'] = "Cadastrar" 
        return context

    def form_valid(self, form):
        grup = get_object_or_404(Group, name='Administradores')
        url = super().form_valid(form)
        self.object.groups.add(grup)
        self.object.save()
        return url