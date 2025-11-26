
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PacienteViewSet,ProfissionalSaudeViewSet,ConsultaViewSet

router=DefaultRouter()
router.register('pacientes',PacienteViewSet)
router.register('profissionais',ProfissionalSaudeViewSet)
router.register('consultas',ConsultaViewSet)

urlpatterns=[
    path('',include(router.urls)),
]
