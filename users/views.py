from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import Group
from .forms import UserForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import PerfilAluno, PerfilVoluntario

# Create your views here.
class StudentCreate(CreateView):
    template_name = 'users/form-base.html'
    form_class = UserForm
    success_url = reverse_lazy('entrar')

    def form_valid(self, form):
        grupo = get_object_or_404(Group, name='Interessado')
        url = super().form_valid(form)
        self.object.groups.add(grupo)
        PerfilAluno.objects.create(usuario=self.object)
        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Registro de novo Aluno'
        context['botao'] = 'Cadastrar'
        return context

class VolunteerCreate(CreateView):
    template_name = 'users/form-base.html'
    form_class = UserForm
    success_url = reverse_lazy('entrar')

    def form_valid(self, form):
        grupo = get_object_or_404(Group, name='Professor')
        url = super().form_valid(form)
        self.object.groups.add(grupo)
        PerfilVoluntario.objects.create(usuario=self.object)
        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Registro de novo Voluntário'
        context['botao'] = 'Cadastrar'
        return context

class PerfilAlunoUpdate(Group, UpdateView):
    template_name = 'users/form-base.html'
    model = PerfilAluno
    fields = ['nome_completo', 'cpf', 'data_nasc', 'contato', 'cidade','serie', 'descricao', ]
    success_url = reverse_lazy('listar-alunos')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(PerfilAluno, usuario=self.request.user)
        return self.object

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Editar Perfil de Aluno'
        context['botao'] = 'Editar'
        return context
        
class PerfilVoluntarioUpdate(UpdateView):
    template_name = 'users/form-base.html'
    model = PerfilVoluntario
    fields = ['nome_completo', 'cpf', 'data_nasc', 'contato', 'cidade', 'nivel', 'descricao']
    success_url = reverse_lazy('listar-voluntarios')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(PerfilVoluntario, usuario=self.request.user)
        return self.object

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Editar Perfil de Voluntário'
        context['botao'] = 'Editar'
        return context
