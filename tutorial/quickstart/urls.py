from rest_framework.routers import DefaultRouter
from .views import CarreraViewSet, MateriaViewSet, AlumnoViewSet, InscripcionViewSet, CardViewSet

routes = DefaultRouter()
routes.register(r'carreras', CarreraViewSet)
routes.register(r'materias', MateriaViewSet)
routes.register(r'alumnos', AlumnoViewSet)
routes.register(r'inscripciones', InscripcionViewSet)
routes.register(r'cards', CardViewSet)

urlpatterns = routes.urls