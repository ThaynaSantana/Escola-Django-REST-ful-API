from rest_framework import serializers
from app.models import Estudante, Curso, Matricula
from app.validators import cpf_invalido, nome_invalido, numero_invalido


class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = '__all__'

    def validate(self, dados):
        if cpf_invalido(dados['cpf']):
            raise serializers.ValidationError({'cpf': 'O CPF deve ser válido!'})
        if nome_invalido(dados['nome']):
            raise serializers.ValidationError({'nome': 'O Nome so pode conter letras!'})
        if numero_invalido(dados['numero_celular']):
            raise serializers.ValidationError({'numero_celular': 'O numero de celular deve seguir o modelo: 71 91234-5678'})


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
        fields = ['codigo', 'descricao', 'periodo']

    def get_periodo(self, obj):
        return obj.get_periodo_display()


class ListaMatriculaCursoSerializer(serializers.ModelSerializer):
    nome = serializers.ReadOnlyField(source='estudante.nome')

    class Meta:
        model = Matricula
        fields = ['nome']

    def get_nome(self, obj):
        return obj.get_nome_display()

class EstudanteSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        exclude = ['cpf','data_nascimento']