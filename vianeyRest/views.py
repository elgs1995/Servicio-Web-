from django.shortcuts import render
from vianeyRest.models import Usuario,Materia,Persona
from vianeyRest.serializers import  UsuarioSerializer,MateriaSerializer,PersonaSerializer
from rest_framework import generics
# Create your views here.
class UsuarioList(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class =  UsuarioSerializer

class UsuarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class MateriaList(generics.ListCreateAPIView):
    queryset = Materia.objects.all()
    serializer_class =  MateriaSerializer

class MateriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Materia.objects.all()
    serializer_class = MateriaSerializer


class PersonaList(generics.ListCreateAPIView):
    queryset = Persona.objects.all()
    serializer_class =  PersonaSerializer

class PersonaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
