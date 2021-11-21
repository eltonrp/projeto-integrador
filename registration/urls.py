from django.urls import path
from .views import DificuldadeCreate, DificuldadeUpdate, DificuldadeDelete
from .views import DificuldadeList, TodaDificuldadeList
from .views import OfertaCreate, OfertaUpdate, OfertaDelete
from .views import OfertaList, TodaOfertaList
from .views import MensagensAlunoCreate, MensagensVoluntarioCreate

urlpatterns = [
    path('registration/student', DificuldadeCreate.as_view(), name='cadastrar-aluno'),
    path('registration/volunteer', OfertaCreate.as_view(), name='cadastrar-voluntario'),

    path('editar/aluno/<int:pk>/', DificuldadeUpdate.as_view(), name='editar-aluno'),
    path('editar/voluntario/<int:pk>/', OfertaUpdate.as_view(), name='editar-voluntario'),
    
    path('excluir/aluno/<int:pk>/', DificuldadeDelete.as_view(), name='excluir-aluno'),
    path('excluir/voluntario/<int:pk>/', OfertaDelete.as_view(), name='excluir-voluntario'),

    path('listar/alunos', DificuldadeList.as_view(), name='listar-alunos'),
    path('listar/voluntarios', OfertaList.as_view(), name='listar-voluntarios'),
    path('todos/alunos', TodaDificuldadeList.as_view(), name='todos-alunos'),
    path('todos/voluntarios', TodaOfertaList.as_view(), name='todos-voluntarios'),

    path('mensagens/aluno/<int:pk>/', MensagensAlunoCreate.as_view(), name='mensagens-aluno'),
    path('mensagens/voluntario/<int:pk>/', MensagensVoluntarioCreate.as_view(), name='mensagens-voluntario'),
]
