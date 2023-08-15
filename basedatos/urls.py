"""
URL configuration for basedatos project.

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

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from categoria.api.router import router_categoria
from usuario.api.router import router_usuario
from gestorcursos.api.router import router_curso, router_cursousuario, router_sesion, router_curso_temas, router_requisitos, router_contenido_vistas, router_recurso, router_contenido


schema_view = get_schema_view(
   openapi.Info(
      title="Capacitandome - API Doc",
      default_version='v1',
      description="Documentacion de la api de Capacitandome",
      terms_of_service="https://www.tincode.es/",
      contact=openapi.Contact(email="pieropr17@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)


api_urls = [
    path('categoria/', include(router_categoria.urls)),
    path('usuario/', include(router_usuario.urls)),
    path('curso/', include(router_curso.urls)),
    path('cursousuario/', include(router_cursousuario.urls)),
    path('sesion/', include(router_sesion.urls)),
    path('curso_temas/', include(router_curso_temas.urls)),
    path('requisitos/', include(router_requisitos.urls)),
    path('contenido/', include(router_contenido.urls)),
    path('recurso/', include(router_recurso.urls)),
    path('contenido_vistas/', include(router_contenido_vistas.urls))
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger',cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',cache_timeout=0), name='schema-redoc'),
    path('api/', include(api_urls))
]
