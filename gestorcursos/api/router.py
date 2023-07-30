from rest_framework.routers import DefaultRouter

from gestorcursos.api.views import CursoApiViewSet, CalificacionCursoApiViewSet, CursoUsuarioApiViewSet, SeccionApiViewSet, Curso_TemasApiViewSet, RequisitosApiViewSet, ClaseApiViewSet, RecursoApiViewSet, clases_vistasApiViewSet, ExamenApiViewSet, PreguntaApiViewSet, AlternativaApiViewSet, ResolverExamenApiViewSet, DetalleResolverExamenApiViewSet, RespuestaApiViewSet

router_curso = DefaultRouter()
router_curso.register(prefix='', basename='curso', viewset=CursoApiViewSet)

router_calificacioncurso = DefaultRouter()
router_calificacioncurso.register(prefix='', basename='calificacioncurso', viewset=CalificacionCursoApiViewSet)

router_cursousuario = DefaultRouter()
router_cursousuario.register(prefix='', basename='cursousuario', viewset=CursoUsuarioApiViewSet)

router_seccion = DefaultRouter()
router_seccion.register(prefix='', basename='seccion', viewset=SeccionApiViewSet)

router_curso_temas = DefaultRouter()
router_curso_temas.register(prefix='', basename='curso_temas', viewset=Curso_TemasApiViewSet)

router_requisitos = DefaultRouter()
router_requisitos.register(prefix='', basename='requisitos', viewset=RequisitosApiViewSet)

router_clase = DefaultRouter()
router_clase.register(prefix='', basename='clase', viewset=ClaseApiViewSet)

router_recurso = DefaultRouter()
router_recurso.register(prefix='', basename='recurso', viewset=RecursoApiViewSet)

router_clases_vistas = DefaultRouter()
router_clases_vistas.register(prefix='', basename='clases_vistas', viewset=clases_vistasApiViewSet)

router_examen = DefaultRouter()
router_examen.register(prefix='', basename='examen', viewset=ExamenApiViewSet)

router_pregunta = DefaultRouter()
router_pregunta.register(prefix='', basename='pregunta', viewset=PreguntaApiViewSet)

router_alternativa = DefaultRouter()
router_alternativa.register(prefix='', basename='alternativa', viewset=AlternativaApiViewSet)

router_resolverexamen = DefaultRouter()
router_resolverexamen.register(prefix='', basename='resolverexamen', viewset=ResolverExamenApiViewSet)

router_detalleresolverexamen = DefaultRouter()
router_detalleresolverexamen.register(prefix='', basename='detalleresolverexamen', viewset=DetalleResolverExamenApiViewSet)

router_respuesta = DefaultRouter()
router_respuesta.register(prefix='', basename='respuesta', viewset=RespuestaApiViewSet)


