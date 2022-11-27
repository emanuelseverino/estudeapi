from datetime import datetime

from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.permissions import BasePermission


class PlanoPermission(BasePermission):

    def has_permission(self, request, view):
        plano = request.user.plano
        hoje = datetime.now().date()
        if plano > hoje:
            return True
        raise MessagemPermissao()


class MessagemPermissao(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = {'erro': 'Você precissa atualizar seu plano',
                      'mensagem': f'Entre em contato para liberar seu acesso.',
                      'contato': '(22) 99799-0159',
                      'whatsapp': 'https://wa.me/5522997990159', }
    default_code = 'not_authenticated'
