from django.db.migrations import serializer
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from tarefa.models import Tarefa


class TarefaSerializer(ModelSerializer):
    data = serializers.DateField(required=True)
    hora = serializers.TimeField(required=True)

    def create(self, validated_data):
        tarefa = Tarefa(**validated_data)
        tarefa.usuario = self.context['request'].user
        tarefa.save()
        return tarefa

    class Meta:
        model = Tarefa
        fields = ['id', 'titulo', 'descricao', 'data', 'hora', 'concluida', ]
        ordering = ['-data', '-hora', '-concluida']
