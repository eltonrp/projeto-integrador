from django.db import models
from django.contrib.auth.models import User
from users.models import PerfilAluno, PerfilVoluntario

# Create your models here.
areas = [
    ('Matemática', 'Matemática'),
    ('Língua Portuguesa', 'Língua Portuguesa'),
    ('Geografia', 'Geografia'),
    ('História', 'História'), 
    ('Física', 'Física'), 
    ('Química', 'Química'), 
    ('Biologia','Biologia'), 
    ('Artes','Artes'), 
    ('Educação Física', 'Educação Física'), 
    ('Sociologia', 'Sociologia'), 
    ('Filosofia', 'Filosofia'),  
    ('Inglês', 'Inglês'),
    ('Outras', 'Outras')
]

class Dificuldade(models.Model):
    nome = models.CharField(max_length=30, help_text='Digite um nome curto para sua dificuldade', verbose_name='Nome da dificuldade')
    area = models.CharField(max_length=20, choices=areas, help_text='Selecione uma área do conhecimento', verbose_name='Disciplina')
    assunto = models.CharField(max_length=200, help_text='Assunto(s) dentro da área do conhecimento. Ex: Equação do Segundo Grau, Equação do Primeiro Grau e Frações')
    descricao = models.TextField(max_length=250, help_text='Escreva livremente com detalhes quais suas dificuldades e como o voluntário pode te ajudar')
    data = models.DateTimeField(auto_now_add=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.area} - {self.nome}, em {self.data}'
    
class Oferta(models.Model):
    habilidades = [
        ('Iniciante', 'Iniciante'),
        ('Intermediário', 'Intermediário'),
        ('Avançado', 'Avançado'),
    ]
    nome = models.CharField(max_length=30, help_text='Digite um nome curto para sua oferta de reforço', verbose_name='Oferta de Reforço')
    habilidade = models.CharField(max_length=30, choices=habilidades, help_text='Selecione o nível de habilidade para a oferta que está registrando')
    area = models.CharField(max_length=20, choices=areas, help_text='Selecione uma área do conhecimento')
    descricao = models.TextField(max_length=250, help_text='Escreva livremente com detalhes suas habilidades e como pode ajudar um aluno.')
    data = models.DateTimeField(auto_now_add=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.area} - {self.nome}, em {self.data}'

class MensagensAluno(models.Model):
    sender = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    receiver = models.ForeignKey(PerfilAluno, on_delete=models.PROTECT, null=True)
    mensagem = models.TextField(max_length=200)

    def __str__(self) -> str:
        return f'{self.mensagem}'

class MensagensVoluntario(models.Model):
    sender = models.ForeignKey(User, on_delete=models.PROTECT)
    receiver = models.ForeignKey(PerfilVoluntario, on_delete=models.PROTECT)
    mensagem = models.TextField(max_length=200)

    def __str__(self) -> str:
        return f'{self.mensagem}'
