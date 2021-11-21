from django.contrib import admin
from .models import Dificuldade, Oferta, MensagensAluno, MensagensVoluntario

# Register your models here.

admin.site.register(Dificuldade)
admin.site.register(Oferta)
admin.site.register(MensagensAluno)
admin.site.register(MensagensVoluntario)
