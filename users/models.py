from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class PerfilAluno(models.Model):
    series = [
        ('1', '1º Ano'),
        ('2', '2º Ano'),
        ('3', '3º Ano'),
    ]
    nome_completo = models.CharField(max_length=50, null=True)
    cpf = models.CharField(max_length=14, verbose_name='CPF', null=True)
    data_nasc = models.DateField(verbose_name='Data de nascimento', null=True)
    contato = models.CharField(max_length=16,help_text='Digite apenas números com o DDD', verbose_name="Tel contato", null=True)
    cidade = models.CharField(max_length=50, help_text='Digite sua cidade e Estado, EX: Campinas-SP', null=True)
    serie = models.CharField(max_length=1, choices=series, verbose_name='Série', null=True)
    descricao = models.TextField(max_length=500, verbose_name="Descrição", help_text='Conte um pouco sobre você, em quais disciplinas estão suas dificuldades e como gostaria de ser ajudado.', null=True, blank=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.nome_completo} | {self.usuario} | {self.usuario.email}'
    
class PerfilVoluntario(models.Model):
    niveis = [
        ('Ensino Médio', 'Ensino Médio'),
        ('Ensino Técnico', 'Ensino Técnico'),
        ('Ensino Superior - cursando', 'Ensino Superior - cursando'),
        ('Ensino Superior - completo', 'Ensino Superior - completo'),
        ('Pós-graduação - cursando', 'Pós-graduação - cursando'),
        ('Pós-graduação - completo', 'Pós-graduação - completo'),
    ]
    nome_completo = models.CharField(max_length=150, null=True)
    cpf = models.CharField(max_length=14, verbose_name='CPF', null=True)
    data_nasc = models.DateField(verbose_name='Data de nascimento', null=True)
    contato = models.CharField(max_length=11,help_text='Digite apenas números com o DDD', verbose_name="Tel contato", null=True)
    cidade = models.CharField(max_length=50, help_text='Digite sua cidade e Estado, EX: Campinas-SP', null=True)
    nivel = models.CharField(max_length=30, choices=niveis, verbose_name='Nível', null=True)
    descricao = models.TextField(max_length=500, verbose_name="Descrição", help_text='Descreva um pouco da sua trajetória, as disciplinas que possui maior habilidade e como gostaria de ajudar nessa causa.', null=True, blank=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.nome_completo} | {self.usuario} | {self.usuario.email}'