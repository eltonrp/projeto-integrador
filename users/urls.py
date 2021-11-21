from django.urls import path
from django.contrib.auth import views as auth_views
from .views import StudentCreate, VolunteerCreate, PerfilAlunoUpdate, PerfilVoluntarioUpdate

urlpatterns = [
    path('entrar/', auth_views.LoginView.as_view(
        template_name='users/form.html'
    ), name='entrar'),
    path('sair/', auth_views.LogoutView.as_view(), name='sair'),
    path('registrar/aluno', StudentCreate.as_view(), name='registrar-aluno'),
    path('registrar/voluntario', VolunteerCreate.as_view(), name='registrar-voluntario'),
    path('atualizar/aluno/', PerfilAlunoUpdate.as_view(), name='atualizar-aluno'),
    path('atualizar/voluntario', PerfilVoluntarioUpdate.as_view(), name='atualizar-voluntario'),
]
