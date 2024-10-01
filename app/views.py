from app.models import Estudante, Curso, Matricula
from app.serializers import EstudanteSerializer, CursoSerializer, MatriculaSerializer, \
    ListaMatriculaEstudanteSerializer, ListaMatriculaCursoSerializer, EstudanteSerializerV2
from rest_framework import viewsets, generics, filters
from rest_framework.permissions import IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend

class EstudanteViewSet(viewsets.ModelViewSet):
    # apenas usuario autenticados podem acessar! segurança
    queryset = Estudante.objects.all()
    #serializer_class = EstudanteSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome','cpf']
    def get_serializer_class(self):
        if self.request.version == 'v2':
            return EstudanteSerializerV2
        return EstudanteSerializer

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