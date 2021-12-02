from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from curso.serializers import CursoSerializer
from django.contrib import messages

def add_curso(request):
    return render(request, 'add_curso.html')

def salvar_curso(request):
    serializer = CursoSerializer(data=request.POST)
    if serializer.is_valid():
        serializer.save()
        return HttpResponseRedirect('/')
    messages.error(request, 'Nome do curso inválido')
    return render(request, 'add_curso.html')
    