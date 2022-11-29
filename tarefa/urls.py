from django.urls import path, include
from rest_framework import routers

from tarefa.api.viewsets import TarefaViewSet

router = routers.DefaultRouter()
router.register('', TarefaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
