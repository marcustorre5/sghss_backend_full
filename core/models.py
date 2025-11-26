
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN='ADMIN','Administrador'
        PROF='PROF','Profissional'
        PAC='PAC','Paciente'
    role=models.CharField(max_length=5,choices=Role.choices,default=Role.PAC)

class Paciente(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='paciente')
    cpf=models.CharField(max_length=11,unique=True)
    data_nascimento=models.DateField(null=True,blank=True)
    telefone=models.CharField(max_length=20,blank=True)

class ProfissionalSaude(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profissional')
    especialidade=models.CharField(max_length=100)
    registro_conselho=models.CharField(max_length=50,unique=True)

class Consulta(models.Model):
    class Tipo(models.TextChoices):
        PRES='PRES','Presencial'
        TEL='TEL','Telemedicina'
    class Status(models.TextChoices):
        AGD='AGD','Agendada'
        CON='CON','Concluída'
        CAN='CAN','Cancelada'
    paciente=models.ForeignKey(Paciente,on_delete=models.CASCADE,related_name='consultas')
    profissional=models.ForeignKey(ProfissionalSaude,on_delete=models.CASCADE,related_name='consultas')
    data_hora=models.DateTimeField()
    tipo=models.CharField(max_length=4,choices=Tipo.choices,default=Tipo.PRES)
    status=models.CharField(max_length=3,choices=Status.choices,default=Status.AGD)
    descricao=models.TextField(blank=True)
    criado_em=models.DateTimeField(auto_now_add=True)
    atualizado_em=models.DateTimeField(auto_now=True)
