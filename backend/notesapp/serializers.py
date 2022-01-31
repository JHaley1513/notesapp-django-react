from rest_framework import serializers
from .models import Note

class NoteSerializer(serializers.ModelSerializer): # For converting Note model to JSON
    class Meta:
        model = Note
        fields = ('id', 'title', 'text', 'created', 'modified', 'starred', 'deleted')