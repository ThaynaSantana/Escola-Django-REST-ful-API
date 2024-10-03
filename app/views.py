from app.models import Estudante, Curso, Matricula
from app.serializers import EstudanteSerializer, CursoSerializer, MatriculaSerializer, \
    ListaMatriculaEstudanteSerializer, ListaMatriculaCursoSerializer, EstudanteSerializerV2
from rest_framework import viewsets, generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.throttling import UserRateThrottle

from app.throtlles import MatriculaAnoRateThrotlle


class EstudanteViewSet(viewsets.ModelViewSet):
    queryset = Estudante.objects.all().order_by('id')
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome', 'cpf']

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return EstudanteSerializerV2
        return EstudanteSerializer


class CursoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CursoSerializer
    queryset = Curso.objects.all().order_by('id')
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['codigo']
    search_fields = ['codigo', 'nivel']



class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all().order_by('id')
    serializer_class = MatriculaSerializer
    throttle_classes = [UserRateThrottle, MatriculaAnoRateThrotlle]
    http_method_names = ['get','post']


class ListaMatriculaEstudanteView(generics.ListAPIView):
    """
    Descrição da View:
    - Lista Matriculas por id de Estudante
    Parâmetros:
    - pk (int): O identificador primário do objeto. Deve ser um int.
    """
    def get_queryset(self):
        queryset = Matricula.objects.filter(estudante_id=self.kwargs['pk']).order_by('id')
        return queryset

    serializer_class = ListaMatriculaEstudanteSerializer


class ListaMatriculaCursoView(generics.ListAPIView):
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk']).order_by('id')
        return queryset

    serializer_class = ListaMatriculaCursoSerializer
