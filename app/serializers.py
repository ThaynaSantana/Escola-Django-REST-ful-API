from rest_framework import serializers

from app.models import Estudante, Curso, Matricula


class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = '__all__'


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = '__all__'

class ListaMatriculaEstudanteSerializer(serializers.ModelSerializer):
    descricao = serializers.ReadOnlyField(source='curso.descricao')
    codigo = serializers.ReadOnlyField(source='curso.codigo')
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields = ['codigo','descricao','periodo']

    def get_periodo(self, obj):
        return obj.get_periodo_display()

class ListaMatriculaCursoSerializer(serializers.ModelSerializer):
    nome = serializers.ReadOnlyField(source='estudante.nome')
    class Meta:
        model = Matricula
        fields = ['nome']

    def get_nome(self,obj):
        return obj.get_nome_display()