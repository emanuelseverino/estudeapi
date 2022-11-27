from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from usuario.api.viewsets import UsuarioViewSet, CriarUsuarioViewSet, ChangePasswordView

router = routers.DefaultRouter()


urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include(router.urls)),
                  path('perfil/', include('perfil.urls')),
                  path('', include('usuario.urls')),
                  path('usuario/', include('django.contrib.auth.urls')),
                  path('login/', obtain_auth_token),
                  path('change-password/', ChangePasswordView.as_view(), name='change-password'),
              ]

# handler404 = views.erro404
# handler500 = views.erro500
