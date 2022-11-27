from django.urls import path, include
from rest_framework import routers

from perfil.api.viewsets import PerfilViewSet
from usuario.api.viewsets import UsuarioViewSet, CriarUsuarioViewSet

router = routers.DefaultRouter()
router.register('usuarios', UsuarioViewSet)
router.register('cadastro', CriarUsuarioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
