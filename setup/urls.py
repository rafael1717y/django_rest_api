from django.contrib import admin
from django.db.models import base
from django.urls import path
from django.urls.conf import include
from escola.views import AlunosViewSet, CursosViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('alunos', AlunosViewSet, basename = 'Alunos')
router.register('cursos', CursosViewSet, basename = 'Cursos')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)), 
]