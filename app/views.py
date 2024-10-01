from app.models import Estudante, Curso, Matricula
from app.serializers import EstudanteSerializer, CursoSerializer, MatriculaSerializer, \
    ListaMatriculaEstudanteSerializer, ListaMatriculaCursoSerializer
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAdminUser

class EstudanteViewSet(viewsets.ModelViewSet):
    # apenas usuario autenticados podem acessar! segurança
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer


class CursoViewSet(viewsets.ModelViewSet):
    # apenas Admins podem acessar! segurança
    permission_classes = [IsAdminUser]

    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
    # apenas usuario autenticados podem acessar! segurança
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

class ListaMatriculaEstudanteView(generics.ListAPIView):
    # apenas usuario autenticados podem acessar! segurança
    def get_queryset(self):
        queryset = Matricula.objects.filter(estudante_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculaEstudanteSerializer

class ListaMatriculaCursoView(generics.ListAPIView):
    # apenas usuario autenticados podem acessar! segurança
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculaCursoSerializer