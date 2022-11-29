from django.contrib.auth import get_user_model
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from permissions.plano_permissions import PlanoPermission
from tarefa.api.serializers import TarefaSerializer
from tarefa.models import Tarefa

Usuario = get_user_model()


class TarefaViewSet(ModelViewSet):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, PlanoPermission]

    def get_queryset(self):
        return self.queryset.get(usuario=self.request.user)
