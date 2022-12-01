from django.contrib.auth import get_user_model
from drf_extra_fields.fields import Base64ImageField
from rest_framework.serializers import ModelSerializer

Usuario = get_user_model()


class PerfilSerializer(ModelSerializer):
    foto = Base64ImageField(required=False)


    class Meta:
        model = Usuario
        fields = ['id', 'foto', 'nome', 'sobrenome', 'username', 'email', 'nascimento', 'celular', 'cidade', ]
