import django
from django.views.generic.edit import  CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Atividades, Campo, Conquistas, Ideias, MeusProjetos, Relatorios
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.shortcuts import get_object_or_404
# Create your views here.

class CampoCreate(LoginRequiredMixin, CreateView):
    model = Campo
    fields = ['nome', 'descricao']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('listar-campo')
    login_url = reverse_lazy("login")

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de Campus"
        return context

class MeusProjetosCreate(LoginRequiredMixin, CreateView):
    model = MeusProjetos
    fields = ['assunto', 'descricao', 'data', 'campo']
    template_name = 'cadastros/formulario-upload.html'
    success_url = reverse_lazy('listar-meusprojetos')
    login_url = reverse_lazy("login")   
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de Campus"
        return context

class RelatoriosCreate(LoginRequiredMixin, CreateView):
    model = Relatorios
    fields = ['assunto', 'descricao', 'data', 'campo']
    template_name = 'cadastros/formulario-upload.html'
    success_url = reverse_lazy('listar-relatorios')
    login_url = reverse_lazy("login")
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de Campus"
        return context

class IdeiasCreate(LoginRequiredMixin, CreateView):
    model = Ideias
    fields = ['assunto', 'descricao', 'data', 'campo']
    template_name = 'cadastros/formulario-upload.html'
    success_url = reverse_lazy('listar-ideias')
    login_url = reverse_lazy("login")
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de Campus"
        return context

class AtividadesCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    model = Atividades
    fields = ['assunto', 'descricao', 'data', 'campo']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('listar-atividades')
    login_url = reverse_lazy("login")
    group_required = u'Administradores'
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url 

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de Campus"
        return context

class ConquistasCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    model = Conquistas
    fields = ['assunto', 'descricao', 'data', 'campo']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('listar-conquistas')
    login_url = reverse_lazy("login")
    group_required = u'Administradores'
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url
           
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de Campus"
        return context

    # UPDATE


class CampoUpdate(LoginRequiredMixin, UpdateView):
    model = Campo
    fields = ['nome', 'descricao']
    template_name = 'cadastros/formulario-upload.html'
    success_url = reverse_lazy('listar-campo')
    login_url = reverse_lazy("login")

    def get_object(self, queryset = None):
        self.object = get_object_or_404(Campo, pk = self.kwargs['pk'], campo = self.request.user)
        return self.object
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Editar cadastro de campus"
        context['botao'] = "Salvar"
        return context

class MeusProjetosUpdate(LoginRequiredMixin, UpdateView):
    model = MeusProjetos
    fields = ['assunto', 'descricao', 'data', 'campo']
    template_name = 'cadastros/formulario-upload.html'
    success_url = reverse_lazy('listar-meusprojetos')
    def get_object(self, queryset = None):
        self.object = get_object_or_404(MeusProjetos, pk = self.kwargs['pk'], campo = self.request.user)
        return self.object


class RelatoriosUpdate(LoginRequiredMixin, UpdateView):
    model = Relatorios
    fields = ['assunto', 'descricao', 'data', 'campo']
    template_name = 'cadastros/formulario-upload.html'
    success_url = reverse_lazy('listar-relatorios')
    login_url = reverse_lazy("login")
    def get_object(self, queryset = None):
        self.object = get_object_or_404(Relatorios, pk = self.kwargs['pk'], campo = self.request.user)
        return self.object


class IdeiasUpdate(LoginRequiredMixin, UpdateView):
    model = Ideias
    fields = ['assunto', 'descricao', 'data', 'campo']
    template_name = 'cadastros/formulario-upload.html'
    success_url = reverse_lazy('listar-ideias')
    login_url = reverse_lazy("login")
    def get_object(self, queryset = None):
        self.object = get_object_or_404(Ideias, pk = self.kwargs['pk'], campo = self.request.user)
        return self.object


class AtividadesUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Atividades
    fields = ['assunto', 'descricao', 'data', 'campo']
    template_name = 'cadastros/formulario-upload.html'
    success_url = reverse_lazy('listar-atividades')
    login_url = reverse_lazy("login")
    group_required = u'Administradores'
    def get_object(self, queryset = None):
        self.object = get_object_or_404(Atividades, pk = self.kwargs['pk'], campo = self.request.user)
        return self.object


class ConquistasUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Conquistas
    fields = ['assunto', 'descricao', 'data', 'campo']
    template_name = 'cadastros/formulario-upload.html'
    success_url = reverse_lazy('listar-conquistas')
    login_url = reverse_lazy("login")
    group_required = u'Administradores'
    def get_object(self, queryset = None):
        self.object = get_object_or_404(Conquistas, pk = self.kwargs['pk'], campo = self.request.user)
        return self.object

# DELETE


class CampoDelete(LoginRequiredMixin, DeleteView):
    model = Campo
    template_name = 'cadastros/formulario-excluir.html'
    success_url = reverse_lazy('listar-campo')
    login_url = reverse_lazy("login")

    def get_object(self, queryset=None):
        self.object = get_object_or_404(
            Campo, pk=self.kwargs['pk'], campo=self.request.user)
        return self.object


class MeusProjetosDelete(LoginRequiredMixin, DeleteView):
    model = MeusProjetos
    template_name = 'cadastros/formulario-excluir.html'
    success_url = reverse_lazy('listar-meusprojetos')
    login_url = reverse_lazy("login")
    def get_object(self, queryset = None):
        self.object = get_object_or_404(MeusProjetos, pk = self.kwargs['pk'], campo = self.request.user)
        return self.object

class RelatoriosDelete(LoginRequiredMixin, DeleteView):
    model = Relatorios
    template_name = 'cadastros/formulario-excluir.html'
    success_url = reverse_lazy('listar-relatorios')
    login_url = reverse_lazy("login")
    def get_object(self, queryset = None):
        self.object = get_object_or_404(Relatorios, pk = self.kwargs['pk'], campo = self.request.user)
        return self.object

class IdeiasDelete(LoginRequiredMixin, DeleteView):
    model = Ideias
    template_name = 'cadastros/formulario-excluir.html'
    success_url = reverse_lazy('listar-ideias')
    login_url = reverse_lazy("login")
    def get_object(self, queryset = None):
        self.object = get_object_or_404(Ideias, pk = self.kwargs['pk'], campo = self.request.user)
        return self.object

class AtividadesDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Atividades
    template_name = 'cadastros/formulario-excluir.html'
    success_url = reverse_lazy('listar-atividades')
    login_url = reverse_lazy("login")
    group_required = u'Administradores'
    def get_object(self, queryset = None):
        self.object = get_object_or_404(Atividades, pk = self.kwargs['pk'], campo = self.request.user)
        return self.object    

class ConquistasDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Conquistas
    template_name = 'cadastros/formulario-excluir.html'
    success_url = reverse_lazy('listar-conquistas')
    login_url = reverse_lazy("login")
    group_required = u'Administradores'
    def get_object(self, queryset = None):
        self.object = get_object_or_404(
            Conquistas, pk=self.kwargs['pk'], campo=self.request.user)
        return self.object

# LISTAR 


class CampoList(LoginRequiredMixin, ListView):
    model = Campo
    lista = 'cadastros/campo.html'
    login_url = reverse_lazy("login")

    def get_queryset(self):
        self.object_list = Campo.objects.filter(nome = self.request.user)
        return super().get_queryset()


class MeusProjetosList(LoginRequiredMixin, ListView):
    model = MeusProjetos
    template_name = 'cadastros/meusprojetos.html'
    login_url = reverse_lazy("login")
    paginate_by = 10

    def get_queryset(self):
        txt_nome = self.request.GET.get('assunto')
        if txt_nome:
            pesquisa = MeusProjetos.objects.filter(assunto__icontains=txt_nome)
        else:
            pesquisa = MeusProjetos.objects.all()
        return pesquisa

class RelatoriosList(LoginRequiredMixin, ListView):
    model = Relatorios
    template_name = 'cadastros/relatorios.html'
    login_url = reverse_lazy("login")
    paginate_by = 10
    def get_queryset(self):
        txt_nome = self.request.GET.get('assunto')
        if txt_nome:
            pesquisa = Relatorios.objects.filter(assunto__icontains=txt_nome)
        else:
            pesquisa = Relatorios.objects.all()
        return pesquisa

class IdeiasList(LoginRequiredMixin, ListView):
    model = Ideias
    template_name = 'cadastros/ideias.html'
    login_url = reverse_lazy("login")
    paginate_by = 10
    def get_queryset(self):
        txt_nome = self.request.GET.get('assunto')
        if txt_nome:
            pesquisa = Ideias.objects.filter(assunto__icontains=txt_nome)
        else:
            pesquisa = Ideias.objects.all()
        return pesquisa

class AtividadesList(LoginRequiredMixin, ListView):
    model = Atividades
    template_name = 'cadastros/atividades.html'
    login_url = reverse_lazy("login")
    paginate_by = 10
    def get_queryset(self):
        txt_nome = self.request.GET.get('assunto')
        if txt_nome:
            pesquisa = Atividades.objects.filter(assunto__icontains=txt_nome)
        else:
            pesquisa = Atividades.objects.all()
        return pesquisa

class ConquistasList(LoginRequiredMixin, ListView):
    model = Conquistas
    template_name = 'cadastros/conquistas.html'
    login_url = reverse_lazy("LoginRequiredMixin, login")
    paginate_by = 10
    def get_queryset(self):
        txt_nome = self.request.GET.get('assunto')
        if txt_nome:
            pesquisa = Conquistas.objects.filter(assunto__icontains=txt_nome)
        else:
            pesquisa = Conquistas.objects.all()
        return pesquisa