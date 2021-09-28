from django.db import models
from django.db.models import fields
from rest_framework import serializers
from escola.models import Aluno, Curso, Matricula


# Transformando o modelo dj em json através do serializador do aluno e curso.
# tbm pode servir como filtro do que se quer disponibilizar para a API ou não. 

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'rg', 'cpf','data_nascimento']


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso 
        fields = '__all__'


class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = []


class ListaMatriculasAlunoSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']
    def get_periodo(self, obj):
        return obj.get_periodo_display()


class ListaAlunosMatriculadosSerializer(serializers.ModelSerializer):
    aluno_nome = serializers.ReadOnlyField(source='alunos.nome')
    class Meta:
        model = Matricula
        fields = ['aluno_nome']