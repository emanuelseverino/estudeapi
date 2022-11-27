from django.urls import path, include
from rest_framework import routers

from perfil.api.viewsets import PerfilViewSet

router = routers.DefaultRouter()
router.register('', PerfilViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('', PerfilViewSet.as_view(), name=''),
]
