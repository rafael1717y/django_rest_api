from django.db import models
from django.db.models import fields
from rest_framework import serializers
from escola.models import Aluno, Curso

# transformando o modelo dj em json através do serializador do aluno e curso.
# tbm pode servir como filtro do que se quer disponibilizar para a API ou não. 

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'rg', 'cpf','data_nascimento']


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso 
        fields = '__all__'