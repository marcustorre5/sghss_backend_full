
from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Paciente,ProfissionalSaude,Consulta

User=get_user_model()
admin.site.register(User)
admin.site.register(Paciente)
admin.site.register(ProfissionalSaude)
admin.site.register(Consulta)
