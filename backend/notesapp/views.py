from django.shortcuts import render
from rest_framework import viewsets # provides base implementation for CRUD operations
from .serializers import NoteSerializer
from .models import Note

class NoteView(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()
