from django.views.generic.edit import CreateView, UpdateView, DeleteView
from users.models import PerfilAluno
from .models import Dificuldade, Oferta, MensagensAluno, MensagensVoluntario
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.shortcuts import get_object_or_404

# Create your views here.
class DificuldadeCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('entrar')
    group_required = u'Interessado'
    model = Dificuldade
    fields = ['nome', 'area', 'assunto', 'descricao']
    template_name = 'pages/register.html'
    success_url = reverse_lazy('listar-alunos')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Registrar Dificuldade'
        context['botao'] = 'Registrar'
        context['descricao'] = 'Você pode cadastrar quantas Dificuldades achar necessárias. Separe por Disciplinas.'
        return context

class OfertaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('entrar')
    group_required = u'Professor'
    model = Oferta
    fields = ['nome', 'area', 'habilidade', 'descricao']
    template_name = 'pages/register.html'
    success_url = reverse_lazy('listar-voluntarios')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Registrar Oferta de Reforço'
        context['botao'] = 'Registrar'
        context['descricao'] = 'Você pode cadastrar quantas Ofertas de Reforço achar necessárias. Separe por Disciplinas.'
        return context
        
############## UPDATE ##################

class DificuldadeUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('entrar')
    group_required = u'Interessado'
    model = Dificuldade
    fields = ['nome', 'area', 'assunto', 'descricao']
    template_name = 'pages/register.html'
    success_url = reverse_lazy('listar-alunos')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Dificuldade, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Editar Dificuldade'
        context['botao'] = 'Editar'
        context['descricao'] = ''
        return context

class OfertaUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('entrar')
    group_required = u'Professor'
    model = Oferta
    fields = ['nome', 'area', 'habilidade', 'descricao']
    template_name = 'pages/register.html'
    success_url = reverse_lazy('listar-voluntarios')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Oferta, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

    def get_context_data(self, *args, **kwargs):
            context = super().get_context_data(*args, **kwargs)
            context['titulo'] = 'Editar registro'
            context['botao'] = 'Editar'
            context['descricao'] = ''
            return context

############## DELETE ##################

class DificuldadeDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('entrar')
    group_required = u'Interessado'
    model = Dificuldade
    template_name = 'pages/form-excluir.html'
    success_url = reverse_lazy('listar-alunos')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Dificuldade, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

class OfertaDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('entrar')
    group_required = u'Professor'
    model = Oferta
    template_name = 'pages/form-excluir.html'
    success_url = reverse_lazy('listar-voluntarios')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Oferta, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

############## LISTA ##################

class DificuldadeList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('entrar')
    group_required = u'Interessado'
    model = Dificuldade
    template_name = 'pages/alunos.html'

    def get_queryset(self):
        self.object_list = Dificuldade.objects.filter(usuario=self.request.user)
        return self.object_list

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['perfil'] = PerfilAluno.objects.filter(nome_completo=self.request.user)
        context['botao'] = 'Cadastrar'

        return context

class OfertaList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('entrar')
    group_required = u'Professor'
    model = Oferta
    template_name = 'pages/voluntarios.html'

    def get_queryset(self):
        self.object_list = Oferta.objects.filter(usuario=self.request.user)
        return self.object_list

class TodaDificuldadeList(ListView):
    model = Dificuldade
    template_name = 'pages/todos-alunos.html'
          
    def get_queryset(self):
        self.object_list = Dificuldade.objects.all()
        return self.object_list

class TodaOfertaList(ListView):
    model = Oferta
    template_name = 'pages/todos-voluntarios.html'
          
    def get_queryset(self):
        self.object_list = Oferta.objects.all()
        return self.object_list

############# Mensagens #########################

class MensagensAlunoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('entrar')
    group_required = u'Professor'
    model = MensagensAluno
    fields = ['mensagem']
    template_name = 'pages/register.html'
    success_url = reverse_lazy('todos-alunos')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Enviar mensagem'
        context['botao'] = 'Enviar'
        context['descricao'] = 'Funcionalidade em construção. Apenas Ilustrativo.'
        return context

class MensagensVoluntarioCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('entrar')
    group_required = u'Interessado'
    model = MensagensVoluntario
    fields = ['mensagem']
    template_name = 'pages/register.html'
    success_url = reverse_lazy('todos-voluntarios')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Enviar mensagem'
        context['botao'] = 'Enviar'
        context['descricao'] = 'Funcionalidade em construção. Apenas Ilustrativo.'
        return context
