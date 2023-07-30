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
from gestorcursos.api.router import router_curso, router_calificacioncurso, router_cursousuario, router_seccion, router_curso_temas, router_requisitos, router_clase, router_recurso, router_clases_vistas, router_examen, router_pregunta, router_alternativa, router_resolverexamen, router_detalleresolverexamen, router_respuesta


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
    path('calificacioncurso/', include(router_calificacioncurso.urls)),
    path('cursousuario/', include(router_cursousuario.urls)),
    path('seccion/', include(router_seccion.urls)),
    path('curso_temas/', include(router_curso_temas.urls)),
    path('requisitos/', include(router_requisitos.urls)),
    path('clase/', include(router_clase.urls)),
    path('recurso/', include(router_recurso.urls)),
    path('clases_vistas/', include(router_clases_vistas.urls)),
    path('examen/', include(router_examen.urls)),
    path('pregunta/', include(router_pregunta.urls)),
    path('alternativa/', include(router_alternativa.urls)),
    path('resolverexamen/', include(router_resolverexamen.urls)),
    path('detalleresolverexamen/', include(router_detalleresolverexamen.urls)),
    path('respuesta/', include(router_respuesta.urls))
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger',cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',cache_timeout=0), name='schema-redoc'),
    path('api/', include(api_urls))
]
