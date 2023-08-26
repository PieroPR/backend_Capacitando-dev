from rest_framework.routers import DefaultRouter

from gestorcursos.api.views import CursoApiViewSet, CursoUsuarioApiViewSet, SesionApiViewSet, ContenidoApiViewSet, RecursoApiViewSet, contenido_vistasApiViewSet

router_curso = DefaultRouter()
router_curso.register(prefix='', basename='curso', viewset=CursoApiViewSet)  # OK

router_cursousuario = DefaultRouter()
router_cursousuario.register(prefix='', basename='cursousuario', viewset=CursoUsuarioApiViewSet) # OK

router_sesion = DefaultRouter()
router_sesion.register(prefix='', basename='sesion', viewset=SesionApiViewSet) # OK

router_contenido = DefaultRouter()
router_contenido.register(prefix='', basename='contenido', viewset=ContenidoApiViewSet) # OK

router_recurso = DefaultRouter()
router_recurso.register(prefix='', basename='recurso', viewset=RecursoApiViewSet) # OK

router_contenido_vistas = DefaultRouter()
router_contenido_vistas.register(prefix='', basename='contenido_vistas', viewset=contenido_vistasApiViewSet) # OK


