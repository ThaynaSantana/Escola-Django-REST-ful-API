from django.contrib import admin
from django.urls import path, include
from app.views import EstudanteViewSet, CursoViewSet, MatriculaViewSet, ListaMatriculaEstudanteView, \
    ListaMatriculaCursoView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('estudantes', EstudanteViewSet, basename='Estudantes')
router.register('cursos', CursoViewSet, basename='Cursos')
router.register('matriculas', MatriculaViewSet, basename='Matriculas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('estudantes/<int:pk>/matriculas/', ListaMatriculaEstudanteView.as_view()),
    path('cursos/<int:pk>/matriculas/', ListaMatriculaCursoView.as_view())
]
