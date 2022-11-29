from django.contrib.auth import get_user_model
from django.db import models

Usuario = get_user_model()


class Tarefa(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(max_length=1000)
    data = models.DateField(blank=True, null=True)
    hora = models.TimeField(blank=True, null=True)
    concluida = models.BooleanField(default=False)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Tarefa'
        verbose_name_plural = 'Tarefas'
