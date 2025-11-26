
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Paciente,ProfissionalSaude,Consulta
from .serializers import PacienteSerializer,ProfissionalSaudeSerializer,ConsultaSerializer

class PacienteViewSet(viewsets.ModelViewSet):
    queryset=Paciente.objects.all()
    serializer_class=PacienteSerializer
    permission_classes=[IsAuthenticated]

class ProfissionalSaudeViewSet(viewsets.ModelViewSet):
    queryset=ProfissionalSaude.objects.all()
    serializer_class=ProfissionalSaudeSerializer
    permission_classes=[IsAuthenticated]

class ConsultaViewSet(viewsets.ModelViewSet):
    queryset=Consulta.objects.all()
    serializer_class=ConsultaSerializer
    permission_classes=[IsAuthenticated]
