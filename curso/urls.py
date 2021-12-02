from django.urls import path
from .views import add_curso, salvar_curso

urlpatterns = [
    path('curso/', add_curso, name="add_curso"),
    path('salvar_curso/', salvar_curso, name="salvar_curso"),
]
