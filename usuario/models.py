from datetime import datetime
from twilio.rest import Client
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class UsuarioMaganer(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('O e-mail é obrigatório')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Usuário precisa ter is_superuser=True')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Usuário precisa ter is_staff=True')

        return self._create_user(email, password, **extra_fields)


class CustomUsuario(AbstractUser):
    foto = models.ImageField(upload_to='usuarios', blank=True, null=True)
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    nascimento = models.DateField(blank=True, null=True)
    email = models.EmailField('e-mail', unique=True)
    celular = models.CharField('celular', max_length=17, unique=True)
    cidade = models.CharField('cidade', max_length=50, blank=True, null=True)
    plano = models.DateField(default=datetime.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'nome', 'sobrenome', 'celular']

    def __str__(self):
        return self.email

    # def save(self, *args, **kwargs):
    #     if self.pk:
    #         mes = Client('AC67a4fc44d1430895dd3191f2f5a107d8', '9ff2dea4c66321b927c663103b3ec410').messages.create(
    #             body=f'{self.nome} acabou de criar uma nova conta!',
    #             from_='whatsapp:+12202348211',
    #             to='whatsapp:+14155238886'
    #         )
    #         print(mes.sid)
    #     return super().save(*args, **kwargs)

    objects = UsuarioMaganer()
