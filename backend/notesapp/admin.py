from django.contrib import admin
from .models import Note

class NotesAppAdmin(admin.ModelAdmin):
  list = ('title', 'text', 'created', 'modified', 'starred', 'deleted')

admin.site.register(Note, NotesAppAdmin)