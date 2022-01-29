from django.contrib import admin
from .models import NotesApp

class NotesAppAdmin(admin.ModelAdmin):
  list = ('title', 'description', 'completed')

admin.site.register(NotesApp, NotesAppAdmin)