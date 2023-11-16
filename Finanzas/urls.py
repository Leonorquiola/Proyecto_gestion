"""
URL configuration for Finanzas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from Aplicaciones.Seguridad.views import TokenObtainPersonalizadoView

class Protegida(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response({"content":"Esta clase está protegida"}, status=status.HTTP_200_OK)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('Aplicaciones.Cuentas.urls')),
    #path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/', TokenObtainPersonalizadoView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('protegida/', Protegida.as_view(), name='protegida'),
    #path('authorization/', include('rest_framework.urls'))
]
