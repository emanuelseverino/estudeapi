from django.contrib.auth import get_user_model
from rest_framework.authentication import TokenAuthentication
from rest_framework.mixins import UpdateModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from perfil.api.serializers import PerfilSerializer
from permissions.plano_permissions import PlanoPermission

Usuario = get_user_model()


class PerfilViewSet(RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = Usuario.objects.all()
    serializer_class = PerfilSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, PlanoPermission]

    def get_object(self):
        return self.queryset.get(email=self.request.user.email)
